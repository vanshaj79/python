import signal
import time
import sys

# custom handler
def handler(signum, frame):
    print("\nSignal received:", signum)
    print("CTRL+C detect hua, program stop nahi hoga abhi!")
    
# register handler for SIGINT (CTRL+C)
signal.signal(signal.SIGINT, handler)

print("Program start ho gaya. CTRL+C dabao test ke liye...")
while True:
    time.sleep(1)
