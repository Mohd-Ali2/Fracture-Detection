import subprocess
import os

def dump_messages():
    # Define the path to the messages directory on Android
    android_messages_dir = "/data/data/com.android.providers.telephony/databases/mmssms.db"

    # Define the path to the destination folder on the computer
    dump_folder = "C:\\Messages\\Dump_messages"

    # Create the directory if it doesn't exist
    os.makedirs(dump_folder, exist_ok=True)

    try:
        # Use adb to pull the messages database from Android to the computer
        subprocess.run(['adb', 'pull', android_messages_dir, dump_folder], check=True)
        print("Messages successfully dumped and stored in '{}' folder.".format(dump_folder))
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    # Dump messages from Android device to PC
    dump_messages()
