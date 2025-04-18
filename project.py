import sys, json, os
from datetime import datetime, timedelta
from tabulate import tabulate

filepath = "./tasks/task.json"

# check and return the value entered is int or not 
def is_input_integer(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
    
def find_valid_option(): # check the option is number 
    is_number = False
    try:
        user_input = input("Enter option number: ").strip()
        option = is_input_integer(user_input) # tell's the input is integer or not
    except KeyboardInterrupt:
        print("\n Program interupted by user.")
        sys.exit()
    if len(user_input) == 0: # to check if the user leave the input blank
        print(f"you entered empty option")
    while not is_number:
        if option is False:
            try:
                user_input = input(" Please Enter valid option number: ").strip()
            except KeyboardInterrupt:
                print("\n Program interupted by user.")
                sys.exit()
            option = is_input_integer(user_input)
            if len(user_input) == 0:
                print(f"you entered empty option")               
        else:
            is_number = True
            return user_input

def get_valid_input(): # check the option is 1 - 5
    valid_option = find_valid_option()
    is_valid_option = False
    try:
        while not is_valid_option:
            if int(valid_option) < 1 or int(valid_option) > 5:
                print(f"You entered Invalid option number")
                valid_option = find_valid_option() # if user option is not from 1 - 5 ask the user reenter 
            elif int(valid_option) == 5:
                    print("\n  ++++++++++ Exiting the program ++++++++++")
                    sys.exit()
            else:
                is_valid_option = True
                return valid_option
    except KeyboardInterrupt :
        print("\n +++++ Program interupted by user. +++++")

def menu(): # display menu
    print("\n++++++++++++++++++++ Task Management ++++++++++++++++++++")   
    print("1: Create task")
    print("2: List Task")
    print("3: Complate Task")
    print("4: Delete Task")
    print("5: EXIT")
    user_option = get_valid_input()
    if user_option == "1":
        add_task()
    elif user_option == "2":
        pass
    elif user_option == "3":
        complate_task(3)
    elif user_option == "4":
        complate_task(4)


def data_read_write(write_data, mode):
    if mode == "w":
        try:
            if os.path.exists:
                with open(filepath, mode) as json_file:
                    json.dump(write_data, json_file)
                    json_file.write("\n")
                return True
            else:
                print("Folder not found")
                return None
        except:
            print("Unable to add new task")
            return None
    elif mode == "r":
        try:
            if os.path.exists:
                with open(filepath, mode) as json_file:
                    data = json.load(json_file)
                    return data
        except json.decoder.JSONDecodeError as e:
            return False 

# function to add Task
def add_task():
    try:
        task_name = input("please enter task name: ").strip()
        if task_name == "":
            print("You add no task ") # if no task name provided return to menu function
            menu()
            return None
        # data for each single tasks
        task_description = input("Enter Task description (optional):").strip()
    except KeyboardInterrupt :
        print("\n Program interupted by user.")    
    current_time = datetime.now()
    created_date = f"{(current_time).strftime("%d, %b")} {current_time.hour}:{current_time.minute:02} {(current_time).strftime("%p")} "
    task_status = "Incomplate"
    completion_time = (current_time + timedelta(hours=24))
    format_completion_time = f"{(completion_time).strftime("%d, %b")} {completion_time.hour}:{completion_time.minute:02} {(completion_time).strftime("%p")}"

    read_data = data_read_write("", "r")
    if read_data == False: # there is no data found
        data_list = []
        task_id = 1
        new_data = {  # formatted task data as json format           
            "task id": task_id,
            "task name": task_name,
            "task description":task_description,
            "created date":created_date,
            "completion time":format_completion_time,
            "task status": task_status
        }
        data_list.append(new_data) 
        write_data = data_read_write(data_list,"w")
    else:
        data_list = read_data
        dict_items = data_list[-1]
        last_item_id = dict_items['task id']
        new_data = {  # formatted task data as json format           
            "task id": last_item_id + 1,
            "task name": task_name,
            "task description":task_description,
            "created date":created_date,
            "completion time":format_completion_time,
            "task status": task_status
        }
        data_list.append(new_data)
        write_data = data_read_write(data_list,"w")
    menu()


def list_task():
        read_data = data_read_write(filepath,"r")
        print("++++++++++ List of existing tasks ++++++++++")
        table = tabulate(read_data, headers="keys", tablefmt="grid")
        print(table)
        menu()


def complate_task(option):
    completed_task = 0
    read_data = read_data = data_read_write("", "r")
    if read_data == None:
        print("There is no task yet ")
        return None
    try:
        read_data = data_read_write(filepath,"r")
        print("++++++++++ List of existing tasks ++++++++++")
        table = tabulate(read_data, headers="keys", tablefmt="grid")
        print(table)
        try:
            if option == 3:
                user_option = int(input("Enter Task Id to complate: ").strip())
            elif option == 4:
                user_option = int(input("Enter Task Id to Delete: ").strip())
        except KeyboardInterrupt:
                print("\n Program interupted by user.")    
    except ValueError:
        print("Your input is not a number")
        return None
    try:
        for data in read_data:
            
            if data['task id'] == user_option:
                selected_data = data
                break
    except UnboundLocalError:
        print("you intered invalid task Id")
        sys.exit()
    except TypeError:
        print("you intered Invalid input type")
        sys.exit()
    try:
        if option == 3:
            completed_task += 1
            selected_data['task status'] = "Completed"
            print("task completed successfully")
        elif option == 4:
            read_data = [data for data in read_data  if data != selected_data]
            print("task deleted successfully")
    except UnboundLocalError:
        print("Invalid Id entered")
        return None        
    write_data = data_read_write(read_data,"w")
    menu()

def main():
    menu()
      

if __name__ == "__main__":
    main()

