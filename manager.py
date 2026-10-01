import subprocess
import sys
from pathlib import Path

worker_file = Path(__file__).with_name("worker.py")
workers = {}

print("Commands: start <name>, stop <name>, list, exit")

try:
    while True:
        parts = input("manager> ").strip().split()

        if not parts:
            continue

        command = parts[0].lower()

        if command == "start" and len(parts) == 2:
            name = parts[1]
            process = workers.get(name)

            if process is not None and process.poll() is None:
                print(f"{name} is already running.")
            else:
                workers[name] = subprocess.Popen(
                    [sys.executable, str(worker_file), name]
                )
                print(f"Started {name}. PID: {workers[name].pid}")

        elif command == "stop" and len(parts) == 2:
            name = parts[1]
            process = workers.get(name)

            if process is not None and process.poll() is None:
                process.terminate()
                process.wait()
                print(f"Stopped {name}.")
            else:
                print(f"{name} is not running.")

        elif command == "list" and len(parts) == 1:
            if not workers:
                print("No workers have been started.")

            for name, process in workers.items():
                status = (
                    "running" if process.poll() is None else "stopped"
                )
                print(f"{name}: {status}, PID: {process.pid}")

        elif command == "exit" and len(parts) == 1:
            break

        else:
            print("Commands: start <name>, stop <name>, list, exit")

except (KeyboardInterrupt, EOFError):
    print("\nExiting manager.")

finally:
    for name, process in workers.items():
        if process.poll() is None:
            process.terminate()
            process.wait()
            print(f"Stopped {name}.")

    print("Manager closed.")