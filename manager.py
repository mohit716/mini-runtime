import subprocess
import sys
from pathlib import Path

worker_file = Path (__file__).with_name("worker.py")

process = subprocess.Popen([sys.executable, str(worker_file)])

printf(f"Worker process started with PID: {process.pid}")

try:
    input("Press Enter to stop the worker...\n")
finally:
    process.terminate()
    process.wait()
    print("Manager: Worker stopped.")



