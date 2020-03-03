import os
from pathlib import Path
from distutils.dir_util import copy_tree

print("> Installing Fonts")

ignored = [".git"]
folders = []
for file in os.listdir("."):
    if os.path.isdir(os.path.abspath(file)) and file not in ignored:
        folders.append(file)

for folder in folders:
    print(f"\t* Installing {folder}")
    src = os.path.abspath(folder)
    dst = f"{Path.home()}/Library/Fonts"
    copy_tree(src, dst)
