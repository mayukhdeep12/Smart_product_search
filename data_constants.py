# data_constants.py
PRODUCTS_DATA = [
    # Each tuple represents a product with the following fields:
    # (product_name, description, price, image_url, product_url, category, color, size, brand, ecommerce_site, promo_code)

    # Electronics
    (
        "Sony WH-1000XM4",
        "Premium noise-cancelling headphones with industry-leading technology (Standard Model)",
        24517,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/61oqO1AMbdL._AC_UF1000%2C1000_QL80_.jpg?v=1740336486729",
        "https://example.com/sony",
        "Electronics",
        "Black",
        "N/A",
        "Sony",
        "BestBuy",
        "SAVE10"
    ),
    (
        "Sony WH-1000XM4",
        "Premium noise-cancelling headphones with industry-leading technology (Enhanced Bass)",
        26239, 
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/sony-wh-1000xm4_qjn8.jpg?v=1740336492418",
        "https://example.com/sony",
        "Electronics",
        "Silver",
        "N/A",
        "Sony",
        "Amazon",
        "MUSIC15"
    ),
    (
        "Sony WH-1000XM4",
        "Premium noise-cancelling headphones with industry-leading technology (Pro Edition)",
        27059,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/61UgZSYRllL.jpg?v=1740336494522",
        "https://example.com/sony",
        "Electronics",
        "Silver",
        "N/A",
        "Sony",
        "Walmart",
        "AUDIO20"
    ),
    
    (
        "Apple AirPods Pro",
        "Active noise cancellation earbuds with spatial audio (2nd Gen)",
        18039,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/download.jpg?v=1740336781856",
        "https://example.com/airpods",
        "Electronics",
        "White",
        "N/A",
        "Apple",
        "AppleStore",
        "PODS15"
    ),
    (
        "Apple AirPods Pro",
        "Active noise cancellation earbuds with spatial audio (2nd Gen, Compact)",
        17219,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/Apple_AirPods-Pro_New-Design_102819_big.jpg.large.jpg?v=1740336782167",
        "https://example.com/airpods",
        "Electronics",
        "White",
        "N/A",
        "Apple",
        "Amazon",
        "APPLE10"
    ),
    (
        "Apple AirPods Pro",
        "Active noise cancellation earbuds with spatial audio (Enhanced Connectivity)",
        18859,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/Apple_AirPods-Pro_New-Design_102819_big.jpg.large.jpg?v=1740336782167",
        "https://example.com/airpods",
        "Electronics",
        "White",
        "N/A",
        "Apple",
        "BestBuy",
        "SAVE15"
    ),
    
    (
        "Samsung Galaxy Watch 5",
        "Advanced smartwatch with health tracking (Standard Edition)",
        21319,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/galaxy-watch5-pro-battery-display-mo.webp?v=1740336880562",
        "https://example.com/watch",
        "Electronics",
        "Silver",
        "44mm",
        "Samsung",
        "Samsung Store",
        "WATCH10"
    ),
    (
        "Samsung Galaxy Watch 5",
        "Advanced smartwatch with health tracking (Sport Edition)",
        20500,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/61aVQDazNHL._AC_UF1000%2C1000_QL80_.jpg?v=1740336880562",
        "https://example.com/watch",
        "Electronics",
        "Silver",
        "44mm",
        "Samsung",
        "Amazon",
        "WEARABLE15"
    ),
    (
        "Samsung Galaxy Watch 5",
        "Advanced smartwatch with health tracking (Premium Edition)",
        22139,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/61aVQDazNHL._AC_UF1000%2C1000_QL80_.jpg?v=1740336880562",
        "https://example.com/watch",
        "Electronics",
        "Silver",
        "44mm",
        "Samsung",
        "BestBuy",
        "SAVE10"
    ),
    
    (
        "MacBook Pro M2",
        "Professional laptop with Apple Silicon (13-inch, M2)",
        114799,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/mbp-spacegray-select-202206-removebg-preview_1_.png?v=1740336981450",
        "https://example.com/macbook",
        "Electronics",
        "Space Gray",
        "13inch",
        "Apple",
        "AppleStore",
        "MAC100"
    ),
    (
        "MacBook Pro M2",
        "Professional laptop with Apple Silicon (14-inch, M2)",
        110699,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/CMC_1384.webp?v=1740336980035",
        "https://example.com/macbook",
        "Electronics",
        "Space Gray",
        "14inch",
        "Apple",
        "Amazon",
        "APPLE10"
    ),
    (
        "MacBook Pro M2",
        "Professional laptop with Apple Silicon (15-inch, M2 Pro)",
        118899,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/CMC_1384.webp?v=1740336980035",
        "https://example.com/macbook",
        "Electronics",
        "Space Gray",
        "15inch",
        "Apple",
        "BestBuy",
        "LAPTOP50"
    ),
    
    # Smart Home
    (
        "Philips Hue Starter Kit",
        "Smart lighting system with bridge and bulbs (Starter Kit)",
        14759,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/8719514291515-929002468811-Philips-Hue_WCA-9W-A60-E27-3set-EUR-PMO-RTP.webp?v=1740337060493",
        "https://example.com/hue",
        "Smart Home",
        "White",
        "N/A",
        "Philips",
        "SmartHome",
        "LIGHT20"
    ),
    (
        "Philips Hue Starter Kit",
        "Smart lighting system with bridge and bulbs (Compact Edition)",
        13939,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/046677563271-929002468305-Philips-Hue_WA-10_5W-A19-E26-4set-US-RTP.webp?v=1740337059175",
        "https://example.com/hue",
        "Smart Home",
        "White",
        "N/A",
        "Philips",
        "Amazon",
        "HOME15"
    ),
    (
        "Philips Hue Starter Kit",
        "Smart lighting system with bridge and bulbs (Extended Bundle)",
        15579,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/046677563271-929002468305-Philips-Hue_WA-10_5W-A19-E26-4set-US-RTP.webp?v=1740337059175",
        "https://example.com/hue",
        "Smart Home",
        "White",
        "N/A",
        "Philips",
        "BestBuy",
        "SMART10"
    ),
    
    (
        "Nest Learning Thermostat",
        "AI-powered smart thermostat (Latest Model)",
        18859,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/71ubizMsdKL._AC_UF894%2C1000_QL80_.jpg?v=1740337127907",
        "https://example.com/nest",
        "Smart Home",
        "Steel",
        "N/A",
        "Google",
        "Google Store",
        "NEST25"
    ),
    (
        "Nest Learning Thermostat",
        "AI-powered smart thermostat (Eco Edition)",
        18039,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/71ubizMsdKL._AC_UF894%2C1000_QL80_.jpg?v=1740337127907",
        "https://example.com/nest",
        "Smart Home",
        "Steel",
        "N/A",
        "Google",
        "Amazon",
        "HOME15"
    ),
    (
        "Nest Learning Thermostat",
        "AI-powered smart thermostat (Pro Edition)",
        19679,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/670cbf81a3354e75d970456a-google-nest-learning-thermostat.jpg?v=1740337127306",
        "https://example.com/nest",
        "Smart Home",
        "Steel",
        "N/A",
        "Google",
        "BestBuy",
        "SMART10"
    ),
    
    # Luxury Items
    (
        "Rolex Submariner",
        "Luxury diving watch in steel (Classic Model)",
        721599,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/m126610lv-0002_drp-upright-bba-with-shadow.png?v=1740337196034",
        "https://example.com/rolex",
        "Luxury",
        "Silver",
        "41mm",
        "Rolex",
        "AuthorizedDealer",
        "LUXURY500"
    ),
    (
        "Rolex Submariner",
        "Luxury diving watch in steel (Limited Edition)",
        713399,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/m126619lb-0003_drp-upright-bba-with-shadow.webp?v=1740337198182",
        "https://example.com/rolex",
        "Luxury",
        "Silver",
        "41mm",
        "Rolex",
        "Amazon",
        "WATCH250"
    ),
    (
        "Rolex Submariner",
        "Luxury diving watch in steel (Heritage Edition)",
        746199,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/m126619lb-0003_drp-upright-bba-with-shadow.webp?v=1740337198182",
        "https://example.com/rolex",
        "Luxury",
        "Silver",
        "41mm",
        "Rolex",
        "Chrono24",
        "TIME200"
    ),

    # Clothes
    (
        "Floral Skirt",
        "A beautiful floral print skirt, perfect for spring.",
        3280,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/30-p-2-skirt-bhutaiya-original-imagg7f2nuyzr2ys.webp?v=1740337261222",
        "https://example.com/skirt",
        "Clothes",
        "Multicolor",
        "S",
        "Generic",
        "SiteA",
        "SPRING15"
    ),
    (
        "Floral Skirt",
        "Elegant floral skirt, ideal for parties and outings.",
        2460,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/81j8GLFxpLL._AC_UY1100_.jpg?v=1740337262067",
        "https://example.com/skirt2",
        "Clothes",
        "Red/Pink",
        "S",
        "DesignerBrand",
        "SiteB",
        "FASHION10"
    ),
    (
        "Floral Skirt",
        "Casual floral skirt, great for everyday wear.",
        2870,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/81SWoBylGfL._AC_UY1100_.jpg?v=1740337263660",
        "https://example.com/skirt3",
        "Clothes",
        "Blue/Green",
        "M",
        "Generic",
        "SiteC",
        "STYLE20"
    ),
    (
        "Casual Denim Jacket",
        "A classic denim jacket, suitable for all seasons.",
        6560,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/91sBFBcL6GL._AC_UY1100_.jpg?v=1740337330270",
        "https://example.com/jacket",
        "Clothes",
        "Blue",
        "M",
        "Levi's",
        "SiteA",
        "DENIM25"
    ),
        (
        "Casual Denim Jacket",
        "A comfy Denim jacket for the casual outing.",
        5740,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/mens-denim-jackets-1-500x500.webp?v=1740337332376",
        "https://example.com/jacket1",
        "Clothes",
        "Blue",
        "S",
        "US POLO",
        "SiteB",
        "DENIM30"
    ),
    (
        "Cocktail Dress",
        "A stunning cocktail dress for special occasions.",
        9840,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/CD0187_rosegold_1_18fcbc1a-b22a-4b9f-a25f-eaf05f184d98-660593_1200x.webp?v=1740337411648",
        "https://example.com/dress",
        "Clothes",
        "Black",
        "L",
        "DesignerBrand",
        "SiteB",
        "PARTY30"
    ),

    # Shoes
    (
        "White Sneakers",
        "Classic white sneakers, perfect for everyday comfort.",
        5740,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/c28d223f-6a82-46be-8922-6a21172bd2841653714541319AfroJackWomenWhiteSneakers1.jpg?v=1740337468079",
        "https://example.com/sneakers",
        "Shoes",
        "White",
        "8",
        "Adidas",
        "SiteC",
        "SPORT10"
    ),
        (
        "White Sneakers",
        "Stylish white sneakers, perfect for gym.",
        4920, 
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/8-line-shoes-fashion-white-original-imag687guzw86huz.webp?v=1740337468325",
        "https://example.com/sneakers1",
        "Shoes",
        "White",
        "7",
        "Nike",
        "SiteA",
        "SPORT15"
    ),
        (
        "White Sneakers",
        "Casual white sneakers, suitable for walks.",
        4100,  
        "https://cdn.glitch.global/f85b9cad-76d1-4a2c-85f9-10087647d4de/RSL0025_1.webp?v=1740337470491",
        "https://example.com/sneakers2",
        "Shoes",
        "White",
        "8",
        "Puma",
        "SiteB",
        "SUMMER15"
    ),
]

