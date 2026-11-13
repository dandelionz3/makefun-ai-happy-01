"""Copy entry.png unchanged to the output directory and verify the copy.

Local run: mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

source = Path(__file__).resolve().parent / "entry.png"
if not source.is_file():
    raise FileNotFoundError(f"Entry image is missing: {source}")
if source.stat().st_size > 1_048_576:
    raise ValueError(f"Entry image exceeds 1,048,576 bytes: {source}")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
target = output_dir / "entry.png"
shutil.copyfile(source, target)
if source.read_bytes() != target.read_bytes():
    raise IOError(f"Copied image does not match source: {target}")
print(f"Copied and verified {target.stat().st_size} bytes to {target}")
