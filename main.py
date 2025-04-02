import sqlite3
import database_setup  # Import the setup script

# Run setup (optional, only if database isn't created yet)
database_setup.setup_database()

import sqlite3
from datetime import datetime

def add_donor():
    conn = sqlite3.connect('charity.db')
    cursor = conn.cursor()

    first_name = input("Enter donor's first name: ")
    surname = input("Enter donor's surname: ")
    business_name = input("Enter business name (if applicable): ")
    postcode = input("Enter postcode: ")
    house_number = input("Enter house number: ")
    phone_number = input("Enter phone number: ")
    donor_type = input("Enter donor type (Individual or Business): ")

    cursor.execute('''INSERT INTO Donors (FirstName, Surname, BusinessName, Postcode, HouseNumber, PhoneNumber, DonorType)
                      VALUES ()''',
                   (first_name, surname, business_name, postcode, house_number, phone_number, donor_type))

    conn.commit()
    print("Donor added successfully!")
    conn.close()

def search_donations():
    conn = sqlite3.connect('charity.db')
    cursor = conn.cursor()

    search_type = input("Search by (Donor or Event): ").lower()

    if search_type == "donor":
        donor_id = input("Enter DonorID: ")
        cursor.execute('''SELECT * FROM Donations WHERE SourceType = "Donor" AND SourceID = ''', (donor_id,))
    elif search_type == "event":
        event_id = input("Enter EventID: ")
        cursor.execute('''SELECT * FROM Donations WHERE SourceType = "Event" AND SourceID = ''', (event_id,))
    else:
        print("Invalid search type.")
        conn.close()
        return

    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No donations found for the given criteria.")

    conn.close()

def main_menu():
    while True:
        print("\n--- Charity Database Menu ---")
        print("1. Add Donor")
        print("2. Search Donations")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == "1":
            add_donor()
        elif choice == "2":
            search_donations()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()