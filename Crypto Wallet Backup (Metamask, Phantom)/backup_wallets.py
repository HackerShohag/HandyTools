import os
import shutil
import platform

# Wallet extensions (Update if needed)
WALLET_EXTENSIONS = {
    "MetaMask": "nkbihfbeogaeaoehlefnkodbefgpgknn",
    "Phantom": "bfnaelmomeimhlpmgjnjophhpkkoljpa"
}

# Detect OS
OS_TYPE = platform.system()
if OS_TYPE == "Windows":
    CHROME_PATH = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Local Extension Settings")
    BACKUP_PATH = os.path.expanduser("~\\Desktop\\CryptoWalletBackup")
else:  # Linux/Mac
    CHROME_PATH = os.path.expanduser("~/.config/google-chrome/Default/Local Extension Settings")
    BACKUP_PATH = os.path.expanduser("./CryptoWalletBackup")

# Create backup folder if not exists
os.makedirs(BACKUP_PATH, exist_ok=True)

# Backup process
for wallet, ext_id in WALLET_EXTENSIONS.items():
    src_path = os.path.join(CHROME_PATH, ext_id)
    dest_path = os.path.join(BACKUP_PATH, wallet)

    if os.path.exists(src_path):
        shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        print(f"[✔] Backup completed for {wallet} → {dest_path}")
    else:
        print(f"[✘] {wallet} not found in Chrome storage.")

print("\n✅ All available wallets have been backed up.")
