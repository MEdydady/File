with open("Files/1.txt", encoding="utf-8") as file_one, open(
        "Files/2.txt", encoding="utf-8") as file_two, open(
            "Files/3.txt", encoding="utf-8") as file_three, open(
                "Files/result.txt", "a", encoding="utf-8") as result_file:

    file_one = file_one.readlines()
    list_file_one = ['1.txt\n', str(len(file_one)) + '\n']

    file_two = file_two.readlines()
    list_file_two = ['2.txt\n', str(len(file_two)) + '\n']

    file_three = file_three.readlines()
    list_file_three = ['3.txt\n', str(len(file_three)) + '\n']

    result_dict = {'1.txt': 8, '2.txt': 1, '3.txt': 9}
    dict_file_name = {
        '1.txt': file_one,
        '2.txt': file_two,
        '3.txt': file_three
    }

    for x in sorted(result_dict.items(), key=lambda x: x[1]):
        z = str(x[1])

        result_file.write(x[0] + '\n')
        result_file.write(z + '\n')
        k = dict_file_name.get(x[0])
        result_file.writelines(k)
        result_file.write('\n')

   