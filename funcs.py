import os
import shutil
import time
import logging
import pathlib as pl


black_suffixes = {
}

def config_input(config: dict) -> None:
    global black_suffixes
    black_suffixes = config['black_suffixes']


def DEBUG(sth='---DEBUG---'):
    print(sth)


def file_filter(fileObj: pl.Path) -> bool:
    # return True
    if fileObj.suffix.lower() in black_suffixes:
        return False
    if fileObj.name[0:2] == '~$':
        return False
    return True



def update(dtop, catalogues, files):
    catalogues.clear()
    files.clear()

    for item in os.listdir(dtop):
        itemObj = pl.Path(dtop).joinpath(item)
        # print(itemObj)
        if itemObj.is_dir():
            # 目录
            # print(itemObj)
            catalogues.append(itemObj.name)

        elif itemObj.is_file():
            filter_pass = file_filter(itemObj)
            if filter_pass:
                name, suffix = os.path.splitext(item)
                files.append((name, suffix))

    with open("catalogues.txt", "w", encoding="utf-8") as ct:
        for item in catalogues:
            ct.write(item + '\n')

    with open("files.txt", "w", encoding="utf-8") as fl:
        for n, s in files:
            fl.write(n + s + '\n')


def user_input(reminder) -> int:
    while True:
        try:
            ins = int(input(reminder))
            return ins
        except Exception:
            print('输入不合法！')


def filings(dtop, catalogues, files):
    i = 0
    for catalogue in catalogues:
        print(i, '.', catalogue, sep='', end=' ')
        i += 1

    print("\n\n---------------请输入数字以便将文件放入对应的文件夹中(回车以跳过，大写字母D以删除文件)----------------\n")

    for n, s in files:
        print(n, s[1:], end=' ')
        num = input()
        if num == '':
            continue
        file = os.path.join(dtop, n + s)
        if num == 'D':
            shutil.move(file, r'Removements')
        else:
            num = int(num)
            catalogue = os.path.join(dtop, catalogues[num])
            try:
                shutil.move(file, catalogue)
            


            except shutil.Error as se:
                new_name = f'{n}({time.time()}){s}'
                new_file = os.path.join(dtop, new_name)
                os.rename(file, new_file)
                file = new_file
                shutil.move(file, catalogue)

            except Exception as e:
                print(f"有错误{e}，请联系作者")

    print("\n\n---------------遍历结束----------------\n")



def to_end():
    print('感谢使用，制作者: @巨浪合金')
    time.sleep(1)


if __name__ == '__main__':
    shutil.move(r'C:\Users\zinca\Desktop\OneDrive 入门.pdf', r'C:\Users\zinca\Desktop\张皓宸乱七八糟')
