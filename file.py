# Задача номер 3

# Открываю и читаю все 3 файла
with open("Files/1.txt", encoding="utf-8") as file_one, open(
        "Files/2.txt", encoding="utf-8") as file_two, open(
            "Files/3.txt", encoding="utf-8") as file_three, open(
                "Files/result.txt", "a", encoding="utf-8") as result_file:

    file_one = file_one.readlines()     
    list_file_one = str(len(file_one))  # считаю количество строк для 1 файла

    file_two = file_two.readlines()
    list_file_two = str(len(file_two))    # считаю количество строк для 2 файла 

    file_three = file_three.readlines()
    list_file_three = str(len(file_three))   # считаю количество строк для 3 файла

    # Список из названия файлов, переменной в которой хранится файл и количество строк
    result_list = [("1.txt", file_one, list_file_one),
                   ("2.txt", file_two, list_file_two),
                   ("3.txt", file_three, list_file_three)]    

    # Сортирую  по количеству строк, в цикле записываю в результирующий файл
    for x, y, z in sorted(result_list, key=lambda x: x[2]):
 
        result_file.write(x + '\n')
        result_file.write(z + '\n')
        result_file.writelines(y)
        result_file.write('\n')



       
        
        