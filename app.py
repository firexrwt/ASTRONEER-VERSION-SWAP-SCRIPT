import msvcrt
import os
from win32api import GetFileVersionInfo


def get_exe_version(folder_path):
    try:
        astro_exe_path = os.path.join(folder_path, "Astro.exe")
        info = GetFileVersionInfo(astro_exe_path, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        version = f"{ms >> 16}.{ms & 0xffff}.{ls >> 16}.{ls & 0xffff}"
        print(f"Версия Astro.exe в папке '{folder_path}': {version}")
        return version
    except Exception as e:
        print(f"Версия Astro.exe в папке '{folder_path}': None")
        return None


def swap_folders(folder1, folder2):
    try:
        # Запрос подтверждения после вывода версий
        if confirmation():
            if not os.path.exists(folder2):
                os.rename(folder1, folder2)
                print(f"Папка '{folder1}' успешно переименована в '{folder2}'.")
                os.makedirs(folder1)
            else:
                temp_name = folder1 + "_temporary_swap_name"
                os.rename(folder1, temp_name)
                os.rename(folder2, folder1)
                os.rename(temp_name, folder2)
                print(f"Папки '{folder1}' and '{folder2}' успешно обменены именами.")
        else:
            print("Обмен папок отменен.")

    except Exception as e:
        print(f"Произошла ошибка при обмене именами папок '{folder1}' and '{folder2}': {e}")


def wait_for_key():
    print("\nНажмите Enter для выхода...")
    while True:
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 13:  # 13 - ASCII код клавиши Enter
                break


def confirmation():
    print("Подтвердите обмен папок (y/n):")
    answer = input().lower()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("\nНеверный ввод. Пожалуйста, попробуйте еще раз.")
        return confirmation()


# Пример использования для папок в текущем каталоге
local_folder1 = "ASTRONEER"
local_folder2 = "ASTRONEER_temp"
get_exe_version(local_folder1)
get_exe_version(local_folder2)
swap_folders(local_folder1, local_folder2)
appdata_local = os.path.join(os.getenv('LOCALAPPDATA'))
appdata_folder1 = os.path.join(appdata_local, "Astro")
appdata_folder2 = os.path.join(appdata_local, "Astro_temp")
swap_folders(appdata_folder1, appdata_folder2)
wait_for_key()