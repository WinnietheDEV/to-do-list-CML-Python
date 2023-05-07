exit_program = False
to_do_list = ['cooking']


def print_tasks(array):
    for index, each_list in enumerate(array):
        print("{}. {}".format(index + 1, each_list))


def extract_task(array):
    return " ".join(word for index, word in enumerate(command_and_task) if index > 0)


while not exit_program:
    command_and_task = input('type command: show, add, remove, or exit: ').split(' ')
    command = command_and_task[0]
    if len(command_and_task) > 1:
        task = extract_task(command_and_task)
    if command == 'exit':
        exit_program = True
    elif command == 'show':
        print_tasks(to_do_list)
    elif command == 'add':
        to_do_list.append(task)
    elif command == 'remove':
        to_do_list.remove(task)