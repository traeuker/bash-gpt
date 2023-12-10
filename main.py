import subprocess
import sys

from inference import get_command, extract_command

def is_exit_command(command):
    return command.lower() in ["exit", "quit", "e", "q", "x"]

def main():
    verbose = False
    while True:
        instruction = input("Enter command (or 'exit' to quit): ")

        if is_exit_command(instruction):
            break

        # Check for verbose flag
        if '-v' in instruction or '--verbose' in instruction:
            verbose = True
            instruction = instruction.replace('-v', '').replace('--verbose', '').strip()

        try:
            notes = ""
            while True:
                cmd_output = get_command(instruction, notes, verbose=verbose)
                extracted_cmd, extracted_notes = extract_command(cmd_output)

                if not extracted_cmd:
                    answer = input(f"Note: '{extracted_notes}'\n(Add additional comments or 'q' to quit): ")
                else:
                    answer = input(f"Do you want to run this command: '{extracted_cmd}'\n('y' or add additional comments or 'q' to quit): ")

                if is_exit_command(answer):
                    return  # Exits the main function, thereby stopping the program

                if answer.lower() in ["y", "yes"]:
                    break


                notes += f"The command {extracted_cmd} is not what the user was looking for.\n User commented: {answer}\n"

            print(extracted_cmd)
            result = subprocess.run(extracted_cmd.split(), capture_output=True, text=True, check=True)
            print(result.stdout)
            print(result.stderr, file=sys.stderr)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}", file=sys.stderr)

        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