SHIPPING_POLICIES = [
    # ecommerce_site, standard_days, express_days, same_day, zones, std_cost, express_cost
    ("AuthorizedDealer", 2, 1, True, "Major Cities", 0.00, 50.00),
    ("AppleStore", 3, 1, True, "All India", 0.00, 40.00),
    ("Samsung Store", 3, 2, False, "All India", 50.00, 100.00),
    ("BestBuy", 4, 2, False, "All India", 75.00, 150.00),
    ("SmartHome", 4, 2, False, "All India", 50.00, 100.00),
    ("Google Store", 3, 2, False, "All India", 50.00, 100.00),
    ("Amazon", 2, 1, True, "All India", 0.00, 50.00),
    ("Walmart", 3, 1, True, "All India", 0.00, 40.00),
    ("Chrono24", 7, 3, False, "Major Cities", 150.00, 300.00),
    ("SiteA", 3, 1, True, "All India", 0.00, 30.00),
    ("SiteB", 5, 2, False, "Major Cities", 30.00, 60.00),
    ("SiteC", 4, 2, False, "All India", 25.00, 50.00)
]

REFUND_POLICIES = [
    # ecommerce_site, window_days, full_condition, partial_condition, non_returnable
    ("AuthorizedDealer", 30, "Unworn with tags", "Store credit only", "Modified or worn items"),
    ("AppleStore", 14, "Unopened items", "Opened but unused", "Damaged items"),
    ("Samsung Store", 14, "Unopened items", "Opened but unused", "Damaged items"),
    ("BestBuy", 30, "Unopened items", "Opened items with all accessories", "Digital items"),
    ("SmartHome", 30, "Unopened items", "Opened but unused", "Installed items"),
    ("Google Store", 15, "Unopened items", "Opened but unused", "Digital content"),
    ("Amazon", 7, "Unopened items", "Opened but unused", "Digital items"),
    ("Walmart", 30, "Unopened items", "Opened items with all accessories", "Digital items"),
    ("Chrono24", 30, "Unworn with tags", "Store credit only", "Modified or worn items"),
    ("SiteA", 30, "Unworn with tags", "Exchange only", "Washed or used items"),
    ("SiteB", 14, "Unworn with tags", "Store credit", "Sale items"),
    ("SiteC", 15, "Unworn with tags", "Partial refund", "Personalized items")
]

