import random

# Products data
product_ids = list(range(1001, 1204))  # 203 incremental IDs starting at 1001

model_name = [
    # 2024 Releases
    "16 Pro Max", "16 Pro", "16", "16 Plus", "S24 Ultra", "S24 Plus", "S24", "9 Pro", "9", "8a",
    "12", "12R", "14 Pro", "14", "Find X7 Pro", "Find X7", "X100 Pro", "X100", "Z Fold 6", "Z Flip 6",
    "GT 6", "Magic 6 Pro", "ROG Phone 8 Pro", "Razr Plus (2024)", "F6", "Phone (2a)", "Note 13 Pro",
    "Neo 9 Pro", "Z60 Ultra", "A55", "Edge (2024)", "G Power 5G (2024)", "G Stylus 5G (2024)", "G Play (2024)",
    
    # 2023 Releases
    "15 Pro Max", "15 Pro", "15", "15 Plus", "S23 Ultra", "S23 Plus", "S23", "8 Pro", "8", "7a",
    "11", "11R", "13 Pro", "13", "Find N3", "Find X6 Pro", "X90 Pro", "X90", "Z Fold 5", "Z Flip 5",
    "GT 5", "Magic 5 Pro", "ROG Phone 7", "Razr 40 Ultra", "F5", "Phone (2)", "Note 12 Pro", "12",
    "Xperia 1 V", "A54", "Edge+", "Nord 3",
    
    # 2022 Releases
    "14 Pro Max", "14 Pro", "14", "14 Plus", "S22 Ultra", "S22 Plus", "S22", "7 Pro", "7", "6a",
    "10 Pro", "10T", "12S Ultra", "12 Pro", "Find X5 Pro", "Find N2", "X80 Pro", "X80", "Z Fold 4", "Z Flip 4",
    "GT Neo 3", "Magic 4 Pro", "ROG Phone 6", "Edge 30 Ultra", "F4", "Phone (1)", "Note 11 Pro", "9 Pro",
    "Xperia 1 IV", "A53", "Nord 2T", "Edge (2022)",
    
    # 2021 Releases
    "13 Pro Max", "13 Pro", "13", "13 Mini", "S21 Ultra", "S21 Plus", "S21", "6 Pro", "6", "9 Pro",
    "9", "Mi 11 Ultra", "Mi 11", "Find X3 Pro", "Find X3", "X70 Pro", "X60 Pro", "Z Fold 3", "Z Flip 3",
    "GT", "50 Pro", "ROG Phone 5", "Edge 20 Pro", "F3", "Note 10 Pro", "7", "Xperia 1 III", "A52",
    "Nord 2", "Edge S",
    
    # 2020 Releases
    "12 Pro Max", "12 Pro", "12", "12 Mini", "S20 Ultra", "S20 Plus", "S20", "5", "4a", "8 Pro",
    "8", "Mi 10 Pro", "Mi 10", "Find X2 Pro", "Reno 4 Pro", "X50 Pro", "Note 20 Ultra", "Note 20",
    "Z Fold 2", "Z Flip", "X50 Pro", "30 Pro", "ROG Phone 3", "Edge Plus", "F2 Pro", "Note 9 Pro",
    "3", "Xperia 1 II", "A51", "11", "S10", "4", "7T",
    
    # 2019 and Earlier Releases
    "11 Pro Max", "11 Pro", "11", "XS Max", "XS", "XR", "S10 Plus", "S10", "4 XL", "7 Pro",
    "7", "Mi 9", "Find X", "Reno 10x Zoom", "X27 Pro", "Note 10 Plus", "Note 10", "Z Flip (2019)",
    "20 Pro", "20", "ROG Phone 2", "Edge (2019)", "F1", "Note 8 Pro", "K20 Pro", "Xperia 1",
    "A50", "10 Plus", "S9 Plus", "S9", "3 XL", "6T", "Mate 20 Pro", "P20 Pro", "X", "8 Plus",
    "8", "S8 Plus", "S8", "2 XL", "5T", "Mate 10 Pro"
]

brand = [
    # 2024
    "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Samsung", "Google", "Google", "Google",
    "OnePlus", "OnePlus", "Xiaomi", "Xiaomi", "Oppo", "Oppo", "Vivo", "Vivo", "Samsung", "Samsung",
    "Realme", "Honor", "Asus", "Motorola", "Poco", "Nothing", "Redmi", "iQOO", "Nubia", "Samsung",
    "Motorola", "Motorola", "Motorola", "Motorola",
    
    # 2023
    "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Samsung", "Google", "Google", "Google",
    "OnePlus", "OnePlus", "Xiaomi", "Xiaomi", "Oppo", "Oppo", "Vivo", "Vivo", "Samsung", "Samsung",
    "Realme", "Honor", "Asus", "Motorola", "Poco", "Nothing", "Redmi", "iQOO", "Sony", "Samsung",
    "Motorola", "OnePlus",
    
    # 2022
    "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Samsung", "Google", "Google", "Google",
    "OnePlus", "OnePlus", "Xiaomi", "Xiaomi", "Oppo", "Oppo", "Vivo", "Vivo", "Samsung", "Samsung",
    "Realme", "Honor", "Asus", "Motorola", "Poco", "Nothing", "Redmi", "iQOO", "Sony", "Samsung",
    "OnePlus", "Motorola",
    
    # 2021
    "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Samsung", "Google", "Google", "OnePlus",
    "OnePlus", "Xiaomi", "Xiaomi", "Oppo", "Oppo", "Vivo", "Vivo", "Samsung", "Samsung", "Realme",
    "Honor", "Asus", "Motorola", "Poco", "Redmi", "iQOO", "Sony", "Samsung", "OnePlus", "Motorola",
    
    # 2020
    "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Samsung", "Google", "Google", "OnePlus",
    "OnePlus", "Xiaomi", "Xiaomi", "Oppo", "Oppo", "Vivo", "Samsung", "Samsung", "Samsung", "Samsung",
    "Realme", "Honor", "Asus", "Motorola", "Poco", "Redmi", "iQOO", "Sony", "Samsung", "Apple",
    "Samsung", "Google", "OnePlus",
    
    # 2019 and Earlier
    "Apple", "Apple", "Apple", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Google", "OnePlus",
    "OnePlus", "Xiaomi", "Oppo", "Oppo", "Vivo", "Samsung", "Samsung", "Samsung", "Huawei", "Huawei",
    "Asus", "Motorola", "Poco", "Redmi", "Redmi", "Sony", "Samsung", "OnePlus", "Samsung", "Samsung",
    "Google", "OnePlus", "Huawei", "Huawei", "Apple", "Apple", "Apple", "Samsung", "Samsung", "Google",
    "OnePlus", "Huawei"
]

