import subprocess
import sys

jobs = [
    "file_check.py",
    "disk_check.py"
]

for job in jobs:
    print(f"Running {job}")

    result = subprocess.run(
        ["python", job]
    )

    if result.returncode != 0:
        print(f"{job} FAILED — stopping pipeline")
        sys.exit(1)

print("ALL JOBS PASSED — PIPELINE SUCCESS")
sys.exit(0)
