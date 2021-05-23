import os

def sum_floder(folder):
    sum = 0
    if os.path.isfile(folder):
        return os.path.getsize(folder)
    else:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                sum += os.path.getsize(file_path)
            else:sum += sum_floder(file_path)
    return sum

def sum_folder_num(folder):
    sum_num = 0
    if os.path.isfile(folder):
        return 1
    else:
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isfile(file_path):
                sum_num += 1
            else:sum_num += sum_folder_num(file_path)
    return sum_num



def sum_space_loop(folder):
    sum_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                sum_size += os.path.getsize(file_path)
    return sum_size

my_folder = "../pythonProject/venv"

print("----using recursion to count the total space occupied-------")
print("Total size is:" + str(sum_floder(my_folder)) + "byte")
print("----using recursion to count the total number of files-------")
print("Total number of files is:" + str(sum_folder_num(my_folder)))
print("----using os.walk to count the total space occupied-------")
print("Total size is:" + str(sum_space_loop(my_folder)) + "byte")

