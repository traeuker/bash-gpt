import subprocess
import sys

def main():
    while True:
        # Prompt user for input
        cmd = input("Enter command (or 'exit' to quit): ")
        if cmd.lower() in ['exit', 'quit', 'e']:
            break

        try:
            # Execute the command
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