PROMO_CODES = {
    # Electronics
    "SAVE10": {"discount": 10, "description": "10% off on select electronics"},
    "MUSIC15": {"discount": 15, "description": "15% off on audio devices"},
    "AUDIO20": {"discount": 20, "description": "20% off on premium headphones"},
    "PODS15": {"discount": 15, "description": "15% off on AirPods"},
    "APPLE10": {"discount": 10, "description": "10% off on Apple products"},
    "SAVE15": {"discount": 15, "description": "15% off on select items"},
    "WATCH10": {"discount": 10, "description": "10% off on smartwatches"},
    "WEARABLE15": {"discount": 15, "description": "15% off on wearable tech"},
    "MAC100": {"discount": 100, "description": "₹100 off on MacBooks"},
    "LAPTOP50": {"discount": 50, "description": "₹50 off on laptops"},
    
    # Smart Home
    "LIGHT20": {"discount": 20, "description": "20% off on smart lighting"},
    "HOME15": {"discount": 15, "description": "15% off on smart home devices"},
    "SMART10": {"discount": 10, "description": "10% off on smart devices"},
    "NEST25": {"discount": 25, "description": "25% off on Nest products"},
    
    # Luxury
    "LUXURY500": {"discount": 10, "description": "10% off on luxury watches"},
    "WATCH250": {"discount": 10, "description": "10% off on premium watches"},
    "TIME200": {"discount": 10, "description": "10% off on select watches"},

    # Clothes
    "SPRING15": {"discount": 15, "description": "15% off on spring collection"},
    "FASHION10": {"discount": 10, "description": "10% off on selected fashion items"},
    "STYLE20": {"discount": 20, "description": "20% off on latest styles"},
    "DENIM25": {"discount": 25, "description": "25% off on denim wear"},
    "DENIM30": {"discount": 30, "description": "30% off on denim wear"},
    "PARTY30": {"discount": 30, "description": "30% off on party wear"},

    # Shoes
    "SPORT10": {"discount": 10, "description": "10% off on sports shoes"},
    "SPORT15": {"discount": 15, "description": "15% off on sports shoes"},
    "SUMMER15": {"discount": 15, "description": "15% off on summer collection"}
}

INDIAN_CITIES = {
    'major_cities': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Jaipur', 'Ahmedabad'],
    'tier_2_cities': ['Lucknow', 'Kanpur', 'Nagpur', 'Indore', 'Thane', 'Bhopal', 'Visakhapatnam', 'Vadodara'],
    'other_cities': ['Agra', 'Varanasi', 'Patna', 'Raipur', 'Ranchi', 'Guwahati']
}