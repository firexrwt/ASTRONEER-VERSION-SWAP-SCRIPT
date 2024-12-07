import os


def swap_folders(folder1, folder2):
    try:
        if not os.path.exists(folder2):
            os.rename(folder1, folder2)
            print(f"Папка '{folder1}' успешно переименована в '{folder2}'.")
        else:
            temp_name = folder1 + "_temporary_swap_name"
            os.rename(folder1, temp_name)
            os.rename(folder2, folder1)
            os.rename(temp_name, folder2)
            print(f"Папки '{folder1}' и '{folder2}' успешно поменялись именами.")
    except Exception as e:
        print(f"Произошла ошибка при смене имен папок '{folder1}' и '{folder2}': {e}")


def wait_for_key():
    input("\nНажмите любую клавишу, чтобы выйти...")

def confirmation():
    print("Подтверждение замены папок: введите y для 'да' или n для 'нет'")
    answer = input()
    if answer == "y":
        return True
    elif answer == "n":
        return False
    else:
        print("Некорректный ввод. Попробуйте еще раз.")
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
