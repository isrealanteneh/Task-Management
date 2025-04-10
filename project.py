import sys, json, os
from datetime import datetime, timedelta
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
    task_status = False
    completion_time = (current_time + timedelta(hours=24))
    format_completion_time = f"{(completion_time).strftime("%d, %b")} {completion_time.hour}:{completion_time.minute:02} {(completion_time).strftime("%p")} "
    filepath = "./tasks/task.json"
    with open(filepath, "r") as json_file:
        json_datas = json.load(json_file)
        # print(len(json_datas))
    # new_task_data = {
    #         "task name": task_name,
    #         "task description":task_description,
    #         "created date":created_date,
    #         "completion time":format_completion_time,
    #         "task status": task_status
    # }
    # if os.path.exists(filepath):
    #     with open(filepath, "a") as json_file:
    #         json.dump(new_task_data, json_file)
    #         json_file.write("\n")
    #     print("New task successfully added")
    




def main():
    # menu()
    add_task()



if __name__ == "__main__":
    main()

