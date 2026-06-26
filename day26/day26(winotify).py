from plyer import notification
import time
from tqdm import tqdm
import os
import dotenv

dotenv.load_dotenv()
from mistralai.client import Mistral

client = Mistral(api_key=os.environ.get("API_KEY"))

task = input("What task would you like the AI to simulate doing? ")
times = int(input("How many times would you like the AI to do this task? "))

inputs = [
    {"role":"user","content":f"{task}. Only return a digit in seconds."},
]

response = client.beta.conversations.start(
    agent_id="ag_019edc001d877765a7ac3b3c73d0be57",
    agent_version=0,
    inputs=inputs,
)

taken = int(response.outputs[0].content)
print(taken)
total_seconds = taken * times
bar = tqdm(range(total_seconds))
for t in bar:
    time.sleep(1)
notification.notify(
    title="Task Complete!",
    message=f"The AI has finished simulating {task} in {total_seconds} seconds!",
    app_icon="notify_icon.ico",
    timeout=5,
)
print(f"Congratulations. You have just wasted {total_seconds} seconds staring at a progress bar.")
time.sleep(3)
print(f'I mean, you could have done something like "{task}" but no. You wasted your time staring at a progress bar.')
time.sleep(3)
print(f"If you really want to stare at a progress bar, I have no hope left for you.")
time.sleep(3)
print(f"Do you know anyone who wastes their time staring at a progress bar? I don't.")
time.sleep(3)
print("[System message:] Thank you for using the semi-aggressive progress bar!")
time.sleep(3)