import os
import shutil
import platform

# Detect OS and set paths
OS_TYPE = platform.system()

if OS_TYPE == "Windows":
    CHROME_PATH = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data")
    BACKUP_PATH = os.path.expanduser("~\\Desktop\\ChromeBackup")
elif OS_TYPE == "Linux":
    CHROME_PATH = os.path.expanduser("~/.config/google-chrome")
    BACKUP_PATH = os.path.expanduser("./ChromeBackup")
else:  # macOS
    CHROME_PATH = os.path.expanduser("~/Library/Application Support/Google/Chrome")
    BACKUP_PATH = os.path.expanduser("./ChromeBackup")

# Restore Chrome User Data
backup_src = os.path.join(BACKUP_PATH, "ChromeUserData")
if os.path.exists(backup_src):
    shutil.copytree(backup_src, CHROME_PATH, dirs_exist_ok=True)
    print(f"[✔] Chrome profiles restored from {backup_src}")
else:
    print(f"[✘] No backup found!")

print("\n✅ Restore complete! Restart Chrome for changes to take effect.")
