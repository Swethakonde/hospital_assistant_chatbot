def welcome():
    print("\nWelcome to Hospital Assistant Chatbot")
    print("How can I assist you today?")
    print("1. Book Appointment")
    print("2. Check Report Status")
    print("3. Doctor Availability")
    print("4. Emergency Hospital Locator")
    print("5. Exit")

def book_appointment():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    department = input("Enter the department (e.g., Cardiology, Neurology): ")
    date = input("Enter preferred appointment date (dd-mm-yyyy): ")

    # Simple validation for past date
    from datetime import datetime
    try:
        appointment_date = datetime.strptime(date, "%d-%m-%Y")
        if appointment_date < datetime.now():
            print("Cannot book appointment for a past date.")
        else:
            print(f"Appointment booked successfully for {name} with {department} department on {date}.")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")

def check_report_status():
    report_number = input("Enter your report number: ")
    ready_reports = ["1001", "1002", "1005"]
    in_progress_reports = ["1003", "1004"]

    if report_number in ready_reports:
        print("Your report is ready. Please collect it from the reception.")
    elif report_number in in_progress_reports:
        print("Your report is still in progress. Please check back later.")
    else:
        print("Invalid report number. Please check and try again.")

def doctor_availability():
    doctors = {
        "Dr. Ramesh - Cardiology": "Available (10 AM - 2 PM)",
        "Dr. Vineeth - Neurology": "Available (12 PM - 4 PM)",
        "Dr. Rithu - Orthopedics": "Not Available Today",
        "Dr. Swapna - Pediatrics": "Available (9 AM - 1 PM)"
    }
    for doc, status in doctors.items():
        print(f"{doc}: {status}")

def emergency_hospital_locator():
    hospital_data = {
        "Hyderabad": "Apollo Hospital, Jubilee Hills",
        "Secunderabad": "Yashoda Hospital, Secunderabad",
        "Kukatpally": "KIMS Hospital, Kukatpally",
        "Miyapur": "Pranaam Hospital, Miyapur",
        "Ameerpet": "Aster Prime Hospital, Ameerpet"
    }
    location = input("Enter your location: ").strip().title()
    if location in hospital_data:
        print(f"Nearest emergency hospital in {location}: {hospital_data[location]}")
    else:
        print("Sorry, no hospital found for your location. Please try a nearby area.")

# Main loop
while True:
    welcome()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        book_appointment()
    elif choice == "2":
        check_report_status()
    elif choice == "3":
        doctor_availability()
    elif choice == "4":
        emergency_hospital_locator()
    elif choice == "5":
        print("Thank you for using Hospital Assistant Chatbot. Stay healthy!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

