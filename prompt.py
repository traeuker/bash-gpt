import os
import platform
import getpass

def get_os_info():
    return platform.system() + " " + platform.release()

def get_current_directory():
    return os.getcwd()

def get_user_permissions():
    if os.name == 'nt':  # Windows
        # In Windows, there's no easy built-in way to check for admin rights
        return "unknown (admin check not implemented on Windows)"
    else:
        # On Unix and MacOS, being root usually means admin privileges
        return "administrator" if os.getuid() == 0 else "regular user"

def get_environment_variables():
    # You might want to filter out sensitive information here
    return ", ".join([f"{key}={value}" for key, value in os.environ.items()])

def fill_initial_prompt(template):
    filled_template = template.replace("[Operating_System_Info]", get_os_info())
    filled_template = filled_template.replace("[Current_Directory_Path]", get_current_directory())
    filled_template = filled_template.replace("[User_Permission_Level]", get_user_permissions())
    # filled_template = filled_template.replace("[Environment_Variables_Info]", get_environment_variables())

    return filled_template

def get_prompt():
    with open("initial_prompt.txt", "r") as file:
        initial_prompt_template = file.read().strip()

    filled_initial_prompt = fill_initial_prompt(initial_prompt_template)

    return filled_initial_prompt

if __name__ == "__main__":
    get_prompt()
