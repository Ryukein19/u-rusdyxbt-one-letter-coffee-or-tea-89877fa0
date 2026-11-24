import os
# One-liner entry (1 char): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "A"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
