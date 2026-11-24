import os
# One-liner entry: the line below is the whole submission.
LINE = "A"
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
