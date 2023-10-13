import os
import glob

def get_file_paths():
    file_path = f'{os.getcwd()}/'
    file_paths = glob.glob(file_path + '*.txt')
    return file_paths

 
def read_files_entry_result():
    files_paths = get_file_paths()
    file_text = []
    for file in files_paths:
        file_names = file.split('\\')[-1]
        with open(file, encoding="utf-8") as input_data:
            text = input_data.readlines()
            file_text.append([len(text), file_names, text])
    file_text.sort()
    with open ("result_text.txt", "w", encoding="utf-8") as result:
        for item in file_text:
            result.write(f'{item[1]}\n{item [0]}\n{" ".join(item[2])}\n')
    return file_text

print(read_files_entry_result())