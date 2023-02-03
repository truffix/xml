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

    print(len(list_mail_address))

read()

