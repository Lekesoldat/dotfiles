import os
from pathlib import Path

print("> Setting up VSCODE")

# Settings
print("Symlinking settings.json")
src = f"{os.getcwd()}/settings.json"
dst = f"{Path.home()}/Library/Application Support/Code/User/settings.json"
os.symlink(src, dst)
print(f"Symlinked {src} -> {dst}")

# Keybindings
print("Symlinked keybindings.json")
src = f"{os.getcwd()}/settings.json"
dst = f"{Path.home()}/Library/Application Support/Code/User/keybindings.json"
os.symlink(src, dst)
print(f"Linked {src} -> {dst}")
