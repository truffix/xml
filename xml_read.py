from bs4 import BeautifulSoup
import requests
import pandas as pd
import xml.etree.cElementTree as ET
import codecs
from pathlib import Path
import os
import datetime


list_cadastr = []
list_file_name = []
list_create = []
list_oks = []
list_vid_on = []
list_vri = []
list_area = []
list_address = []
list_cad_numb = []
list_special_notes = []
list_right_records = []
list_right_owner = []
list_mail_address = []




def read():

    os.chdir(r"C:\Users\User\PycharmProjects\xml\pack")
    now1 = datetime.datetime.now()
    for item in Path('.').glob('*'):
        if item.is_file():
            file = codecs.open(str(item),
                           "r", "utf-8")
            file_path = os.path.abspath(str(item))
            file_name = os.path.basename(file_path)
            data = file.read()

            BS_data = BeautifulSoup(data, "xml")  # собираем кадастровые номера

            b_unique = BS_data.find('object')
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

                BS_data = BeautifulSoup(data, "xml")  # собираем кадастровые номера

                b_unique = BS_data.find('cad_links')
                b_unique = b_unique.find('cad_number')
                b_unique = b_unique.text
                list_oks.append(b_unique)
        except:
            b_unique = " "
            list_oks.append(b_unique)

# собираем Вид ОН
        try:
            if item.is_file():
                file = codecs.open(str(item),
                           "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('object')
                b_unique = b_unique.find('common_data')
                b_unique = b_unique.find('value')
                b_unique = b_unique.text
                list_vid_on.append(b_unique)
        except:
            b_unique = " "
            list_vid_on.append(b_unique)

# собираем ВРИ

        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('land_record')
                b_unique = b_unique.find('params')
                b_unique = b_unique.find('permitted_use')
                b_unique = b_unique.find('by_document')
                list_vri.append(b_unique)
        except:
            b_unique = " "
            list_vri.append(b_unique)


# собираем Площади
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('land_record')
                b_unique = b_unique.find('params')
                b_unique = b_unique.find('area')
                b_unique = b_unique.find_all('value')
                b_unique = b_unique[-1]
                list_area.append(b_unique)
        except:
            b_unique = " "
            list_area.append(b_unique)

# собираем Адрес
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('land_record')
                b_unique = b_unique.find('address_location')
                b_unique = b_unique.find('readable_address')
                b_unique = b_unique.text
                list_address.append(b_unique)
        except:
            b_unique = " "
            list_address.append(b_unique)

# собираем кад номера смежников
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('cadastral_numb_adjacent_parcel')
                b_unique = b_unique.find('cad_number')
                b_unique = b_unique.text
                list_cad_numb.append(b_unique)
        except:
            b_unique = " "
            list_cad_numb.append(b_unique)

# собираем специальные заметки
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('special_notes')
                b_unique = b_unique.text
                list_special_notes.append(b_unique)
        except:
            b_unique = " "
            list_special_notes.append(b_unique)

# собираем собственность
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('right_records')
                b_unique = b_unique.find('value')
                b_unique = b_unique.text
                list_right_records.append(b_unique)
        except:
            b_unique = " "
            list_right_records.append(b_unique)

# собираем ФИО собственников
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('right_holders')
                b_unique = b_unique.text

                result = b_unique[0]
                for letter in b_unique[1:]:
                    if letter.isupper():
                        result += f' {letter}'
                    else:
                        result += letter

                list_right_owner.append(result)
        except:
            b_unique = " "
            list_right_owner.append(b_unique)

# собираем Адреса для почты
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                       "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")

                b_unique = BS_data.find('holders_related_lands')
                b_unique = b_unique.text

                result = b_unique[0]
                for letter in b_unique[1:]:
                    if letter.isupper():
                        result += f' {letter}'
                    else:
                        result += letter

                list_mail_address.append(result)
        except:
            b_unique = " "
            list_mail_address.append(b_unique)


    df_1 = pd.DataFrame( {'Имя файла':list_file_name,'Кадастровый номер':list_cadastr,'ОКС':list_oks, 'Вид ОН':list_vid_on, 'ВРИ':list_vri, 'Площадь':list_area, 'Адрес':list_address, 'Кад номера смежников':list_cad_numb, 'Специальные отметки':list_special_notes, 'Вид права':list_right_records, 'ФИО собственников':list_right_owner, 'Адрес правообла-я смежного ЗУ':list_mail_address})
#    print (len(list_file_name),len(list_cadastr), len(list_oks),len(list_vid_on),len(list_vri),len(list_area))
    print(df_1)
#    now2 = datetime.datetime.now()
#    now3 = now2 - now1
#    print(now3)
#    print(df_1)
#    df_1.to_csv('out.csv')
    return df_1

read()