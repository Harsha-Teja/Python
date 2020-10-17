# The package can be installed as "pip install mysql-connector-python"
# Importing the module: mysql connector. Helps in connecting to the server
import mysql.connector

# Establishing an connection to the server with login credentials
con = mysql.connector.connect(
    host="############",
    user="#######",
    password="##########",
    database="########",
    port="#########",
)

# To test on the connection status
# print("The connection has been established")

# We have to initialize a cursor point before executing the statements
cur = con.cursor()

# We enter the queries here.
cur.execute(
    " SELECT users.fullname, events.event_title, events.event_date_time, users.email, events.created_at, events.event_location, event_attendies.created_at \
	            FROM ######.users \
	                INNER JOIN \
	                    #######.event_attendies \
	                    ON users.id = event_attendies.attendeventable_id \
	                INNER JOIN \
	                    #######.events \
                        ON event_attendies.event_id = events.id;"
)

# To fetch the results from the query
rows = cur.fetchall()

# Printing the fetched results
for r in rows:
    print(
        f""" The fullname is {r[0]}
               the event title is {r[1]}
               the event date is {r[2]}
               the user email is {r[3]}
               event created on {r[4]}
               event location is {r[5]}
               user clickedat {r[6]}
               ########################
          """
    )

# We have to close the established connection to mysql server.
con.close()
