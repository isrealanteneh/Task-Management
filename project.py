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
    
def find_valid_option():
    is_number = False
    user_input = input("Enter option number: ")
    option = is_input_integer(user_input)
    if len(user_input) == 0:
        print(f"you entered empty option")
    while not is_number:
        if option is False:
            user_input = input(" Please Enter valid option number: ")
            option = is_input_integer(user_input)
            if len(user_input) == 0:
                print(f"you entered empty option")               
        else:
            is_number = True
            return user_input

def get_valid_input():
    valid_option = find_valid_option()
    is_valid_option = False
    while not is_valid_option:
        if int(valid_option) < 1 or int(valid_option) > 4:
            print(f"You entered Invalid option number")
            valid_option = find_valid_option()
        else:
            is_valid_option = True
            return valid_option

def menu(): # display menu
    print("++++++++++++++++++++ Task Management ++++++++++++++++++++")   
    menus = {
        1: "Create task",
        2: "List Task",
        3: "Compare Task",
        4: "Delete Task"
    }
    for key,value in menus.items():
        print(f"{key}. {value}")
    user_option = get_valid_input()
   
# function to add Task
def add_task():
    task_name = input("please enter task name: ")
    if task_name == "":
        print("You add no task ")
        menu()
        return None
    task_description = input("Enter Task description (optional):")
    current_time = datetime.now()
    created_date = f"{(current_time).strftime("%d, %b")} {current_time.hour}:{current_time.minute:02} {(current_time).strftime("%p")} "
    task_status = "Incomplate"
    completion_time = (current_time + timedelta(hours=24))
    format_completion_time = f"{(completion_time).strftime("%d, %b")} {completion_time.hour}:{completion_time.minute:02} {(completion_time).strftime("%p")} "
    if os.path.exists(filepath):    
        with open(filepath, "r") as json_file:
            try:
                data = json.load(json_file)
                if isinstance(data,list):
                    data_list = data
                elif isinstance(data,dict):
                    data_list = [data]
                else:
                    data_list = []
            except json.decoder.JSONDecodeError as e:
                data_list = []
                print(f"Error reading JSON data:")
    else:
        data_list = []
    task_length = len((data_list))
    task_id = task_length
    if task_length == 0:
        task_id = 1
    else:
        task_id += 1
    
    new_data = {
            "task id": task_id,
            "task name": task_name,
            "task description":task_description,
            "created date":created_date,
            "completion time":format_completion_time,
            "task status": task_status
                    }

    data_list.append(new_data)
    if os.path.exists(filepath):
        with open(filepath, "w") as json_file:
            json.dump(data_list, json_file)
            json_file.write("\n")
        print("New task successfully added")
    
def list_task():
        with open(filepath,'r') as json_file:
            try:
                data = json.load(json_file)
                if isinstance(data, list):
                    data_list = data
                if isinstance(data, dict):
                    data_list = [data]
                else:
                    data_list = []
            except json.decoder.JSONDecodeError as e:
                data_list = []
                print(f"There is no task ")
        table = tabulate(data, headers="keys", tablefmt="grid")
        print(table)


def read_write():
    with open(filepath,"r") as json_file:
        try:
            data = json.load(json_file)
            if isinstance(data, dict):
                return data
            return data
        except json.decoder.JSONDecodeError as e:
            return None 

def complate_task():
    # list_task()
    data = read_write()
    if data == None:
        print("There is no task ")
    user_option = input("Enter Task Id to complate: ").strip()
    print(data)
    for each_data in data:
        try:
            if int(each_data['task id']) == int(user_option):
                complated_task = each_data
                break
        except ValueError:
            print("There is no task with this id")
    try:
        change_status = input(f"Did you complate {complated_task['task name']}? enter[Y/N]: ").strip()
        if change_status == "Y" or change_status == "y":
            complated_task.clear()
    except UnboundLocalError:
            print("there is no task with the given Id ")

    with open(filepath,'w') as json_file:
        json_data = json.dump(data, json_file)
        print("Task completed successfully")




def main():
    # menu()
    # add_task()
    # list_task()
     complate_task()



if __name__ == "__main__":
    main()

