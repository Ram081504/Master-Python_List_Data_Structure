Restaurant_name_list = ["Sarsa Kitchen + Bar", "Provenciano", "Pamana Restaurant", "Barbara Heritage Restaurant", "Café Adriatico"]
Restaurant_phone_list = ["0915 721 4190", "0915 721 4190", "046 413 2461", "02 8527 4083", "0917 808 5184"]
Restaurant_ratings_list = [4.4, 4.6, 4.5, 4.4, 4.5]
Restaurant_location_list = ["Makati", "Quezon", "Tagaytay", "Intramuros", "Malate"]
Restaurant_hours_list = ["11 AM to 10 PM", "10:30 AM to 9 PM", "9 AM to 10 PM", "9 AM to 9 PM", "7 AM to 12 AM"]

print("Restaurant Data:")
for i in range(len(Restaurant_name_list)):
    print(f"Ratings: {Restaurant_ratings_list[i]}, Name: {Restaurant_name_list[i]}, Phone: {Restaurant_phone_list[i]}, Location: {Restaurant_location_list[i]}, Open Hours: {Restaurant_hours_list[i]}")