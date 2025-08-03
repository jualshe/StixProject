#function with outputs
from symbol import return_stmt


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't proved the right data"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name(input("What is your first name?"),input("What is your last name?"))
print(formated_string)