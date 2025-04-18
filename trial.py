# import os
# file_path = "./tasks/task.json"
# if os.path.exists(file_path):
#     print("right")
# else:
#     print("wrong")

# task['task status'] = "Complated"
#         data.pop()
#         print(type(data), " ", type(complate_task_list))
#         print("One task complated succesfully")
    

# # complate_task_list = [complated_task]
#     # tablefmt = tabulate(complate_task_list, headers="",tablefmt="grid")
#     # task = complate_task_list[0]
    

#  print(data)
#     for each_data in data:
#         try:
#             if int(each_data['task id']) == int(user_option):
#                 complated_task = each_data
#                 break
#         except ValueError:
#             print("There is no task with this id")
#     try:
#         change_status = input(f"Did you complate {complated_task['task name']}? enter[Y/N]: ").strip()
#         if change_status == "Y" or change_status == "y":
#             complated_task.clear()
#     except UnboundLocalError:
#             print("there is no task with the given Id ")

    # with open(filepath,'w') as json_file:
    #     json_data = json.dump(data, json_file)
    #     print("Task completed successfully")


    # if os.path.exists(filepath):    
    #         try:
    #             data = json.load(json_file)
    #             if isinstance(data,list):
    #                 data_list = data
    #             elif isinstance(data,dict):
    #                 data_list = [data]
    #             else:
    #                 data_list = []
    #             data_list = []
    # else:
    #     data_list = []
    # task_length = len((data_list))
    # task_id = task_length
    # if task_length == 0:
    #     task_id = 1
    # else:
    #     task_id += 1
    

    # data_list.append(new_data)

# if len(user_input) == 0:
# #                 print(f"you entered empty option")
# def read_write():
#     with open(filepath,"r") as json_file:
#         try:
#             data = json.load(json_file)
#             if isinstance(data, dict):
#                 return data
#             return data
#         except json.decoder.JSONDecodeError as e:
#             return None 