unit_price = [
    # 2024 (Estimated values as of March 5, 2025)
    1200, 1000, 800, 900, 1300, 1000, 800, 1000, 800, 500, 900, 600, 850, 700, 950, 750, 900, 700,
    1800, 1100, 650, 950, 1200, 1000, 450, 400, 350, 550, 800, 400, 550, 300, 400, 150,
    
    # 2023
    900, 750, 600, 700, 950, 750, 600, 750, 600, 400, 650, 500, 700, 550, 1400, 800, 750, 550,
    1400, 850, 500, 800, 900, 800, 350, 500, 300, 600, 1100, 350, 700, 550,
    
    # 2022
    700, 600, 500, 550, 750, 550, 450, 550, 450, 300, 500, 450, 650, 500, 600, 1000, 600, 450,
    1100, 650, 400, 600, 800, 550, 300, 350, 250, 500, 900, 300, 400, 450,
    
    # 2021
    550, 450, 400, 350, 600, 450, 350, 450, 350, 400, 350, 500, 350, 450, 350, 450, 400, 900,
    500, 300, 350, 600, 400, 250, 200, 350, 750, 250, 350, 400,
    
    # 2020
    450, 400, 350, 300, 400, 300, 250, 300, 200, 350, 300, 300, 250, 350, 250, 300, 450, 350,
    700, 400, 250, 300, 450, 350, 200, 150, 250, 600, 200, 300, 200, 250, 250,
    
    # 2019 and Earlier
    400, 350, 300, 350, 300, 250, 250, 200, 200, 300, 250, 200, 300, 250, 200, 350, 300, 350,
    300, 250, 400, 250, 200, 150, 200, 500, 150, 250, 200, 150, 150, 200, 250, 200, 250, 200,
    150, 150, 100, 150, 200, 200
]

release_date = [
    # 2024 (Estimated based on typical launch patterns)
    "15-09-2024", "15-09-2024", "15-09-2024", "15-09-2024", "31-01-2024", "31-01-2024", "31-01-2024",
    "20-10-2024", "20-10-2024", "15-05-2024", "10-01-2024", "25-02-2024", "20-10-2024", "20-10-2024",
    "15-03-2024", "15-03-2024", "10-11-2024", "10-11-2024", "15-07-2024", "15-07-2024", "05-06-2024",
    "20-03-2024", "10-01-2024", "20-06-2024", "15-05-2024", "05-03-2024", "10-10-2024", "15-11-2024",
    "20-12-2024", "15-03-2024", "04-06-2024", "15-03-2024", "30-05-2024", "15-01-2024",
    
    # 2023
    "20-09-2023", "20-09-2023", "20-09-2023", "20-09-2023", "01-02-2023", "01-02-2023", "01-02-2023",
    "15-10-2023", "15-10-2023", "10-05-2023", "15-01-2023", "20-02-2023", "25-10-2023", "25-10-2023",
    "20-10-2023", "15-03-2023", "10-11-2023", "10-11-2023", "20-07-2023", "20-07-2023", "15-06-2023",
    "25-03-2023", "05-01-2023", "15-06-2023", "10-05-2023", "15-07-2023", "05-10-2023", "20-11-2023",
    "15-05-2023", "10-03-2023", "20-06-2023", "05-07-2023",
    
    # 2022
    "15-09-2022", "15-09-2022", "15-09-2022", "15-09-2022", "05-02-2022", "05-02-2022", "05-02-2022",
    "20-10-2022", "20-10-2022", "15-05-2022", "10-01-2022", "20-08-2022", "15-07-2022", "15-07-2022",
    "25-02-2022", "20-12-2022", "25-04-2022", "25-04-2022", "25-07-2022", "25-07-2022", "15-03-2022",
    "20-03-2022", "05-07-2022", "20-09-2022", "15-06-2022", "05-07-2022", "15-10-2022", "20-02-2022",
    "15-05-2022", "10-03-2022", "20-07-2022", "15-08-2022",
    
    # 2021
    "20-09-2021", "20-09-2021", "20-09-2021", "20-09-2021", "25-01-2021", "25-01-2021", "25-01-2021",
    "25-10-2021", "25-10-2021", "25-03-2021", "25-03-2021", "25-02-2021", "25-02-2021", "15-03-2021",
    "15-03-2021", "15-09-2021", "25-03-2021", "25-07-2021", "25-07-2021", "15-03-2021", "15-06-2021",
    "25-03-2021", "25-07-2021", "25-03-2021", "25-03-2021", "25-01-2021", "25-04-2021", "25-03-2021",
    "20-07-2021", "25-01-2021",
    
    # 2020
    "20-10-2020", "20-10-2020", "20-10-2020", "20-10-2020", "25-02-2020", "25-02-2020", "25-02-2020",
    "15-10-2020", "15-08-2020", "20-04-2020", "20-04-2020", "15-02-2020", "15-02-2020", "15-03-2020",
    "15-06-2020", "15-06-2020", "15-08-2020", "15-08-2020", "25-08-2020", "25-02-2020", "15-02-2020",
    "15-04-2020", "15-07-2020", "15-04-2020", "15-05-2020", "15-03-2020", "15-02-2020", "15-02-2020",
    "15-03-2020", "15-09-2020", "25-02-2020", "15-10-2020", "15-10-2020",
    
    # 2019 and Earlier
    "20-09-2019", "20-09-2019", "20-09-2019", "25-09-2018", "25-09-2018", "25-09-2018", "25-02-2019",
    "25-02-2019", "15-10-2019", "15-05-2019", "15-05-2019", "25-02-2019", "25-06-2018", "15-05-2019",
    "15-03-2019", "25-08-2019", "25-08-2019", "25-02-2019", "15-10-2018", "15-10-2018", "15-07-2019",
    "15-03-2019", "15-08-2018", "15-05-2019", "15-05-2019", "25-02-2019", "15-03-2019", "15-02-2019",
    "25-02-2018", "25-02-2018", "15-10-2018", "15-10-2018", "15-10-2018", "15-03-2018", "25-10-2017",
    "25-10-2017", "25-10-2017", "25-03-2017", "25-03-2017", "15-10-2017", "15-10-2017", "15-10-2017"
]

