import sqlite3
import random
from typing import List, Dict, Tuple
import re
from collections import defaultdict
from datetime import datetime, timedelta
import calendar
from data_constants import INDIAN_CITIES
from fuzzywuzzy import fuzz

class ProductSearchTools:
    def __init__(self, db_path="products.db"):
        self.db_path = db_path
        self.intent_patterns = {
            'shipping': r'(deliver|shipping|arrive|get|order|ready by|receive|when|delivery)',
            'refund': r'(refund|return|exchange|money back|warranty|guarantee)',
            'search': r'(find|show|search|looking for|want|need|available)',
            'compare': r'(compare|price comparison|cheaper|best price|lowest price|comparison|deals|any better deals)',
            'discount': r'(discount|promo|coupon|code|offer|deal|save)',
            'stock': r'(stock|in stock|available|inventory)'  # Added stock check intent
        }

    def detect_location(self, query: str) -> str:
        """Detect location from query or return default"""
        query_lower = query.lower()

        # Check for cities in the query
        for category in INDIAN_CITIES.values():
            for city in category:
                if city.lower() in query_lower:
                    return city

        return "Delhi"  # Default city

    def parse_date_from_query(self, query: str) -> tuple:
        """Extract date information from the query"""
        today = datetime.now()

        # Handle day names
        days = {day.lower(): i for i, day in enumerate(calendar.day_name)}
        for day, day_num in days.items():
            if day in query.lower():
                target_date = today
                while target_date.weekday() != day_num:
                    target_date += timedelta(days=1)
                return target_date, f"Requested for {day.title()}"

        # Handle relative dates
        if "tomorrow" in query.lower():
            return today + timedelta(days=1), "Requested for tomorrow"
        if "next week" in query.lower():
            return today + timedelta(weeks=1), "Requested for next week"

        # Specific date mentioned (e.g., "by 15th July")
        date_match = re.search(r'by (\d+)(?:st|nd|rd|th)? (\w+)', query.lower())
        if date_match:
            day = int(date_match.group(1))
            month_name = date_match.group(2)
            try:
                month = datetime.strptime(month_name, '%B').month  # Full month name
            except ValueError:
                try:
                    month = datetime.strptime(month_name, '%b').month  # Abbreviated month name
                except ValueError:
                    return today, "Invalid date format"

            year = today.year
            try:
                specific_date = datetime(year, month, day)
                if specific_date < today:
                    specific_date = datetime(year + 1, month, day)  # If date is in the past, assume next year
                return specific_date, f"Requested for {specific_date.strftime('%B %d, %Y')}"
            except ValueError:
                return today, "Invalid date"

        return today, "No specific date mentioned, assuming today"

    def detect_intent(self, query: str) -> str:
        """Detect the primary intent of the query using regular expressions."""
        for intent, pattern in self.intent_patterns.items():
            if re.search(pattern, query.lower()):
                return intent
        return 'search'

    def tokenize_query(self, query: str) -> List[str]:
        """Convert query into meaningful tokens"""
        query = re.sub(r'[^\w\s]', ' ', query.lower())
        stop_words = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it',
                     'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with'}
        return [word for word in query.split() if word not in stop_words]

    def calculate_relevance_score(self, product: Dict, query_tokens: List[str]) -> Tuple[float, Dict]:
        """Calculate relevance score for a product using fuzzy matching."""
        score = 0
        match_details = defaultdict(list)

        product_name_tokens = self.tokenize_query(product['product_name'])
        description_tokens = self.tokenize_query(product['description'])

        # Use Fuzzy Matching
        for token in query_tokens:
            # Fuzzy match on product name
            name_ratio = fuzz.partial_ratio(token, product['product_name'].lower())
            if name_ratio > 80:  # Adjust threshold as needed
                score += 3.0 * (name_ratio / 100)  # Scale score by fuzzy ratio
                match_details['name'].append(token)

            # Fuzzy match on description
            description_ratio = fuzz.partial_ratio(token, product['description'].lower())
            if description_ratio > 70:  # Adjust threshold as needed
                score += 1.0 * (description_ratio / 100)  # Scale score by fuzzy ratio
                match_details['description'].append(token)

            if token == product['brand'].lower():
                score += 2.0
                match_details['brand'].append(token)
            if token == product['category'].lower():
                score += 1.5
                match_details['category'].append(token)

        return score, match_details

    def search_products(self, query: str) -> List[Dict]:
        """Search products with enhanced relevance scoring"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Extract price constraint if present
        price_limit = None
        price_match = re.search(r'under (?:rupees|₹) ?(\d+)', query, re.IGNORECASE)
        if price_match:
            price_limit = int(price_match.group(1))
            query = query.replace(price_match.group(0), '')  # Remove price constraint from query

        # Extract size constraint if present
        size_needed = None
        size_match = re.search(r'size (\w+)', query)
        if size_match:
            size_needed = size_match.group(1).upper()
            query = query.replace(size_match.group(0), '')  # Remove size constraint from query

        cursor.execute("SELECT * FROM products")
        columns = [desc[0] for desc in cursor.description]
        products = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()

        query_tokens = self.tokenize_query(query)
        scored_products = []

        for product in products:
            # Apply price filtering, if specified
            if price_limit is not None and product['price'] > price_limit:
                continue

            # Apply size filtering, if specified
            if size_needed is not None and product['size'].upper() != size_needed:
                continue

            score, match_details = self.calculate_relevance_score(product, query_tokens)
            if score > 0:
                product['relevance_score'] = score
                product['match_details'] = match_details
                scored_products.append(product)

        scored_products.sort(key=lambda x: x['relevance_score'], reverse=True)

        return scored_products

    def check_stock_availability(self, product: Dict) -> bool:
        """Simulate checking stock availability (replace with actual logic)"""
        # In a real application, this would involve querying an inventory system
        # Here, we just return a random boolean for demonstration purposes
        return random.choice([True, False])

    def get_shipping_info(self, product: Dict, target_date: datetime, location: str) -> Dict:
        """Get shipping information for a product"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT sp.* FROM shipping_policies sp
            JOIN products p ON p.shipping_policy_id = sp.policy_id
            WHERE p.product_id = ?
        """, (product['product_id'],))

        shipping_policy = dict(zip([d[0] for d in cursor.description], cursor.fetchone()))
        conn.close()

        today = datetime.now()

        # Adjust delivery times based on location
        location_factor = 1.0
        if location in INDIAN_CITIES['major_cities']:
            location_factor = 1.0
        elif location in INDIAN_CITIES['tier_2_cities']:
            location_factor = 1.5
        else:
            location_factor = 2.0

        standard_days = int(shipping_policy['standard_delivery_days'] * location_factor)
        express_days = int(shipping_policy['express_delivery_days'] * location_factor)

        standard_delivery = today + timedelta(days=standard_days)
        express_delivery = today + timedelta(days=express_days)

        return {
            'standard_delivery_date': standard_delivery,
            'express_delivery_date': express_delivery,
            'same_day_available': shipping_policy['same_day_available'] and location in INDIAN_CITIES['major_cities'],
            'delivery_zones': shipping_policy['delivery_zones'],
            'shipping_cost': shipping_policy['shipping_cost'],
            'express_shipping_cost': shipping_policy['express_shipping_cost'],
            'can_meet_target': express_delivery <= target_date,  # Accurate target date check
            'location': location,
            'location_type': 'Major City' if location in INDIAN_CITIES['major_cities'] else
                           'Tier 2 City' if location in INDIAN_CITIES['tier_2_cities'] else 'Other City'
        }

    def get_refund_info(self, product: Dict) -> Dict:
        """Get refund policy information for a product"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT rp.* FROM refund_policies rp
            JOIN products p ON p.refund_policy_id = rp.policy_id
            WHERE p.product_id = ?
        """, (product['product_id'],))

        refund_policy = dict(zip([d[0] for d in cursor.description], cursor.fetchone()))
        conn.close()

        return refund_policy

    def compare_prices(self, product_name: str) -> List[Dict]:
        """Compare prices of the same product across different platforms"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM products
            WHERE product_name = ?
        """, (product_name,))

        columns = [desc[0] for desc in cursor.description]
        products = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()

        return products

    def get_promo_code_info(self, product_id: int) -> dict:
        """Get promo code information for a product"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT p.promo_code, pc.discount, pc.description
            FROM products p
            JOIN promo_codes pc ON p.promo_code = pc.code
            WHERE p.product_id = ?
        """, (product_id,))

        result = cursor.fetchone()
        conn.close()

        if result:
            return {
                'code': result[0],
                'discount': result[1],
                'description': result[2]
            }
        return None

    def apply_promo_code(self, product_id: int, original_price: float, promo_code: str = None) -> float:
        """Apply promo code discount to product price"""
        if promo_code:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            cursor.execute("""
                SELECT discount FROM promo_codes WHERE code = ?
            """, (promo_code,))

            result = cursor.fetchone()
            conn.close()

            if result and result[0] is not None:
                discount_percentage = result[0]
                discounted_price = original_price * (1 - discount_percentage/100)
                return round(discounted_price, 2)
            else:
                return original_price  # Return original price if promo code is invalid
        else:
            promo_info = self.get_promo_code_info(product_id)
            if promo_info:
                discount_percentage = promo_info['discount']
                discounted_price = original_price * (1 - discount_percentage/100)
                return round(discounted_price, 2)
        return original_price