import streamlit as st
import sqlite3
import ollama
import time
import random
import re
from datetime import datetime
from tools import ProductSearchTools
from typing import List, Dict
from data_constants import INDIAN_CITIES

# Add custom CSS for rounded images and modern design
st.markdown(
    """
    <style>
    .rounded-image {
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease-in-out;
    width: 200px; /* Set the width /
    height: 300px; / Maintain aspect ratio and cover the entire area */
    }
    .rounded-image:hover {
    transform: scale(1.05);
    }
    .stTextInput>div>div>input {
    border-radius: 20px;
    border: 1px solid #ddd;
    padding-left: 20px;
    }
    .stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 20px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    border: none;
    }
    .stButton>button:hover {
    background-color: #367C39;
    }
    .sidebar .sidebar-content {
    background-color: #f0f2f6;
    }
    h1 {
    color: #333;
    text-align: center;
    }
    h2 {
    color: #333;
    }
    h3 {
    color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

class ProductSearchApp:
    def __init__(self, db_path="products.db"):
        """Initializes the ProductSearchApp with a database path."""
        self.db_path = db_path
        self.tools = ProductSearchTools(db_path=self.db_path)
        if 'history' not in st.session_state:
            st.session_state.history = []
        if 'applied_promos' not in st.session_state:
            st.session_state.applied_promos = {}

    def get_comparison_summary(self, products: List[Dict]) -> str:
        """Summarize price comparison details using LLM, suggest best one"""
        try:
            if not products:
                return "No products to compare."

            prompt = f"""
            Summarize these products and suggest the best one based on price and features:
            """
            for product in products:
                prompt += f"""
                - {product['product_name']} on {product['ecommerce_site']}:
                  - Brand: {product['brand']}
                  - Category: {product['category']}
                  - Price: ₹{product['price']:,.2f}
                  - Description: {product['description']}
                """

            response = ollama.chat(
                model='llama3.2',
                messages=[
                    {
                        'role': 'system',
                        'content': 'You are a helpful shopping assistant specializing in comparing products and suggesting the best option to the user.  Be concise. Ensure prices are in Indian Rupees (₹). Recommend what item to buy if user is on tight budget.'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"Sorry, I encountered an error while generating the price comparison summary: {str(e)}"

    def get_shipping_refund_summary(self, product: Dict, target_date: datetime, location: str) -> str:
        """Summarize shipping and refund details using LLM"""
        try:
            shipping_info = self.tools.get_shipping_info(product, target_date, location)
            refund_info = self.tools.get_refund_info(product)

            prompt = f"""
            Summarize the shipping and refund information for {product['product_name']}.

            Shipping Information:
            - Delivery Location: {shipping_info['location']}
            - Standard Delivery Date: {shipping_info['standard_delivery_date'].strftime('%B %d, %Y')}
            - Standard Shipping Cost: ₹{shipping_info['shipping_cost']:.2f}
            - Express Delivery Date: {shipping_info['express_delivery_date'].strftime('%B %d, %Y')}
            - Express Shipping Cost: ₹{shipping_info['express_shipping_cost']:.2f}
            - Same Day Delivery Available: {shipping_info['same_day_available']}

            Refund Information:
            - Return Window: {refund_info['return_window_days']} days
            - Full Refund Condition: {refund_info['full_refund_condition']}
            - Partial Refund Condition: {refund_info['partial_refund_condition']}
            - Non-Returnable Condition: {refund_info['non_returnable_condition']}
            """

            response = ollama.chat(
                model='llama3.2',
                messages=[
                    {
                        'role': 'system',
                        'content': 'You are a helpful shopping assistant. Provide concise summaries for shipping and refund information.'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"Sorry, I encountered an error while generating the shipping and refund summary: {str(e)}"

    def get_llm_response(self, query: str) -> str:
        """Get response from LLM when no products are found"""
        try:
            response = ollama.chat(
                model='llama3.2',
                messages=[
                    {
                        'role': 'system',
                        'content': 'You are a helpful shopping assistant. When products are not found, provide helpful alternative suggestions and related product recommendations. Be very concise.'
                    },
                    {
                        'role': 'user',
                        'content': f"I'm looking for {query}, but couldn't find it in our store. Please provide helpful suggestions and alternatives."
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"Sorry, I encountered an error while processing your request: {str(e)}"

    def summarize_product(self, product: Dict) -> str:
        """Summarize product details only using LLM"""
        try:
            prompt = f"""
            Summarize the following product details in a concise and engaging way.  Make sure to use Indian Rupees for the price.
            Product Name: {product['product_name']}
            Description: {product['description']}
            Brand: {product['brand']}
            Category: {product['category']}
            Color: {product['color']}
            Size: {product['size']}
            Ecommerce Site: {product['ecommerce_site']}
            Price: ₹{product['price']:,.2f}
            """
            response = ollama.chat(
                model='llama3.2',
                messages=[
                    {
                        'role': 'system',
                        'content': 'You are a helpful shopping assistant. Provide concise and engaging summaries of product details. Ensure that prices are shown in Indian Rupees (₹).'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )
            return response['message']['content']
        except Exception as e:
            return f"Sorry, I encountered an error while summarizing: {str(e)}"

    def display_product_image(self, image_url: str):
        """Display product image with rounded corners using Streamlit's st.image"""
        st.markdown(
            f"""
            <div class="rounded-image">
                <img src="{image_url}" alt="Product Image" style="width: 200px; height: 300px; object-fit: cover; border-radius: 10px;">
            </div>
            """,
            unsafe_allow_html=True
        )

    def display_shipping_info(self, product: Dict, shipping_info: Dict, target_date: datetime, location: str):
        """Display shipping information in a formatted way"""
        with st.expander("📦 Shipping Details"):
            # Location information
            st.markdown(f"**Delivery Location:** {shipping_info['location']} ({shipping_info['location_type']})")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Standard Delivery:**")
                st.write(f"- Date: {shipping_info['standard_delivery_date'].strftime('%B %d, %Y')}")
                st.write(f"- Cost: ₹{shipping_info['shipping_cost']:.2f}")

            with col2:
                st.markdown("**Express Delivery:**")
                st.write(f"- Date: {shipping_info['express_delivery_date'].strftime('%B %d, %Y')}")
                st.write(f"- Cost: ₹{shipping_info['express_shipping_cost']:.2f}")

            st.markdown(f"**Delivery Zone:** {shipping_info['delivery_zones']}")
            if shipping_info['same_day_available']:
                st.success("✓ Same-day delivery available in your area")
            else:
                st.info("ℹ️ Same-day delivery not available in your area")
            with st.spinner("Generating AI Summary for Shipping..."):
                shipping_summary = self.get_shipping_refund_summary(product, target_date, location)
                st.subheader("AI Summary for Shipping:")
                st.write(shipping_summary)

    def display_refund_info(self, product: Dict, refund_info: Dict, target_date: datetime, location: str):
        """Display refund policy information in a formatted way"""
        with st.expander("↩️ Return & Refund Policy"):
            st.markdown(f"**Return Window:** {refund_info['return_window_days']} days")

            st.markdown("**Full Refund Conditions:**")
            st.write(refund_info['full_refund_condition'])

            st.markdown("**Partial Refund Conditions:**")
            st.write(refund_info['partial_refund_condition'])

            st.markdown("**Non-Returnable Conditions:**")

        with st.spinner("Generating AI Summary for Refund..."):
                refund_summary = self.get_shipping_refund_summary(product, target_date, location)
                st.subheader("AI Summary for Refund:")
                st.write(refund_summary)

    def display_price_comparison(self, products: List[Dict]):
        """Display price comparison results and AI summary, recommend best choice"""
        #with st.expander("💰 Price Comparison and AI Recommendation"):
        if not products:
            st.warning("No matching products found for price comparison.")
            return

        with st.spinner("Generating AI Comparison Summary and Recommendation..."):
            comparison_summary = self.get_comparison_summary(products)
            st.subheader("AI Comparison Summary and Recommendation:")
            st.write(comparison_summary)

        for product in products:
            with st.expander(f"Details for {product['product_name']} on {product['ecommerce_site']}"):

                st.markdown(f"**{product['ecommerce_site']}**")
                self.display_product_image(product['image_url'])
                st.write(f"- **Price:** ₹{product['price']:,.2f}")
                st.write(f"- **Brand:** {product['brand']}")
                st.write(f"- **Category:** {product['category']}")
                if product['color'] != 'N/A':
                    st.write(f"- **Color:** {product['color']}")
                if product['size'] != 'N/A':
                    st.write(f"- **Size:** {product['size']}")
                st.write("---")

    def display_product_details(self, product: Dict, promo_code: str = None, target_date: datetime = datetime.now(), location: str = "Delhi"):
        """Displays the product details in a structured format."""
        col1, col2 = st.columns([1, 2])

        with col1:
            self.display_product_image(product['image_url'])

        with col2:
            st.subheader(product['product_name'])  # Moved product name to the top
            st.markdown(f"**Brand:** {product['brand']}")
            st.markdown(f"**Store:** {product['ecommerce_site']}")
            st.markdown(f"**Category:** {product['category']}")
            if product['color'] != 'N/A':
                st.markdown(f"**Color:** {product['color']}")
            if product['size'] != 'N/A':
                st.markdown(f"**Size:** {product['size']}")

            original_price = product['price']
            current_price = self.tools.apply_promo_code(product['product_id'], original_price, promo_code)

            promo_info = self.tools.get_promo_code_info(product['product_id'])

            if promo_code:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()

                cursor.execute("""
                    SELECT discount, description FROM promo_codes WHERE code = ?
                """, (promo_code,))

                result = cursor.fetchone()
                conn.close()
                if result:
                    discount_percentage = result[0]
                    description = result[1]
                    st.markdown("**Manually Applied Promo Code:**")
                    st.code(promo_code)
                    st.markdown(f"*{description}*")
                    st.markdown(f"**Original Price:** ~~₹{original_price:,.2f}~~")
                    st.markdown(f"**Discounted Price:** ₹{current_price:,.2f}")
                    st.success(f"Promo code applied! You save ₹{original_price - current_price:,.2f}")
            # If no manual promo, handle default promo
            elif promo_info:
                st.markdown("**Available Promo Code:**")
                col_promo1, col_promo2 = st.columns([2, 1])
                with col_promo1:
                    st.code(promo_info['code'])
                    st.markdown(f"*{promo_info['description']}*")
                with col_promo2:
                    if str(product['product_id']) not in st.session_state.applied_promos:
                        if st.button("Apply Promo", key=f"promo_{product['product_id']}"):
                            st.session_state.applied_promos[str(product['product_id'])] = True
                            st.rerun()

            if str(product['product_id']) in st.session_state.applied_promos and not promo_code:
                st.markdown(f"**Original Price:** ~~₹{original_price:,.2f}~~")
                st.markdown(f"**Discounted Price:** ₹{current_price:,.2f}")
                st.success(f"Promo code applied! You save ₹{original_price - current_price:,.2f}")
            elif not promo_code:
                st.markdown(f"**Price:** ₹{current_price:,.2f}")

    def display_ai_summary(self, product: Dict):
        """Displays the AI-generated summary of the product."""
        with st.spinner("Generating AI Summary..."):
            product_summary = self.summarize_product(product)
            st.subheader("AI Summary:")
            st.write(product_summary)

    def display_product_description(self, product: Dict):
        """Displays the product description."""
        with st.expander("Product Description"):
            st.write(product['description'])

    def display_similar_products(self, products: List[Dict]):
        """Displays a list of similar products."""
        if len(products) > 1:
            with st.expander("Other Matching Products"):
                for product in products[1:]:
                    st.markdown(f"- **{product['product_name']}** by {product['brand']} (₹{product['price']:,.2f})")

    def run(self):
        """Runs the main Streamlit application."""
        st.title("🛍️ Smart Product Search")
        st.markdown("""
        Search products and get detailed shipping & refund information:
        - Check product availability and details
        - View estimated delivery dates and shipping costs
        - Check refund and return policies
        - Location-based delivery estimates
        - Compare prices across multiple platforms
        """)

        # Location selector
        selected_location = st.sidebar.selectbox(
            "📍 Select Your City",
            options=sorted(
                INDIAN_CITIES['major_cities'] +
                INDIAN_CITIES['tier_2_cities'] +
                INDIAN_CITIES['other_cities']
            )
        )

        query = st.text_input(
            "🔍 What would you like to know?",
            placeholder="e.g., 'When will Rolex Submariner arrive if I order today?' or 'Show me refund policy for AirPods Pro'"
        )

        if query:
            # Detect the intent and location of the query
            intent = self.tools.detect_intent(query)
            target_date, date_info = self.tools.parse_date_from_query(query)
            location = self.tools.detect_location(query) or selected_location

            # Check for specific promo code mentioned in the query
            promo_code = None
            promo_match = re.search(r'code (\w+)|discount code (\w+)|promo code (\w+)', query.lower())
            if promo_match:
                promo_code = next((group for group in promo_match.groups() if group is not None), None).upper()
                query = query.replace(promo_match.group(0), '')

            # Choose a random preview duration between 1 and 4 seconds
            preview_duration = random.uniform(1, 4)

            # Show loading preview based on intent
            if intent == 'search':
                preview_message = "🔍 Searching for products..."
            elif intent == 'compare':
                preview_message = "📊 Comparing product prices..."
            elif intent == 'shipping':
                preview_message = "🚚 Getting shipping information..."
            elif intent == 'refund':
                preview_message = "↩️ Fetching refund policies..."
            elif intent == 'discount':
                preview_message = "💰 Finding available discounts..."
            elif intent == 'stock':
                preview_message = "📦 Checking stock availability..."
            else:
                preview_message = "🤔 Processing your request..."

            preview_placeholder = st.empty()
            preview_placeholder.info(preview_message)
            time.sleep(preview_duration)  # Wait for the random duration
            preview_placeholder.empty()   # Clear the preview message

            with st.spinner("Processing your request..."):
                products = self.tools.search_products(query)

                if products:
                    # For stock checking
                    if intent == 'stock':
                        product = products[0]
                        in_stock = self.tools.check_stock_availability(product)
                        if in_stock:
                            st.success(f"✅ {product['product_name']} is in stock!")
                        else:
                            st.error(f"❌ {product['product_name']} is currently out of stock!")

                    if intent == 'compare':
                        product_name = products[0]['product_name']
                        comparison_products = self.tools.compare_prices(product_name)
                        if comparison_products:
                            self.display_price_comparison(comparison_products)
                        else:
                            st.warning("No matching products found for comparison.")

                    else:
                        # Display only the first product if intent is not compare
                        product = products[0]  # Select the first product
                        self.display_product_details(product, promo_code, target_date, location)

                        if intent == 'shipping':
                            shipping_info = self.tools.get_shipping_info(product, target_date, location)
                            self.display_shipping_info(product, shipping_info, target_date, location)

                        elif intent == 'refund':
                            refund_info = self.tools.get_refund_info(product)
                            self.display_refund_info(product, refund_info, target_date, location)

                        elif intent == 'discount':
                            with st.spinner("Generating AI Summary for Discount..."):
                                ai_summary = self.summarize_product(product)
                                st.subheader("AI Summary")
                                st.write(ai_summary)

                        else:  # Default: just search intent
                            self.display_ai_summary(product)

                        self.display_product_description(product)
                        self.display_similar_products(products[1:]) # Changed to slice to exclude first element

                else:
                    with st.spinner("No exact matches found. Getting AI recommendations..."):
                        llm_response = self.get_llm_response(query)
                        st.info("💡 AI Assistant Recommendations:")
                        st.write(llm_response)

if __name__ == "__main__":
    app = ProductSearchApp()
    app.run()