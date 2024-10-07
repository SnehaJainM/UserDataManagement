#----------------IMPORTS---------------------

import mysql.connector
import re
#-----------------CONNECTING --------------------

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="user_data"
 
    
)

#----------------CONNECTION LINE---------------------

mycursor = mydb.cursor()
#-----------------REGISTER NEW USERS == CREATE--------------------

def register_users():
    
    print("---------  ENTER USER DETAILS    -----------\n \n")

    first_name=input("Enter the first name :").strip().lower()
    last_name=input("Enter the last name  : ").strip().lower()
    phone_number=(input("Enter the phone number: "))
    email=input("Enter your email address : ").strip().lower()
    address=input("Enter your address : ").strip().lower()
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if phone_number=="" or first_name=="" or last_name=="" or email=="" or address=="":
        print("Please Enter all the Details")
        return
    elif not(first_name.isalpha()):
        print(f'only alphabets allowed for this input field: First Name: {first_name}')
        return
    elif not(last_name.isalpha()):
        print(f'only alphabets allowed for this input field: LastName: {last_name}')
    elif not(address.isalpha()):
        print(f'only alphabets allowed for this input field: Address: {address}')
    elif not phone_number.isdigit() or len(phone_number) < 10:
        print("Phone number must be at least 10 digits long and contain only numbers.")
        return
    
    elif not re.match(email_regex, email):
        print("Invalid email format.")
        return
    else:
        
        sql_query="insert into userdetails(first_name,last_name,phone_number,email,address) values(%s,%s,%s,%s,%s)"

        values=(first_name,last_name,phone_number,email,address)
        mycursor.execute(sql_query,values)
        mydb.commit()
        print("--------- DATA SAVED SUCCESSFULLY!   -----------\n \n")


#-------------VIEW EXISTING USERS == READ------------------------

def view_user_details():
    
    
    sql_query="select * from userdetails"
    mycursor.execute(sql_query)
    
    results = mycursor.fetchall() 

    if not results:  
        
        print("No entries yet.")
    else:
        print("---------  USER DETAILS    -----------\n \n")
        for i in results:
            print(i)

#-----------------VIEW USERS BY LOCATION READ BY SPEC --------------------

def  view_users_bylocation(location,phone_number):

    sql_query="select * from userdetails where address=%s"
    mycursor.execute(sql_query, (location,))
    
    results = mycursor.fetchall()

    if not results:
        print("No entries found for the given location.")
    else:
        print(f"---------  USERS FROM {location}    -----------\n \n")
        for i in results:
            print(i)
        

#----------------- UPDATE USER DETAILS == UPDATE  --------------------

def update_user_details():

    print("---------  ENTER THE DETAILS THAT ARE TO BE UPDATED..  -----------\n \n")
    print("---------  DEATILS  THAT ARE AVAILABLE FOR AN UPDATION ARE PHONE NUMBER / EMAIL / ADDRESS  -----------\n \n")
    print("Do you want to update your phone number?")
    response=input("Y/N: ").lower()
    if (response=="y"):
        old_number=(input("ENTER YOUR OLD PHONE NUMBER : "))
        new_number=(input("ENTER YOUR NEW PHONE NUMBER : "))
            
        if old_number=="" or new_number=="" :
            print("Please Enter all the Details")
            return
            
        if not old_number.isdigit() or len(old_number) < 10 and not new_number.isdigit() or len(new_number) < 10:
            print("Phone numbers must be at least 10 digits long and contain only numbers.")
            return
        update_phone_number(old_number,new_number)
         
    else:
        print("Do you want to update your email?")
        response=input("Y/N: ").lower()
        if (response=="y"):
            old_email_id=(input("ENTER YOUR OLD EMAIL: "))
            new_email_id=(input("ENTER YOUR NEW EMAIL: "))
            update_email_id(old_email_id,new_email_id)
            
        else:
            print("Do you want to update your address?")
            response=input("Y/N: ").lower()
            if (response=="y"):
                old_address=(input("ENTER YOUR OLD ADDRESS: "))
                new_address=(input("ENTER YOUR NEW ADDRESS: "))
                phone_number=(input("ENTER YOUR PHONE NUMBER: "))
                update_address(old_address,new_address,phone_number)
                
            else:
                print("---------  NO OTHER OPTIONS AVAILABLE  -----------\n \n")
                
                
def update_address(old_address,new_address,phone_number):
    old_address = old_address.strip()
    new_address = new_address.strip()
    print(f"Attempting to update address from '{old_address}' to '{new_address}'")
    

    sql_query = "UPDATE userdetails SET address = %s WHERE address = %s and phone_number=%s"
    mycursor.execute(sql_query, (new_address,old_address,phone_number))
    mydb.commit() 
    if mycursor.rowcount > 0:
        print("Address updated successfully.")
    else:
        print("No record found with the provided old address.")

    
def update_email_id(old_email_id,new_email_id):
    sql_query = "UPDATE userdetails SET email = %s WHERE email = %s"
    mycursor.execute(sql_query, (new_email_id, old_email_id))
    mydb.commit() 
    if mycursor.rowcount > 0:
        print("Email updated successfully.")
    else:
        print("No record found with the provided old email.")

    
def update_phone_number(old_number, new_number):
    sql_query = "UPDATE userdetails SET phone_number = %s WHERE phone_number = %s"
    mycursor.execute(sql_query, (new_number, old_number))
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Phone number updated successfully.")
    else:
        print("No record found with the provided old phone number.")


#----------------- DELETE  --------------------
def delete_user_details():
    phone_number=input("ENTER THE PHONE NUMBER OF THE USER THAT IS TO BE DELETED: ")
    sql_query = "DELETE FROM userdetails WHERE phone_number = %s"
    mycursor.execute(sql_query, (phone_number,))
    mydb.commit()  
    
    if mycursor.rowcount > 0:
        print(f"User with phone number {phone_number} has been deleted.")
    else:
        print(f"No user found with phone number {phone_number}.")
    

def delete_all():
    sql_query = "TRUNCATE TABLE userdetails;"
    mycursor.execute(sql_query)
    mydb.commit()  
    print(" ALL RECORDS HAVE BEEN REMOVED")
    
    
#-------------------------------------    MAIN -------------------------------------
print("---------------------------------------------------\n \n")       
print(" *****  Welcome to ADMIN PANEL  *****\n \n")
print("---------------------------------------------------\n \n")
res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )


while(res != "7"):


    if res == "1":
        register_users() 
        print("---------------------------------------------------\n \n")
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )

        print("---------------------------------------------------\n \n")

    elif res == "2":
        view_user_details() 
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )
        print("---------------------------------------------------\n \n")   

    elif res == "3":
        location=input("Enter the Location: ")
        
        view_users_bylocation(location) 
        print("---------------------------------------------------\n \n")
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )
        print("---------------------------------------------------\n \n")

    elif res == "4":
        update_user_details()
        print("---------------------------------------------------\n \n") 
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )
        print("---------------------------------------------------\n \n")

    elif res == "5":
        delete_user_details() 
        print("---------------------------------------------------\n \n")
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )
        print("---------------------------------------------------\n \n")
    elif res == "6":
        delete_all()
        print("---------------------------------------------------\n \n")
        res=input("Enter the number of operation you want to perform :  \n 1.Register New User \n 2.View User Details  \n 3.View User details by location \n 4.Update User Details \n 5.Delete User Details \n 6.delete all records \n 7.exit \n \n" )
        print("---------------------------------------------------\n \n")

        
    elif res == "7":
        break
    else:
        print(" INVALID OPTION ")
        break
