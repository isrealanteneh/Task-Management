# Task Management System

This is a Python-based task management system that allows users to manage their tasks effectively. The program provides a menu-driven interface where users can add, list, complete, and delete tasks.

## Features

1. **Add Task**
   - Command: Select menu option `1`.
   - Allows the user to add a new task by providing a task name and an optional description.
   - Automatically assigns a unique task ID, sets the creation date, and calculates the completion deadline (24 hours from creation).

2. **List Task**
   - Command: Select menu option `2`.
   - Displays all existing tasks in a tabular format.
   - Shows task details such as ID, name, description, creation date, completion time, and status.

3. **Complete Task**
   - Command: Select menu option `3`.
   - Marks a task as "Completed" by entering its task ID.
   - Updates the task status in the task list.

4. **Delete Task**
   - Command: Select menu option `4`.
   - Deletes a task by entering its task ID.
   - Removes the task from the task list.

5. **Exit Program**
   - Command: Select menu option `5`.
   - Exits the program gracefully.

## How to Use

1. Run the program by executing `project.py`.
2. A menu will be displayed with the following options:++++++++++++++++++++ Task Management ++++++++++++++++++++ 1: Create task 2: List Task 3: Complete Task 4: Delete Task 5: EXIT
3. Enter the corresponding menu option number to perform the desired action.
4. Follow the prompts to add, list, complete, or delete tasks.

## File Structure

- **`tasks/task.json`**: Stores the task data in JSON format.
- **`project.py`**: Main program file containing the task management logic.

## Dependencies

- Python 3.x
- `tabulate` library for displaying tasks in a tabular format.

Install the `tabulate` library using:
```sh
pip install tabulate
