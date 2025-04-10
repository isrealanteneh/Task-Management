import os
file_path = "./tasks/task.json"
if os.path.exists(file_path):
    print("right")
else:
    print("wrong")