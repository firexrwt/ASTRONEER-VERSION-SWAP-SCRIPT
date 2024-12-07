import os


def swap_folders(folder1, folder2):
    try:
        if not os.path.exists(folder2):
            os.rename(folder1, folder2)
            print(f"The folder '{folder1}' has been successfully renamed to '{folder2}'.")
        else:
            temp_name = folder1 + "_temporary_swap_name"
            os.rename(folder1, temp_name)
            os.rename(folder2, folder1)
            os.rename(temp_name, folder2)
            print(f"The folders '{folder1}' and '{folder2}' have successfully swapped names.")
    except Exception as e:
        print(f"An error occurred while swapping folder names '{folder1}' and '{folder2}': {e}")


def wait_for_key():
    input("\nPress any key to exit...")

def confirmation():
    print("Folder swap confirmation: enter y for 'yes' or n for 'no'")
    answer = input()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("\nInvalid input. Please try again.")
        return confirmation()



# Пример использования для папок в текущем каталоге
confirmation()
local_folder1 = "ASTRONEER"
local_folder2 = "ASTRONEER_temp"
swap_folders(local_folder1, local_folder2)
appdata_local = os.path.join(os.getenv('LOCALAPPDATA'))
appdata_folder1 = os.path.join(appdata_local, "Astro")
appdata_folder2 = os.path.join(appdata_local, "Astro_temp")
swap_folders(appdata_folder1, appdata_folder2)
wait_for_key()
