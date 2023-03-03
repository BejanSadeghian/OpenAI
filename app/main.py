from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

# Other code that uses db_url and secret_key
openai.organization = "org-OFNtsHfjRVB0oCSAOS3k4UOE"
openai.api_key = os.getenv("API_KEY")
models = openai.Model.list()

# r = openai.Completion.create(
#   engine="davinci",
#   prompt="Make a list of astronomical observatories:"
# )

keep_going = True
conversation = []
while keep_going:
    print("\n\nSay something: (type 'quit()' to leave) for \n")
    prompt = input()
    if prompt == "quit()":
        break
    conversation.append({"role": "user", "content": prompt})
    # print(prompt)
    r = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )
    chatgpt_response = r.choices[0]["message"]["content"]
    conversation.append({"role": "assistant", "content": chatgpt_response})
    print(chatgpt_response)
