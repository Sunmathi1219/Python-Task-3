# python function to read from a text file.The function will take the name of the text file and display the contentof the file into the console

def read_file_content(file_name):
    with open(file_name,'r')as file:
        content_read=file.read()
        print(content_read)


file_name="current_timestamp.txt"

read_file_content(file_name)