operating_system = [
    # 2024
    "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android",
    
    # 2023
    "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android",
    
    # 2022
    "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android",
    
    # 2021
    "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android",
    
    # 2020
    "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android",
    
    # 2019 and Earlier
    "iOS", "iOS", "iOS", "iOS", "iOS", "iOS", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android", "Android",
    "Android", "Android", "Android", "Android", "Android", "iOS", "iOS", "iOS", "Android", "Android",
    "Android", "Android", "Android"
]

screen_size_inches = [
    # 2024
    6.9, 6.3, 6.1, 6.7, 6.8, 6.7, 6.2, 6.7, 6.3, 6.1, 6.67, 6.55, 6.78, 6.67, 6.8, 6.7, 6.78,
    6.67, 7.6, 6.9, 6.67, 6.78, 6.82, 6.9, 6.55, 6.67, 6.67, 6.67, 6.78, 6.6, 6.6, 6.7, 6.7, 6.5,
    
    # 2023
    6.7, 6.1, 6.1, 6.7, 6.8, 6.7, 6.2, 6.7, 6.3, 6.1, 6.67, 6.55, 6.78, 6.67, 7.6, 6.8, 6.78,
    6.67, 7.6, 6.9, 6.67, 6.78, 6.82, 6.9, 6.55, 6.67, 6.67, 6.67, 6.5, 6.6, 6.8, 6.67,
    
    # 2022
    6.7, 6.1, 6.1, 6.7, 6.8, 6.7, 6.2, 6.7, 6.3, 6.1, 6.67, 6.55, 6.78, 6.67, 6.8, 7.6, 6.78,
    6.67, 7.6, 6.9, 6.67, 6.78, 6.82, 6.8, 6.55, 6.67, 6.67, 6.67, 6.5, 6.6, 6.55, 6.7,
    
    # 2021
    6.7, 6.1, 6.1, 5.4, 6.8, 6.7, 6.2, 6.7, 6.3, 6.67, 6.55, 6.78, 6.67, 6.8, 6.7, 6.78, 6.67,
    7.6, 6.9, 6.67, 6.67, 6.82, 6.7, 6.55, 6.67, 6.67, 6.5, 6.6, 6.55, 6.7,
    
    # 2020
    6.7, 6.1, 6.1, 5.4, 6.8, 6.7, 6.2, 6.1, 6.0, 6.67, 6.55, 6.78, 6.67, 6.8, 6.6, 6.67, 6.8,
    6.7, 7.6, 6.9, 6.67, 6.67, 6.82, 6.7, 6.55, 6.67, 6.67, 6.5, 6.6, 6.1, 6.8, 6.1, 6.55,
    
    # 2019 and Earlier
    6.5, 6.1, 6.1, 6.5, 5.8, 6.1, 6.8, 6.2, 6.4, 6.67, 6.2, 6.67, 6.8, 6.6, 6.67, 6.8, 6.7,
    6.2, 6.7, 6.4, 6.82, 6.5, 6.2, 6.67, 6.67, 6.5, 6.5, 6.4, 6.2, 5.8, 6.2, 6.2, 6.3, 6.0,
    5.8, 5.5, 4.7, 6.2, 5.8, 6.0, 6.2, 6.3
]

display_type = [
    # 2024
    "OLED", "OLED", "OLED", "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "OLED", "OLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "AMOLED", "LCD",
    "P-OLED", "LCD", "P-OLED", "LCD",
    
    # 2023
    "OLED", "OLED", "OLED", "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "OLED", "OLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "OLED", "LCD",
    "OLED", "AMOLED",
    
    # 2022
    "OLED", "OLED", "OLED", "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "OLED", "OLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "OLED", "LCD",
    "AMOLED", "OLED",
    
    # 2021
    "OLED", "OLED", "OLED", "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "OLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "OLED", "LCD", "AMOLED", "AMOLED",
    
    # 2020
    "OLED", "OLED", "OLED", "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "LCD", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "OLED", "LCD", "OLED",
    "AMOLED", "OLED", "AMOLED",
    
    # 2019 and Earlier
    "OLED", "OLED", "OLED", "OLED", "OLED", "LCD", "AMOLED", "AMOLED", "OLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED", "AMOLED",
    "AMOLED", "AMOLED", "AMOLED", "LCD", "AMOLED", "OLED", "LCD", "AMOLED", "AMOLED", "AMOLED",
    "OLED", "AMOLED", "AMOLED", "AMOLED", "OLED", "LCD", "LCD", "AMOLED", "AMOLED", "OLED",
    "AMOLED", "AMOLED"
]

