from datetime import datetime

def time_stamp():
    # getting user input
    input_data = input("Enter date and time in this format 31/12/2022 01:00:00 ")
    # changing to datetime module
    try:
        data = datetime.strptime(input_data,"%d/%m/%Y %H:%M:%S")
        # converting into Timestamp
        timestamp = datetime.timestamp(data)
        print(timestamp)
    except ValueError as e:
        print(e)

# calling the function
time_stamp()