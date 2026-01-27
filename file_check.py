import os
import sys
from datetime import datetime

file_path = "input/data.txt"
log_file = "logs/job.log"

print("Job started")

with open(log_file, "a") as log:
    log.write(f"{datetime.now()} - Job started\n")

if os.path.exists(file_path):
    print("Input file found")

    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - File found\n")

    print("JOB SUCCESS")
    sys.exit(0)   # ✅ SUCCESS
else:
    print("Input file NOT found")

    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - File missing\n")

    print("JOB FAILED")
    sys.exit(1)   # ❌ FAILURE (VERY IMPORTANT)