resolution_h = [
    # 2024
    1290, 1179, 1179, 1290, 1440, 1440, 1440, 1344, 1344, 1080, 1080, 1080, 1440, 1080, 1440,
    1080, 1440, 1080, 2208, 1768, 1080, 1440, 1080, 1768, 1080, 1080, 1080, 1080, 1440, 1080,
    1080, 1080, 1080, 1080,
    
    # 2023
    1290, 1179, 1179, 1290, 1440, 1440, 1440, 1344, 1344, 1080, 1080, 1080, 1440, 1080, 2208,
    1440, 1440, 1080, 2208, 1768, 1080, 1440, 1080, 1768, 1080, 1080, 1080, 1080, 1080, 1080,
    1440, 1080,
    
    # 2022
    1290, 1179, 1179, 1290, 1440, 1440, 1440, 1344, 1344, 1080, 1080, 1080, 1440, 1080, 1440,
    2208, 1440, 1080, 2208, 1768, 1080, 1440, 1080, 1440, 1080, 1080, 1080, 1080, 1080, 1080,
    1080, 1080,
    
    # 2021
    1284, 1170, 1170, 828, 1440, 1440, 1440, 1440, 1344, 1080, 1080, 1440, 1080, 1440, 1080,
    1440, 1080, 2208, 1768, 1080, 1080, 1080, 1440, 1080, 1080, 1080, 1080, 1080, 1080, 1080,
    
    # 2020
    1284, 1170, 1170, 828, 1440, 1440, 1440, 1080, 1080, 1080, 1080, 1440, 1080, 1440, 1080,
    1080, 1440, 1440, 2208, 1768, 1080, 1080, 1080, 1440, 1080, 1080, 1080, 1080, 1080, 1170,
    1440, 1080, 1080,
    
    # 2019 and Earlier
    1242, 1125, 828, 1242, 1125, 828, 1440, 1440, 1440, 1080, 1080, 1080, 1440, 1080, 1080,
    1440, 1440, 1080, 1440, 1080, 1080, 1080, 1080, 1080, 1080, 1080, 1080, 1080, 1440, 1440,
    1440, 1080, 1440, 1080, 1125, 1080, 750, 1440, 1440, 1440, 1080, 1440
]

resolution_v = [
    # 2024
    2796, 2556, 2556, 2796, 3088, 3120, 3120, 2992, 2992, 2400, 2400, 2400, 3200, 2400, 3200,
    2400, 3200, 2400, 1768, 3820, 2400, 3200, 2400, 3820, 2400, 2400, 2400, 2400, 3200, 2400,
    2400, 2400, 2400, 2400,
    
    # 2023
    2796, 2556, 2556, 2796, 3088, 3120, 3120, 2992, 2992, 2400, 2400, 2400, 3200, 2400, 1768,
    3200, 3200, 2400, 1768, 3820, 2400, 3200, 2400, 3820, 2400, 2400, 2400, 2400, 2400, 2400,
    3088, 2400,
    
    # 2022
    2796, 2556, 2556, 2796, 3088, 3120, 3120, 2992, 2992, 2400, 2400, 2400, 3200, 2400, 3200,
    1768, 3200, 2400, 1768, 3820, 2400, 3200, 2400, 3120, 2400, 2400, 2400, 2400, 2400, 2400,
    2400, 2400,
    
    # 2021
    2778, 2532, 2532, 1792, 3088, 3120, 3120, 3088, 2778, 2400, 2400, 3200, 2400, 3200, 2400,
    3200, 2400, 1768, 3820, 2400, 2400, 2400, 3120, 2400, 2400, 2400, 2400, 2400, 2400, 2400,
    
    # 2020
    2778, 2532, 2532, 1792, 3200, 3200, 3200, 2400, 2400, 2400, 2400, 3200, 2400, 3200, 2400,
    2400, 3200, 3200, 1768, 3820, 2400, 2400, 2400, 3120, 2400, 2400, 2400, 2400, 2400, 2532,
    3200, 2400, 2400,
    
    # 2019 and Earlier
    2688, 2436, 1792, 2688, 2436, 1792, 3200, 3200, 2960, 2400, 2400, 2400, 3200, 2400, 2400,
    3200, 3200, 2160, 3200, 2400, 2400, 2400, 2400, 2400, 2400, 2400, 2400, 2400, 2960, 2960,
    2960, 2400, 3200, 2160, 2436, 1920, 1334, 2960, 2960, 2960, 2400, 3200
]

