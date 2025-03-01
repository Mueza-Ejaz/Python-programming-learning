
# Task: Employee Records Management
# Ek dictionary-based program likho jo employees ka data store kare.

# ✅ Requirements:
# - Add Employee – Naya employee dictionary me add karo.
# - Update Salary – Kisi employee ki salary update karo.
# - Remove Employee – Employee ko dictionary se delete karo.
# - Check Employee – Dekho ke employee mojood hai ya nahi.
# - Display All Employees – Sare employees aur unki salary show karo.

employees = {

    "Asma": 50000,
    "Laiba": 40000,
    "Yasir": 60000,
    "Moiz": 45000,
    
}

# Add new employee:

add_employee = {"Zahir":75000}
employees.update(add_employee)
print(employees)   # {'Asma': 50000, 'Laiba': 40000, 'Yasir': 60000, 'Moiz': 45000, 'Zahir': 75000}

# Update Salary:

employees["Moiz"] = 40000
print(employees) # {'Asma': 50000, 'Laiba': 40000, 'Yasir': 60000, 'Moiz': 40000, 'Zahir': 75000}

# Remove Employee:
employees.pop("Yasir")
print(employees) # {'Asma': 50000, 'Laiba': 40000, 'Moiz': 40000, 'Zahir': 75000}


# Check Employee:

if "Laiba" in employees: 
    print("Key Exist")
else:
    print("Key not Exist")

# Display All Employees:
print(employees)  # # {'Asma': 50000, 'Laiba': 40000, 'Moiz': 40000, 'Zahir': 75000} 
