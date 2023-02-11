from bs4 import BeautifulSoup
import requests
import pandas as pd
import xml.etree.cElementTree as ET
import codecs
from pathlib import Path
import os
import datetime
import re
import zipfile
import os


list_oks = []
list_cadastr = []
list_file_name = []
list_nazn = []
list_name = []
list_addres = []
extension = ".xml"

#rint("Введите путь к папке с архивами выписок")
#path1 = input()
#path1.replace("\"","\\")
#base_dir = r"C:\Users\User\PycharmProjects\xml\oks\pack_oks"


def read_oks(base_dir):

    os.chdir(base_dir)
    now1 = datetime.datetime.now()
    s = []
    for item in Path('.').glob('*'):
        file_path = os.path.abspath(str(item))
        if file_path.endswith('.xml'):
            s.append(1)

    d = 0
    for item in Path('.').glob('*'):
        file_path = os.path.abspath(str(item))

        if file_path.endswith('.xml'):

            if item.is_file():
                file = codecs.open(str(item),
                               "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")  # собираем кадастровый номер

                b_unique = BS_data.find('build_record')
                b_unique = b_unique.find('object')
                b_unique = b_unique.find('cad_number')
                b_unique = b_unique.text
                list_cadastr.append(b_unique)
                list_file_name.append(file_name)



# собираем ОКСы
            try:
                if item.is_file():
                    file = codecs.open(str(item),
                               "r", "utf-8")
                    file_path = os.path.abspath(str(item))
                    file_name = os.path.basename(file_path)
                    data = file.read()

                    BS_data = BeautifulSoup(data, "xml")

                    b_unique = BS_data.find('land_cad_numbers')
                    b_unique = b_unique.find_all('cad_number')

                    b_unique1 = []
                    for i in range(len(b_unique)):
                        b_unique2 = b_unique[i].get_text()
                        result = b_unique2[0]
                        for letter in b_unique2[1:]:
                            if letter.isupper():
                                result += f' {letter}'
                            else:
                                result += letter
                        b_unique1.append(result)

#                b_unique = b_unique.text
                    list_oks.append(b_unique1)
            except:
                b_unique = " "
                list_oks.append(b_unique)

# собираем Назначение
            try:
                if item.is_file():
                    file = codecs.open(str(item),
                                           "r", "utf-8")
                    file_path = os.path.abspath(str(item))
                    file_name = os.path.basename(file_path)
                    data = file.read()

                    BS_data = BeautifulSoup(data, "xml")

                    b_unique = BS_data.find('build_record')
                    b_unique = b_unique.find('params')
                    b_unique = b_unique.find_all('value')

                    b_unique1 = []
                    for i in range(len(b_unique)):
                        b_unique2 = b_unique[i].get_text()
                        result = b_unique2[0]
                        for letter in b_unique2[1:]:
                            if letter.isupper():
                                result += f' {letter}'
                            else:
                                result += letter
                        b_unique1.append(result)

                    list_nazn.append(b_unique1)
            except:
                b_unique = " "
                list_nazn.append(b_unique)

# собираем Наименование
            try:
                if item.is_file():
                    file = codecs.open(str(item),
                                           "r", "utf-8")
                    file_path = os.path.abspath(str(item))
                    file_name = os.path.basename(file_path)
                    data = file.read()

                    BS_data = BeautifulSoup(data, "xml")  # собираем кадастровые номера

                    b_unique = BS_data.find('build_record')
                    b_unique = b_unique.find('params')
                    b_unique = b_unique.find_all('name')

                    b_unique1 = []
                    for i in range(len(b_unique)):
                        b_unique2 = b_unique[i].get_text()
                        result = b_unique2[0]
                        for letter in b_unique2[1:]:
                            if letter.isupper():
                                result += f' {letter}'
                            else:
                                result += letter
                        b_unique1.append(result)

                    list_name.append(b_unique1)
            except:
                b_unique = " "
                list_name.append(b_unique)

# собираем Адрес
            try:
                if item.is_file():
                    file = codecs.open(str(item),
                                           "r", "utf-8")
                    file_path = os.path.abspath(str(item))
                    file_name = os.path.basename(file_path)
                    data = file.read()

                    BS_data = BeautifulSoup(data, "xml")  # собираем кадастровые номера

                    b_unique = BS_data.find('build_record')
                    b_unique = b_unique.find('address_location')
                    b_unique = b_unique.find_all('readable_address')

                    b_unique1 = []
                    for i in range(len(b_unique)):
                        b_unique2 = b_unique[i].get_text()
                        result = b_unique2[0]
                        for letter in b_unique2[1:]:
                            if letter.isupper():
                                result += f' {letter}'
                            else:
                                result += letter
                        b_unique1.append(result)

                    list_addres.append(b_unique1)
            except:
                b_unique = " "
                list_addres.append(b_unique)
            path = Path(base_dir)
            d = d + 1
            print(file_path, "--", d,"/", sum(s))





        df_1 = pd.DataFrame( {'Имя файла':list_file_name,'Кадастровый номер':list_cadastr,'ОКС':list_oks,'Назначение':list_nazn,'Наименование':list_name,'Адрес':list_addres})
#    df_1.to_excel(r'C:\Users\User\PycharmProjects\xml\out_oks\out.xlsx', encoding='utf-16')
    now2 = datetime.datetime.now()
    now3 = now2 - now1
#    print(now3)
#    print(df_1)
    return df_1

#read_oks()