processor = [
    # 2024
    "A18 Pro", "A18 Pro", "A18", "A18", "Snapdragon 8 Gen 3", "Snapdragon 8 Gen 3", "Snapdragon 8 Gen 3",
    "Tensor G4", "Tensor G4", "Tensor G3", "Snapdragon 8 Gen 3", "Dimensity 7300", "Dimensity 9300",
    "Dimensity 9300", "Snapdragon 8 Gen 3", "Snapdragon 8 Gen 3", "Dimensity 9300", "Dimensity 9300",
    "Snapdragon 8 Gen 3", "Snapdragon 8 Gen 3", "Dimensity 8300", "Snapdragon 8 Gen 3", "Snapdragon 8 Gen 3",
    "Snapdragon 8 Gen 3", "Dimensity 7200", "Dimensity 7300", "Dimensity 7020", "Dimensity 9200",
    "Snapdragon 8 Gen 3", "Snapdragon 7 Gen 1", "Snapdragon 7s Gen 2", "Dimensity 7020", "Snapdragon 6 Gen 1",
    "Snapdragon 680",
    
    # 2023
    "A17 Pro", "A17 Pro", "A16 Bionic", "A16 Bionic", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2",
    "Snapdragon 8 Gen 2", "Tensor G3", "Tensor G3", "Tensor G2", "Snapdragon 8 Gen 2", "Dimensity 6020",
    "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2",
    "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2",
    "Dimensity 8200", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Dimensity 6020",
    "Dimensity 7300", "Dimensity 6020", "Snapdragon 8 Gen 2", "Snapdragon 8 Gen 2", "Snapdragon 7 Gen 1",
    "Snapdragon 8 Gen 2", "Snapdragon 7+ Gen 2",
    
    # 2022
    "A16 Bionic", "A16 Bionic", "A15 Bionic", "A15 Bionic", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1",
    "Snapdragon 8 Gen 1", "Tensor G2", "Tensor G2", "Tensor G1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1",
    "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1",
    "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1",
    "Dimensity 8100", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Dimensity 6020",
    "Dimensity 7200", "Dimensity 6020", "Snapdragon 8 Gen 1", "Snapdragon 8 Gen 1", "Snapdragon 7 Gen 1",
    "Dimensity 8100", "Snapdragon 8 Gen 1",
    
    # 2021
    "A15 Bionic", "A15 Bionic", "A15 Bionic", "A15 Bionic", "Snapdragon 888", "Snapdragon 888",
    "Snapdragon 888", "Tensor", "Tensor", "Snapdragon 888", "Snapdragon 888", "Snapdragon 888",
    "Snapdragon 888", "Snapdragon 888", "Snapdragon 888", "Snapdragon 888", "Snapdragon 888",
    "Snapdragon 888", "Snapdragon 888", "Dimensity 1200", "Snapdragon 870", "Snapdragon 888",
    "Snapdragon 888", "Dimensity 1200", "Dimensity 6020", "Snapdragon 870", "Snapdragon 888",
    "Snapdragon 7 Gen 1", "Dimensity 8100", "Snapdragon 870",
    
    # 2020
    "A14 Bionic", "A14 Bionic", "A14 Bionic", "A14 Bionic", "Snapdragon 865", "Snapdragon 865",
    "Snapdragon 865", "Snapdragon 865", "Snapdragon 765G", "Snapdragon 865", "Snapdragon 865",
    "Snapdragon 865", "Snapdragon 865", "Snapdragon 865", "Snapdragon 865", "Snapdragon 865",
    "Snapdragon 865", "Snapdragon 865", "Snapdragon 865", "Snapdragon 865", "Dimensity 1000",
    "Snapdragon 865", "Snapdragon 865", "Snapdragon 865", "Dimensity 1000", "Dimensity 6020",
    "Snapdragon 865", "Snapdragon 865", "Snapdragon 7 Gen 1", "A13 Bionic", "Snapdragon 855",
    "Snapdragon 855", "Snapdragon 855",
    
    # 2019 and Earlier
    "A13 Bionic", "A13 Bionic", "A13 Bionic", "A12 Bionic", "A12 Bionic", "A12 Bionic", "Snapdragon 855",
    "Snapdragon 855", "Snapdragon 855", "Snapdragon 855", "Snapdragon 855", "Snapdragon 855",
    "Snapdragon 845", "Snapdragon 845", "Snapdragon 845", "Snapdragon 855", "Snapdragon 855",
    "Snapdragon 855", "Kirin 980", "Kirin 980", "Snapdragon 855", "Snapdragon 845", "Snapdragon 845",
    "Snapdragon 855", "Snapdragon 855", "Snapdragon 855", "Snapdragon 7 Gen 1", "Snapdragon 845",
    "Snapdragon 845", "Snapdragon 845", "Snapdragon 845", "Snapdragon 845", "Kirin 980", "Kirin 970",
    "A11 Bionic", "A11 Bionic", "A11 Bionic", "Snapdragon 835", "Snapdragon 835", "Snapdragon 835",
    "Snapdragon 835", "Kirin 970"
]

ram_gb = [
    # 2024
    8, 8, 8, 8, 12, 12, 8, 12, 8, 8, 12, 8, 12, 8, 12, 8, 12, 8, 12, 12, 8, 12, 12, 8, 8, 8,
    8, 8, 12, 8, 8, 8, 8, 4,
    
    # 2023
    8, 8, 6, 6, 12, 12, 8, 12, 8, 8, 12, 8, 12, 8, 12, 12, 12, 8, 12, 12, 8, 12, 12, 8, 8, 8,
    8, 8, 12, 8, 12, 8,
    
    # 2022
    6, 6, 6, 6, 12, 12, 8, 12, 8, 8, 12, 8, 12, 8, 12, 12, 12, 8, 12, 12, 8, 12, 12, 8, 8, 8,
    8, 8, 12, 8, 8, 8,
    
    # 2021
    6, 6, 4, 4, 12, 12, 8, 12, 8, 12, 8, 12, 8, 12, 8, 12, 8, 12, 12, 8, 8, 12, 8, 8, 8, 8,
    12, 8, 8, 8,
    
    # 2020
    6, 6, 4, 4, 12, 12, 8, 8, 6, 12, 8, 12, 8, 12, 8, 8, 12, 8, 12, 12, 8, 8, 12, 8, 8, 8,
    8, 12, 8, 4, 8, 6, 8,
    
    # 2019 and Earlier
    4, 4, 4, 4, 4, 3, 8, 8, 6, 8, 6, 8, 8, 8, 8, 8, 8, 8, 8, 8, 12, 6, 6, 8, 8, 12, 6, 8,
    6, 6, 4, 6, 8, 6, 3, 3, 2, 4, 4, 4, 6, 8
]

