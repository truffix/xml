from bs4 import BeautifulSoup
import requests
import pandas as pd
import xml.etree.cElementTree as ET
import codecs
from pathlib import Path
import os
import datetime
import re


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
        try:
            if item.is_file():
                file = codecs.open(str(item),
                                   "r", "utf-8")
                file_path = os.path.abspath(str(item))
                file_name = os.path.basename(file_path)
                data = file.read()

                BS_data = BeautifulSoup(data, "xml")  # собираем кадастровые номера

                b_unique = BS_data.find_all('right_type')
#                b_unique = b_unique.find('value')
                b_unique1 = []
                for i in range(len(b_unique)):
                    b_unique2 = b_unique[i].get_text()
                    result = b_unique2[0]
                    for letter in b_unique2[1:]:
                        if letter.isupper():
                            result += f' {letter}'
                        else:
                            result += letter
                    b_unique2 = re.sub(r'[^\w\s]+|[\d]+', r'', b_unique2).strip()
                    b_unique1.append(b_unique2)

#                b_unique = b_unique.replace("<", "")
#                b_unique = b_unique.find_all('surname')
#                b_unique = b_unique.text
#                value = b_unique[1].getText()




                list_cad_numb.append(b_unique1)
        except:
            b_unique = " "
            list_cad_numb.append(b_unique)

    print(list_cad_numb)

read()

