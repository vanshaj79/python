import os
from dotenv import load_dotenv
from openai import OpenAI

# load env
load_dotenv()

client = OpenAI()


# read task from file
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()


# make a call to open ai with prompt to categorize our tasks
def summarize_tasks(tasks):
    prompt = f"""
        you are a smart task planning agent.
        given a list of tasks, categorize them into 3 priority buckets:
        - High priority
        - Medium priority
        - Low priority
        Tasks:
        {tasks}
        
        return the response in this format:
        High Priority
        - task 1
        - task 2
        Medium Priority
        - task1 
        - task 2
        Low Priority
        - task 1
        - task 2
    """

    response = client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": prompt}]
    )
    print("\n RESPONSE \n")
    print(response)
    return response.choices[0].message.content


if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)
    print("\n Task Summary \n")
    print("-" * 30)
    print(summary)
