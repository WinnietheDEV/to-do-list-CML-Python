exit_program = False
to_do_list = []

try:
    with open("todo.txt") as file:
        tasks = file.readlines()
        for task in tasks:
            new_task = task.replace("\n", "")
            to_do_list.append(new_task)
except:
    print("Can't read the file!")


def print_tasks(array):
    for index, each_list in enumerate(array):
        print("{}. {}".format(index + 1, each_list))


def write_task():
    try:
        with open("todo.txt", 'w') as file:
            if len(to_do_list) == 0:
                file.write('')
            else:
                for task in to_do_list:
                    file.write(task+"\n")
    except:
        print("Can't write task to the file!")


while not exit_program:
    command = input('choose command: show, add, remove, edit, or exit: ').strip()
    match command:
        case "exit":
            exit_program = True
        case "show":
            print_tasks(to_do_list)
        case "add":
            task = input('Enter task: ')
            to_do_list.append(task)
            write_task()
        case "remove":
            print_tasks(to_do_list)
            index = int(input('Enter number of task to be removed: '))
            index = index - 1
            to_do_list.pop(index)
            write_task()
        case _:
            print('Hey, you entered wrong command')