storage = [
    # 2024
    256, 256, 128, 256, 256, 256, 128, 256, 128, 128, 256, 128, 256, 128, 256, 128, 256, 128,
    256, 256, 128, 256, 256, 256, 128, 128, 128, 128, 256, 128, 256, 128, 128, 64,
    
    # 2023
    256, 256, 128, 256, 256, 256, 128, 256, 128, 128, 256, 128, 256, 128, 256, 256, 256, 128,
    256, 256, 128, 256, 256, 256, 128, 128, 128, 128, 256, 128, 256, 128,
    
    # 2022
    256, 256, 128, 256, 256, 256, 128, 256, 128, 128, 256, 128, 256, 128, 256, 256, 256, 128,
    256, 256, 128, 256, 256, 256, 128, 128, 128, 128, 256, 128, 128, 256,
    
    # 2021
    128, 128, 64, 64, 256, 256, 128, 256, 128, 256, 128, 256, 128, 256, 128, 256, 128, 256,
    256, 128, 128, 256, 256, 128, 128, 128, 256, 128, 128, 256,
    
    # 2020
    128, 128, 64, 64, 256, 256, 128, 128, 64, 256, 128, 256, 128, 256, 128, 128, 256, 128,
    256, 256, 128, 128, 256, 256, 128, 128, 128, 256, 128, 64, 128, 64, 128,
    
    # 2019 and Earlier
    64, 64, 64, 64, 64, 64, 128, 64, 64, 128, 64, 64, 128, 128, 128, 256, 128, 128, 128, 64,
    256, 128, 64, 128, 128, 256, 64, 128, 64, 64, 64, 64, 128, 64, 64, 64, 32, 64, 64, 64,
    64, 128
]

battery_capacity_mah = [
    # 2024
    4400, 4300, 4200, 4300, 5000, 4900, 4400, 4700, 4500, 4400, 5000, 4500, 5000, 4500, 5000,
    4500, 5000, 4500, 4400, 4000, 5000, 5000, 5000, 4000, 5000, 4260, 5000, 5000, 5000, 5000,
    5000, 5000, 5000, 5000,
    
    # 2023
    4360, 4260, 4160, 4260, 5000, 4850, 4400, 4600, 4400, 4300, 5000, 4500, 5000, 4500, 4400,
    5000, 5000, 4500, 4400, 4000, 5000, 5000, 5000, 4000, 5000, 4260, 5000, 5000, 5000, 5000,
    5000, 5000,
    
    # 2022
    4320, 4220, 4120, 4220, 5000, 4850, 4350, 4500, 4400, 4300, 5000, 4500, 5000, 4500, 5000,
    4400, 5000, 4500, 4400, 4000, 5000, 5000, 5000, 5000, 5000, 4260, 5000, 5000, 5000, 5000,
    5000, 5000,
    
    # 2021
    4350, 4250, 4150, 3095, 5000, 4850, 4350, 4600, 4400, 5000, 4500, 5000, 4500, 5000, 4500,
    5000, 4500, 4400, 4000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000,
    
    # 2020
    3687, 3687, 2775, 2775, 5000, 4850, 4350, 4000, 4000, 5000, 4500, 5000, 4500, 5000, 4500,
    4500, 5000, 4500, 4400, 4000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 3279,
    4000, 3140, 4000,
    
    # 2019 and Earlier
    3969, 3174, 3110, 3630, 2942, 2716, 4000, 3400, 4000, 4000, 3400, 4000, 3500, 4000, 4000,
    4000, 3400, 3400, 4200, 3400, 5000, 4000, 3400, 4000, 4000, 4000, 4000, 4000, 3000, 3000,
    3000, 3400, 3400, 3000, 2691, 2438, 1821, 3000, 3000, 3000, 3400, 3400
]

rear_camera_mp_1 = [
    # 2024
    48, 48, 48, 48, 200, 200, 200, 50, 50, 50, 50, 50, 108, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    
    # 2023
    48, 48, 48, 48, 200, 200, 200, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    
    # 2022
    48, 48, 48, 48, 108, 108, 108, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    50, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    
    # 2021
    12, 12, 12, 12, 108, 108, 108, 50, 50, 48, 48, 108, 48, 50, 50, 50, 50, 50, 50, 50, 50, 50,
    50, 48, 48, 48, 48, 48, 48, 48,
    
    # 2020
    12, 12, 12, 12, 108, 108, 108, 64, 12, 48, 48, 108, 48, 48, 48, 48, 108, 108, 48, 48, 48,
    48, 48, 48, 48, 48, 48, 48, 48, 12, 108, 12, 48,
    
    # 2019 and Earlier
    12, 12, 12, 12, 12, 12, 48, 48, 12, 48, 48, 48, 48, 48, 48, 64, 48, 12, 48, 48, 48, 48,
    48, 48, 48, 48, 48, 48, 12, 12, 12, 48, 40, 40, 12, 12, 12, 12, 12, 12, 48, 40
]

rear_camera_mp_2 = [
    # 2024
    12, 12, 12, 12, 50, 50, 50, 48, 48, 13, 50, 13, 50, 50, 50, 50, 50, 50, 12, 12, 13, 50, 8,
    12, 13, 8, 2, 13, 8, 8, 13, 8, 13, 2,
    
    # 2023
    12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 50, 13, 50, 50, 12, 50, 50, 50, 12, 12, 13, 50, 8,
    12, 13, 8, 2, 13, 12, 8, 13, 13,
    
    # 2022
    12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 50, 13, 50, 50, 50, 12, 50, 50, 12, 12, 13, 50, 8,
    12, 13, 8, 2, 13, 12, 8, 13, 13,
    
    # 2021
    12, 12, 12, 12, 10, 10, 10, 12, 12, 12, 12, 50, 13, 50, 50, 50, 50, 12, 12, 13, 13, 8, 12,
    13, 2, 13, 12, 8, 13, 13,
    
    # 2020
    12, 12, 12, 12, 10, 10, 10, 12, 5, 12, 12, 13, 13, 13, 13, 13, 10, 10, 12, 12, 13, 13, 8,
    12, 13, 2, 13, 12, 8, 12, 12, 12, 12,
    
    # 2019 and Earlier
    12, 12, None, 12, 12, None, 12, 12, 12, 12, 12, 12, 13, 13, 13, 12, 12, 12, 13, 13, 8, 12,
    12, 2, 13, 12, 8, 12, 12, 12, 12, 12, 13, 5, None, None, None, 12, 12, 12, 12, 13
]

