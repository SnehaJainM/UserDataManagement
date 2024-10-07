# User Data Management 👾

## Overview

This project is a simple User Data Management system built using Python and MySQL. It allows users to register, view, update, and delete user information stored in a MySQL database. 
## Features

1. **Register New Users**: Capture and store user details such as first name, last name, phone number, email, and address.
2. **View User Details**: Display all registered users and their information.
3. **View Users by Location**: Filter and display users based on their address.
4. **Update User Details**: Modify existing user information such as phone number, email, or address.
5. **Delete Specific User Details**: Remove a specific user by their phone number.
6. **Delete All Records**: Clear all user data from the database.
7. **Data Validation**: Input validation to ensure data integrity.

## Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

## Setup

1. **Install MySQL**: Make sure you have MySQL installed and running on your machine. Create a database named `user_data`.

2. **Create the `userdetails` Table**: Run the following SQL command in your MySQL client to create the required table:

   ```sql
   CREATE TABLE userdetails (
       id INT AUTO_INCREMENT PRIMARY KEY,
       first_name VARCHAR(100),
       last_name VARCHAR(100),
       phone_number VARCHAR(15),
       email VARCHAR(100),
       address VARCHAR(255)
   );
   ```


3. Follow the on-screen prompts to perform various operations on the user data.

## User Instructions

- **Enter User Details**: When registering a user, ensure that all fields are filled correctly according to the validation rules provided (e.g., valid email format, phone number length).
- **Viewing Users**: You can view all users or filter by location.
- **Updating Details**: Specify which details you want to update and provide the old value to confirm the change.
- **Deleting Users**: Provide the phone number of the user you wish to delete.

Thanks !✨😗
