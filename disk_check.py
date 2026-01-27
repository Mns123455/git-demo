
import shutil
import sys
from datetime import datetime

log_file = "logs/disk_job.log"
threshold_gb = 5

try:
    total, used, free = shutil.disk_usage("C:/")
    free_gb = free // (1024**3)

    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - Free space: {free_gb} GB\n")

    print(f"Free disk space: {free_gb} GB")

    if free_gb < threshold_gb:
        print("DISK SPACE LOW - JOB FAILED")
        sys.exit(1)
    else:
        print("DISK SPACE OK - JOB SUCCESS")
        sys.exit(0)

except Exception as e:
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - ERROR: {str(e)}\n")

    print("JOB FAILED DUE TO ERROR")
    sys.exit(1)
