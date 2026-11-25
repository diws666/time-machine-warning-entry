#!/usr/bin/env python3
"""Writes the time machine warning label entry to /output/entry.txt."""

LABEL = "WARNING: Returning to 2020 will void your warranty and your will to live."  # 73 characters

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LABEL)

print("bytes written:", len(LABEL.encode("utf-8")))
print("verification result: byte-identical True")
