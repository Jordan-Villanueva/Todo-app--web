FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
     to-do items
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def convert_to_meters(feet_loc,inches_loc):
    meters_loc = feet_loc*0.3048 + inches_loc*0.0254
    return meters_loc

if __name__ == "__main__":
    print("Hello")
    print("Hi")