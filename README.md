# Smart-Community-System
Basic Internet of Things project to collect data regarding the number of people present in a community hall.

# Requirements
- Account in Carriots
- WAMP Server
- Android Studio
- Python 3

# android
Consists the *Android* code to display the current number of people in the hall, along with details of how have entered and left the hall.
It also has an option to check the history of entries and exits on your local machine (using *Apache WAMP Server*).

# python
1. **data_publish.py** - Run on the Raspberry Pi, which is connected to two IR Sensors (can also be PIR sensors), to continuously transmit data to Carriots.

2. **db_mysql.py** - Runs on the local machine (or any cloud service) and collects data present in Carriots and stores it in MySQL database.

# php
**community_db.php** - It is used to display the data collected in the database on Apache WAMP Server.
