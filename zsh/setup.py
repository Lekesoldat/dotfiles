import os
from pathlib import Path

print("> Setting up ZSH")
print("Symlinking .zshrc to home directory")

src = f"{os.getcwd()}/.zshrc"
dst = f"{Path.home()}/.zshrc"
os.symlink(src, dst)

print(f"Symlinked {src} -> {dst}")
