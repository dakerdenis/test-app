#from functions import get_todos, write_todos
import functions
import time

user_prmt = "Type add or show or edit,complete exit: "
todos = []
now = time.strftime("%b %d, %Y %H:%m:%S")
print("Today is", now)
while True:
    user_action = input(user_prmt)
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]        
        todos=functions.get_todos()            
        todos.append(todo + '\n')
        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos=functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith('edit'):
        
        
        try:
            number = int(user_action[5:])
            number = number -1
            todos=functions.get_todos()
                
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n' # Update the specific todo

            functions.write_todos(filepath="files/todos.txt",todos_arg=todos)
        except ValueError:
            print('your commad is not valid')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos=functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number)
            
            functions.write_todos(todos)
            
            message = f"todo {todo_to_remove} was remooved from the list"
            print(message)
        except IndexError:
            print('There is no item with that number')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye !")
