import sqlite3

def setup_database():
    conn = sqlite3.connect('charity.db')
    cursor = conn.cursor()

    # Create Donors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Donors (
                        DonorID INTEGER PRIMARY KEY,
                        FirstName TEXT,
                        Surname TEXT,
                        BusinessName TEXT,
                        Postcode TEXT,
                        HouseNumber TEXT,
                        PhoneNumber TEXT,
                        DonorType TEXT
                      )''')

    # Create Events table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Events (
                        EventID INTEGER PRIMARY KEY,
                        EventName TEXT,
                        RoomInfo TEXT,
                        BookingDateTime TEXT,
                        Cost REAL
                      )''')

    # Create Donations table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Donations (
                        DonationID INTEGER PRIMARY KEY,
                        Amount REAL,
                        Date TEXT,
                        GiftAid BOOLEAN,
                        Notes TEXT,
                        SourceType TEXT,
                        SourceID INTEGER
                      )''')

    # Create Volunteers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Volunteers (
                        VolunteerID INTEGER PRIMARY KEY,
                        FirstName TEXT,
                        Surname TEXT,
                        PhoneNumber TEXT,
                        AssignedEventID INTEGER,
                        FOREIGN KEY (AssignedEventID) REFERENCES Events(EventID)
                      )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()