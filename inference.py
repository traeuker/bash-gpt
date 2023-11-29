import os
from openai import OpenAI

with open("/Users/tilman/.openaikey", "r") as file:
    api_key = file.read().strip()


client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=api_key,
)

def get_command(instruct, notes):
    messages = [
        {"role": "system", "content": "You are a Linux user. You are trying to find commands that best reflect the user's instructions. Only output the commands."},
        {"role": "user", "content": instruct}
    ]

    if notes:
        messages.append({"role": "user", "content": notes})

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )

    answer = response.choices[0].message.content
    # print("AI:", answer)
    return answer




if __name__ == "__main__":
    get_command('show me all files in this directory', '')

