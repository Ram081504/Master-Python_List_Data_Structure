Employee_name_list = ["Kisseraskley Endonela", "Mat Gabriel Sevella", "John Denson Inao", "Christian Toribio", "Ram Louise Capilitan"]
Employee_job_list = ["Web Designer", "SQL Developer", "Web Developer", "Software Engineer", "IT Professional"]
Employee_number_list = ["00015019", "00015150", "00015456", "00015605", "00015607"]
Employee_age_list = [20, 19, 21, 20, 20]
Employee_email_list = ["Endonela@gmail.com", "Sevella@gmail.com", "Inao@gmail.com", "Toribio@gmail.com", "Capilitan@gmail.com"]

print("Employees Data:")
for i in range(len(Employee_name_list)):
    print(f"Number: {Employee_number_list[i]}, Name: {Employee_name_list[i]}, Job Title: {Employee_job_list[i]}, Age: {Employee_age_list[i]}, Email: {Employee_email_list[i]}")