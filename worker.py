import sys
import time

name = sys.argv[1]

while True:
    print(f"[{name}] I'm running!", flush=True)
    time.sleep(2)