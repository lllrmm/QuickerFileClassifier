from funcs import *
import pathlib as pl
import json

CONFIG_FILE_NAME = 'config.json'
CONFIG_TAG_DESKTOP = 'desktop'
with open(CONFIG_FILE_NAME, encoding='utf-8') as config_file:
    config = json.load(config_file)


config_input(config)
dtop = config[CONFIG_TAG_DESKTOP]
catalogues = []
files = []


def DEBUG(sth='---DEBUG---'):
    print(sth)





if __name__ == '__main__':
    update(dtop, catalogues, files)

    while True:
        ins = user_input("1. 更新数据 2. 文件操作 3.退出: ")
        if ins == 1:
            update(dtop, catalogues, files)

        elif ins == 2:
            DEBUG()
            filings(dtop, catalogues, files)

        elif ins == 3:
            to_end()
            break