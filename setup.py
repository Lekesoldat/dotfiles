import os

print("--- Starting dotfiles bootstrap ---\n")

ignored = [".git"]
folders = []
for file in os.listdir("."):
    if os.path.isdir(os.path.abspath(file)) and file not in ignored:
        folders.append(file)

for folder in folders:
    os.system(f"python3 ./{folder}/setup.py")
    print()
