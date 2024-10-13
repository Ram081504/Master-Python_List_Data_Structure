Laptop_products_list = ["Microsoft Surface Laptop", "Lenovo IdeaPad Duet 5 OLED Chromebook", "Apple MacBook Air 13-inch M3", "Dell XPS 13 2024", "Acer Aspire 5"]
Laptop_processors_list = ["Qualcomm Snapdragon X Elite", " Qualcomm Snapdragon 7c Gen2", "Apple M3", "Qualcomm Snapdragon X Elite", " Intel Core i5"]
Laptop_screensize_list = ["14-inch / 15-inch", "13.3-inch", "13.6-inch", "13.4-inch", "14-inch"]
Laptop_ram_list = [64, 8, 24, 16, 8]
Laptop_storage_list = ["1TB", "128GB", "2TB", "512GB", "512GB"]

print("Laptop Data:")
for i in range(len(Laptop_products_list)):
    print(f"Product: {Laptop_products_list[i]} Processors: {Laptop_processors_list[i]}, Screen size: {Laptop_screensize_list[i]}, Ram: {Laptop_ram_list[i]}, Storage: {Laptop_storage_list[i]}")
