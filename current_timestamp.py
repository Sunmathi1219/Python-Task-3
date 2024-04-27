#function will create a text file with current timestamp,and the file content should have the content of current timestamp

import datetime

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # To get current time

def create_timestamp_file(file_name):
    with open(file_name,'w')as file:
        file.write(current_time)
        file.close


file_name="current_timestamp.txt"  


print(f"Text File has been created successfully with Current Timestamp: {current_time}")


create_timestamp_file(file_name)

     





























'''
import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate the file name with the timestamp
    file_name = "timestamp.txt"
    
    # Create and write to the file
    with open(file_name, 'w') as file:
        file.write(current_time)
    
    print(f"File '{file_name}' created successfully with timestamp: {current_time}")

# Call the function to create the timestamp file
create_timestamp_file()

'''