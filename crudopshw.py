import mysql.connector
import creds
from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#creating a connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)

"""
#create a new entry and add it to the table
query = "INSERT INTO users (firstname, lastname) VALUES ('Thomas','Edison')"
#execute_query(conn, query)

#select all users
select_users = "SELECT * FROM users"
users = execute_read_query(conn, select_users)

for user in users:
    print(user["firstname"] + " has the last name: " + user["lastname"])
"""

# Adding the table for vaults
create_vault_table = """
CREATE TABLE IF NOT EXISTS vaults(
id INT AUTO_INCREMENT,
number INT,
code INT,
content VARCHAR(255) NOT NULL,
owner VARCHAR(30) NOT NULL,
PRIMARY KEY (id)
)"""

execute_query(conn, create_vault_table)

