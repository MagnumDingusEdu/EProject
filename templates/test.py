import os 

basepath = "."
folder_list = []
with os.scandir(basepath) as file_directory_list:
    for elements in file_directory_list:
        if  not elements.is_file():
            folder_list.append(elements.name)
print(folder_list)

for folder in folder_list:
    file_list = os.scandir(folder)

    for filename in file_list:
        print(filename.name, end=',')
    print(folder)
    print("next dir")