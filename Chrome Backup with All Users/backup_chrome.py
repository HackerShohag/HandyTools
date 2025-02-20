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

# Create backup folder if not exists
os.makedirs(BACKUP_PATH, exist_ok=True)

# Backup entire Chrome User Data
backup_dest = os.path.join(BACKUP_PATH, "ChromeUserData")
if os.path.exists(CHROME_PATH):
    shutil.copytree(CHROME_PATH, backup_dest, dirs_exist_ok=True)
    print(f"[✔] Chrome profiles backed up to {backup_dest}")
else:
    print(f"[✘] Chrome profile directory not found!")

print("\n✅ Backup complete. Store the backup safely!")