rear_camera_mp_3 = [
    # 2024
    12, 12, None, None, 10, 10, None, 12, None, None, 12, None, 12, None, 12, None, 12, None,
    12, None, None, 12, None, None, None, None, None, None, None, None, None, None, None, None,
    
    # 2023
    12, 12, None, None, 10, 10, None, 12, None, None, 12, None, 12, None, 12, 12, 12, None,
    12, None, None, 12, None, None, None, None, None, None, None, None, None, None,
    
    # 2022
    None, None, None, None, 10, 10, None, None, None, None, 12, None, 12, None, 12, 12, 12,
    None, 12, None, None, 12, None, None, None, None, None, None, None, None, None, None,
    
    # 2021
    None, None, None, None, 12, 12, None, None, None, 12, None, 12, None, 12, None, 12, None,
    12, None, None, None, None, None, None, None, None, None, None, None, None,
    
    # 2020
    None, None, None, None, 12, 12, None, None, None, 12, None, 12, None, 12, None, 12, 12,
    None, 12, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    
    # 2019 and Earlier
    None, None, None, None, None, None, None, None, None, None, None, None, 12, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None
]

rear_camera_mp_4 = [
    # 2024
    None, None, None, None, 10, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None,
    
    # 2023
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None,
    
    # 2022
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None,
    
    # 2021
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    
    # 2020
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None,
    
    # 2019 and Earlier
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    None, None, None, None, None, None, None, None, None, None, None, None
]

front_camera_mp = [
    # 2024
    12, 12, 12, 12, 12, 12, 12, 10.8, 10.8, 10.8, 32, 16, 32, 16, 32, 16, 32, 16, 10, 10, 16,
    32, 16, 10, 16, 16, 8, 16, 32, 8, 32, 16, 16, 16,
    
    # 2023
    12, 12, 12, 12, 12, 12, 12, 10.8, 10.8, 10.8, 32, 16, 32, 16, 10, 32, 32, 16, 10, 10, 16,
    32, 16, 10, 16, 16, 8, 16, 12, 8, 32, 32,
    
    # 2022
    12, 12, 12, 12, 12, 12, 12, 10.8, 10.8, 10.8, 32, 16, 32, 16, 32, 10, 32, 16, 10, 10, 16,
    32, 16, 32, 16, 16, 8, 16, 12, 8, 16, 32,
    
    # 2021
    12, 12, 12, 12, 12, 12, 12, 10.8, 10.8, 16, 16, 32, 16, 32, 16, 32, 16, 10, 10, 16, 16,
    16, 32, 16, 8, 16, 12, 8, 16, 32,
    
    # 2020
    12, 12, 12, 12, 12, 12, 12, 10.8, 8, 16, 16, 32, 16, 32, 16, 16, 12, 12, 10, 10, 16, 16,
    16, 32, 16, 8, 16, 12, 8, 12, 12, 8, 16,
    
    # 2019 and Earlier
    12, 12, 12, 12, 12, 7, 12, 12, 8, 16, 16, 16, 32, 16, 16, 12, 12, 10, 16, 16, 16, 16,
    8, 8, 16, 12, 8, 16, 8, 8, 8, 16, 16, 8, 7, 7, 7, 8, 8, 8, 16, 16
]

five_g_support = [
    # 2024
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No",
    
    # 2023
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    
    # 2022
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    
    # 2021
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes",
    
    # 2020
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "No", "No", "No", "No",
    
    # 2019 and Earlier
    "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No",
    "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No",
    "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No", "No"
]

weight_g = [
    # 2024
    227, 199, 172, 215, 233, 213, 187, 221, 199, 167, 205, 188, 208, 190, 215, 195, 210, 190, 239, 
    187, 185, 205, 240, 199, 175, 170, 180, 185, 210, 180, 195, 185, 190, 165,
    
    # 2023
    221, 187, 174, 206, 232, 213, 188, 205, 187, 169, 200, 185, 205, 189, 239, 210, 205, 189, 238,
    187, 183, 200, 239, 195, 172, 168, 179, 183, 210, 179, 205, 189,
    
    # 2022
    240, 206, 174, 221, 228, 212, 187, 203, 184, 163, 197, 183, 205, 188, 210, 238, 203, 187, 237,
    186, 180, 198, 238, 200, 170, 165, 177, 180, 205, 177, 183, 190,
    
    # 2021
    204, 174, 172, 144, 229, 213, 188, 207, 187, 195, 180, 205, 188, 209, 189, 203, 187, 236, 185,
    178, 183, 237, 198, 168, 175, 178, 203, 175, 180, 195,
    
    # 2020
    203, 174, 162, 143, 226, 212, 188, 168, 151, 193, 179, 203, 187, 207, 185, 198, 225, 208, 235,
    183, 175, 180, 235, 195, 165, 173, 175, 200, 173, 172, 211, 162, 178,
    
    # 2019 and Earlier
    206, 179, 162, 208, 175, 158, 208, 184, 173, 189, 172, 190, 206, 184, 195, 221, 205, 171, 205,
    188, 233, 190, 160, 171, 173, 198, 171, 184, 174, 158, 166, 175, 199, 185, 194, 177, 143, 172,
    148, 162, 171, 197
]

wireless_charge = [
    # 2024
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes",
    "Yes", "No", "Yes", "No", "Yes", "No",
    
    # 2023
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes",
    "Yes", "No", "Yes", "Yes",
    
    # 2022
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes",
    "Yes", "No", "Yes", "Yes",
    
    # 2021
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes", "No",
    "Yes", "Yes",
    
    # 2020
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No", "Yes", "Yes",
    "No", "Yes", "Yes", "No", "Yes",
    
    # 2019 and Earlier
    "Yes", "Yes", "Yes", "Yes", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "No", "Yes",
    "Yes", "Yes", "Yes", "Yes", "Yes", "Yes", "No", "No", "No", "Yes", "Yes", "Yes", "Yes", "Yes"
]

