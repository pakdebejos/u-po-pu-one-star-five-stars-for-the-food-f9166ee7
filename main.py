"""Worth Turning the Fleet Around: one-line entry for make.fun.

The program writes exactly one line - an alien visitor's one-star review of Earth, redeemed by a bowl of noodle soup - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 177 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = 'One star because your planet made me queue for three hours to watch a sunset, but the noodle soup at the bottom of the stairs was worth the entire invasion fleet turning around.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
