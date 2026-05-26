import os

def get_files(path):
    files = []

    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_file():
                files.append(entry.path)
            elif entry.is_dir():
                files.extend(get_files(entry.path))

    return files


def read_file(path):
    with open(path, 'r') as f:
        return f.read()

dir1 = input("첫 번째 디렉토리 이름: ")
dir2 = input("두 번째 디렉토리 이름: ")

files1 = get_files(dir1)
files2 = get_files(dir2)


if len(files1) != len(files2):
    print("파일이 다릅니다.")
else:
    same = True

    for f1, f2 in zip(sorted(files1), sorted(files2)):
        stat1 = os.stat(f1)
        stat2 = os.stat(f2)

        name1 = os.path.basename(f1)
        name2 = os.path.basename(f2)

        size_same = stat1.st_size == stat2.st_size

        content_same = read_file(f1) == read_file(f2)

        if name1 != name2 or not size_same or not content_same:
            same = False
            print(f"{f1} 와 {f2} 다릅니다.")

    if same:
        print("파일이 같습니다.")
    else:
        print("파일이 다릅니다.")