water_resistance = [
    # 2024
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    None, "IP54", None, "IP68", "IP68", "IP53", "IP68", None, "IP68", None,
    
    # 2023
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    None, "IP54", None, "IP68", "IP68", "IP53", "IP68", "IP68",
    
    # 2022
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    None, "IP54", None, "IP68", "IP68", "IP53", "IP68", "IP68",
    
    # 2021
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", None,
    None, "IP68", "IP68", "IP53", "IP68", "IP68",
    
    # 2020
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    None, None, "IP68", "IP68", "IP53", "IP68", "IP68", "IP68", "IP68",
    
    # 2019 and Earlier
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68",
    "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", None, None,
    None, "IP68", "IP53", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP68", "IP67", "IP67",
    "IP67", "IP68", "IP68", "IP68", "IP68", "IP68"
]

# Products Dictionary
products = {
    "id": product_ids,
    "model_name": model_name,
    "brand": brand,
    "unit_price": unit_price,
    "release_date": release_date,
    "operating_system": operating_system,
    "screen_size_inches": screen_size_inches,
    "display_type": display_type,
    "resolution_h": resolution_h,
    "resolution_v": resolution_v,
    "processor": processor,
    "ram_gb": ram_gb,
    "storage": storage,
    "battery_capacity_mah": battery_capacity_mah,
    "rear_camera_mp_1": rear_camera_mp_1,
    "rear_camera_mp_2": rear_camera_mp_2,
    "rear_camera_mp_3": rear_camera_mp_3,
    "rear_camera_mp_4": rear_camera_mp_4,
    "front_camera_mp": front_camera_mp,
    "five_g_support": five_g_support,
    "weight_g": weight_g,
    "wireless_charge": wireless_charge,
    "water_resistance": water_resistance
}

# Regions Data
region_ids = list(range(1001, 1045))  # 44 unique IDs starting at 301

country = [
    "Japan", "United States", "Germany", "Brazil", "India", "China", "South Korea", "Nigeria",
    "United Kingdom", "France", "Canada", "Australia", "Russia", "Mexico", "South Africa", "Indonesia",
    "Italy", "Spain", "Thailand", "Egypt", "Argentina", "Turkey", "Saudi Arabia", "Pakistan",
    "Vietnam", "Philippines", "Malaysia", "Singapore", "Netherlands", "Sweden", "Norway", "Switzerland",
    "Poland", "Ukraine", "Colombia", "Chile", "Peru", "Bangladesh", "Kenya", "Ghana", "Morocco",
    "Algeria", "New Zealand", "Ireland"
]

continent = [
    "Asia", "North America", "Europe", "South America", "Asia", "Asia", "Asia", "Africa",
    "Europe", "Europe", "North America", "Oceania", "Europe", "North America", "Africa", "Asia",
    "Europe", "Europe", "Asia", "Africa", "South America", "Asia", "Asia", "Asia",
    "Asia", "Asia", "Asia", "Asia", "Europe", "Europe", "Europe", "Europe",
    "Europe", "Europe", "South America", "South America", "South America", "Asia", "Africa", "Africa",
    "Africa", "Africa", "Oceania", "Europe"
]

population_m = [
    125.80, 345.00, 83.20, 203.00, 1425.00, 1410.00, 51.30, 223.00, 67.40, 65.00, 38.50, 26.00,
    144.00, 126.00, 60.00, 279.00, 58.50, 47.00, 71.00, 105.00, 45.00, 85.00, 36.00, 241.00,
    98.00, 115.00, 33.00, 5.80, 17.50, 10.40, 5.40, 8.70, 38.00, 44.00, 51.00, 19.00,
    34.00, 171.00, 54.00, 31.00, 37.00, 44.00, 5.00, 5.00
]

gdp_per_capita = [
    48000, 82000, 54000, 11000, 3000, 14000, 51000, 2000, 46000, 49000, 58000, 64000,
    12000, 11000, 7000, 2500, 37000, 42000, 7500, 4000, 9000, 10500, 28000, 1800,
    4500, 3400, 13000, 78000, 52000, 59000, 82000, 67000, 14000, 4500, 8000, 17000,
    6500, 1500, 3000, 3500, 4500, 3500, 54000, 62000
]

tech_adoption_rate = [
    0.85, 0.90, 0.88, 0.70, 0.45, 0.80, 0.92, 0.40, 0.87, 0.86, 0.89, 0.91, 0.65, 0.68,
    0.60, 0.55, 0.83, 0.84, 0.67, 0.50, 0.66, 0.62, 0.75, 0.38, 0.60, 0.58, 0.72, 0.95,
    0.89, 0.90, 0.92, 0.91, 0.70, 0.45, 0.65, 0.73, 0.55, 0.42, 0.48, 0.52, 0.57, 0.47,
    0.88, 0.90
]

# Regions Dictionary
regions = {
    "id": region_ids,
    "country": country,
    "continent": continent,
    "population_m": population_m,
    "gdp_per_capita": gdp_per_capita,
    "tech_adoption_rate": tech_adoption_rate
}

# Channels Data
channel_ids = [random.randint(200000, 799999) for _ in range(15)]

channel_type = [
    "Online Store", "Retail Store", "Carrier", "Online Store", "Retail Store",
    "Carrier", "Direct Sales", "Online Store", "Retail Store", "Carrier",
    "Online Store", "Retail Store", "Direct Sales", "Online Store", "Carrier"
]

partner_name = [
    "Amazon", "Best Buy", "Verizon", "eBay", "Walmart",
    "AT&T", "Apple Store", "Newegg", "Target", "T-Mobile",
    "AliExpress", "Costco", "Samsung Store", "B&H Photo", "Sprint"
]

cost_per_sale = [
    50.00, 75.00, 90.00, 45.00, 70.00, 85.00, 40.00, 55.00, 65.00, 95.00,
    48.00, 60.00, 35.00, 52.00, 88.00
]

# Channels Dictionary
channels = {
    "id": channel_ids,
    "channel_type": channel_type,
    "partner_name": partner_name,
    "cost_per_sale": cost_per_sale
}
