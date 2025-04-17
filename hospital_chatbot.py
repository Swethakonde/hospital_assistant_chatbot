# hospital_chatbot.py
def show_menu():
    print("\n🩺 Welcome to SmartCare Hospital Assistant")
    print("1. Book Appointment")
    print("2. Check Report Status")
    print("3. Emergency Help")
    print("4. Exit")

def book_appointment():
    departments = {
        "Cardiology": ["Dr. Ravi", "Dr. Sandeep"],
        "Nephrology": ["Dr. Vineeth Sharma", "Dr. Anika"],
        "General": ["Dr. Vishnu", "Dr. Eesha"]
    }

    dept = input("Enter department (Cardiology/Nephrology/General): ").title()
    if dept not in departments:
        print("❌ Invalid department.")
        return

    print(f"Available doctors in {dept}: {', '.join(departments[dept])}")
    doctor = input("Choose doctor: ").strip()
    if doctor not in departments[dept]:
        print("❌ Invalid doctor.")
        return

    slot = input("Choose time (10 AM / 11:30 AM / 2 PM / 4 PM): ")
    if slot not in ["10 AM", "11:30 AM", "2 PM", "4 PM"]:
        print("❌ Invalid time slot.")
        return

    print(f"✅ Appointment booked with {doctor} at {slot} in {dept} department.")

def check_report_status():
    reports = {
        "P111": "Ready",
        "P222": "In Progress",
        "P333": "Not Found"
    }

    pid = input("Enter your Patient ID (e.g., P111): ").upper()
    status = reports.get(pid, "❌ Invalid Patient ID")
    print(f"📄 Report Status: {status}")

def emergency_help():
    emergency_map = {
        "Ameerpet": "Rainbow Hospital, Ameerpet",
        "Kukatpally": "Apollo Clinic, Kukatpally",
        "Madhapur": "Care Hospital, Madhapur",
        "Begumpet": "Yashoda Hospital, Begumpet",
        "Secunderabad": "KIMS Hospital, Secunderabad"
    }

    area = input("\nEnter your area (e.g., Madhapur): ").title().strip()
    hospital = emergency_map.get(area)
    if hospital:
        print(f"\n🚨 Nearest Emergency Hospital: {hospital}")
    else:
        print("\n❌ Sorry, no emergency hospital found for your area.")

def main():
    while True:
        show_menu()
        choice = input("Enter choice (1-4): ")
        if choice == '1':
            book_appointment()
        elif choice == '2':
            check_report_status()
        elif choice == '3':
            emergency_help()
        elif choice == '4':
            print("👋 Thank you for using SmartCare. Stay healthy!")
            break
        else:
            print("❗ Invalid choice.")
main()




