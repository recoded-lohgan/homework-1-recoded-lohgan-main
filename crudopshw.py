import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

# Creating a connection to MySQL database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
cursor = conn.cursor()

# Adding the table for vaults
create_vault_table = """
CREATE TABLE IF NOT EXISTS vaults (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number INT UNIQUE NOT NULL,
    code VARCHAR(10) NOT NULL,
    content VARCHAR(255) NOT NULL,
    owner VARCHAR(30) NOT NULL
);
"""
execute_query(conn, create_vault_table)

# Insert initial test vaults (remove `id` since it is auto-generated)
add_items_query = "INSERT INTO vaults (number, code, content, owner) VALUES ('100', '12345', 'This is secret content from vault 1', 'Al Capone')"
add_other_item_query = "INSERT INTO vaults (number, code, content, owner) VALUES ('200', '98765', 'This is secret content from vault 2', 'Cleopatra')"

# Uncomment these lines if you need to re-run data insertion
# execute_query(conn, add_items_query)
# execute_query(conn, add_other_item_query)

# Function to display vault numbers on startup
def show_vault_numbers():
    cursor.execute("SELECT number FROM vaults")
    vaults = cursor.fetchall()
    print("\nCurrent vault numbers:")
    for vault in vaults:
        print(f"- Vault {vault[0]}")
    print()

# Function to create a new vault entry
def create_vault():
    number = input("Enter vault number: ")
    code = input("Enter vault code: ")
    content = input("Enter vault content: ")
    owner = input("Enter vault owner: ")

    try:
        cursor.execute(
            "INSERT INTO vaults (number, code, content, owner) VALUES (%s, %s, %s, %s)",
            (number, code, content, owner)
        )
        conn.commit()
        print("Vault entry created successfully!\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}\n")

# Function to retrieve a vault entry
def retrieve_vault():
    number = input("Enter the vault number to retrieve: ")
    code = input("Enter the vault code: ")

    cursor.execute("SELECT content, owner FROM vaults WHERE number = %s AND code = %s", (number, code))
    result = cursor.fetchone()

    if result:
        print(f"\nVault Content: {result[0]}\nVault Owner: {result[1]}\n")
    else:
        print("Invalid vault number or code.\n")

# Main function
def main():
    while True:
        print("Welcome to the Bank Vault Management System.")
        show_vault_numbers()
        print("1. Create a new vault entry")
        print("2. Retrieve vault information")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_vault()
        elif choice == "2":
            retrieve_vault()
        elif choice == "3":
            print("Closing program. Have a nice day.")
            break
        else:
            print("Invalid option! Please try again.\n")

if __name__ == "__main__":
    main()
