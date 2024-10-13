University_list = ["University of the Philippines Diliman", "Ateneo de Manila University", "Philippine Normal University", "De La Salle University Manila", "Polytechnic University of the Philippines"]
University_president_list = ["Angelo Jimenez", "Roberto Yap", "Bert J. Tuga", "Br. Bernard S. Oca FSC", "Manuel Muhi"]
University_location_list = ["Quezon City", "Quezon City", "Manila", "Manila", "Manila"]
University_status_list = ["Public", "Private", "Public", "Private", "Public"]
University_date_list = [1908, 1859, 1901, 1911, 1904]

print("University Data:")
for i in range(len(University_list)):
    print(f"University: {University_list[i]}, President: {University_president_list[i]}, Location: {University_location_list[i]}, Status: {University_status_list[i]}, Founded: {University_date_list[i]}")