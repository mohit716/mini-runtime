import subprocess
import sys
from pathlib import Path

worker_file = Path (__file__).with_name("worker.py")

process = None

print("Commands: start, status, stop, exit")



import subprocess
import sys
from pathlib import Path

worker_file = Path(__file__).with_name("worker.py")
process = None

print("Commands: start, status, stop, exit")

try:
    while True:
        command = input("manager> ").strip().lower()

        if command == "start":
            if process is not None and process.poll() is None:
                print("Worker is already running.")
            else:
                process = subprocess.Popen(
                    [sys.executable, str(worker_file)]
                )
                print(f"Started worker. PID: {process.pid}")

        elif command == "status":
            if process is None:
                print("Worker has not been started.")
            elif process.poll() is None:
                print(f"Worker is running. PID: {process.pid}")
            else:
                print(f"Worker stopped. Exit code: {process.returncode}")

        elif command == "stop":
            if process is not None and process.poll() is None:
                process.terminate()
                process.wait()
                print("Worker stopped.")
            else:
                print("No worker is running.")

        elif command == "exit":
            break

        else:
            print("Commands: start, status, stop, exit")

except (KeyboardInterrupt, EOFError):
    print("\nExiting manager.")

finally:
    if process is not None and process.poll() is None:
        process.terminate()
        process.wait()
        print("Worker stopped.")

    print("Manager closed.")


