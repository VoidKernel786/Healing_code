import ast
import inspect
import shutil
import os
import time


def print_with_delay(text, delay=1.0):
    print(text)
    time.sleep(delay)


def heal(file):
    current_file = file
    backup_file = current_file + ".bak"

    if not os.path.exists(backup_file):
        print("Creating initial backup...")
        shutil.copyfile(current_file, backup_file)

    # Read source
    with open(file, "r", encoding="utf-8") as f:
        src = f.read()

    # Try to parse to detect syntax errors
    try:
        ast.parse(src)
        print("✅ Code OK:", file)
    except SyntaxError:
        print_with_delay(f"⚠️ Corruption detected in: {file}")
        print_with_delay("Restoring backup...")

        # Restore from backup
        shutil.copy(file + ".bak", file)
        print("✔ Restored:", file)


if __name__ == "__main__":
    heal("target_script.py")
