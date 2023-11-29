import subprocess
import sys

from inference import get_command

def main():
    while True:
        # Prompt user for input
        instruction = input("Enter command (or 'exit' to quit): ")
        if instruction.lower() in ['exit', 'quit', 'e']:
            break
        try:
            notes = ''
            # keep looping over prompt until you find solution that agrees with user
            while True:
                # get command by 
                cmd = get_command(instruction, notes)

                # ask do you want to run this command?
                answer = input(f"Do you want to run this command: '{cmd}'\n('y' or add additional comments): ")

                if answer.lower() in ['y', 'yes']:
                    break

                notes += f"The command {cmd} did not work.\n User said: {answer}\n"
            # Execute the command
            print(cmd)
            result = subprocess.run(cmd.split(), capture_output=True, text=True, check=True)
            # Print the output
            print(result.stdout)
            print(result.stderr, file=sys.stderr)
        except subprocess.CalledProcessError as e:
            # Print error message if the command execution fails
            print(f"Error: {e}", file=sys.stderr)
        except Exception as e:
            # General error handling
            print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
