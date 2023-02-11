import zipfile
import os
from pathlib import Path
import bs4
import requests
import pandas as pd

rar_names =[]



#base_dir = r'C:\Users\User\PycharmProjects\xml\pack_oks'  # absolute path to the data folder
extension = ".zip"
extension_sig = ".sig"
extension_pdf = ".pdf"




def unpack_all_in_dir(_dir):
    i = 0
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            rar_path = os.path.abspath(item)
            rar_name = os.path.basename(rar_path)
            rar_names.append(rar_name)
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(_dir)  # extract file to dir
            zip_ref.close()  # close file

        elif os.path.isdir(abs_path):
            unpack_all_in_dir(abs_path)


        # recurse this function with inner folder
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(_dir)  # extract file to dir
            zip_ref.close()  # close file

        elif os.path.isdir(abs_path):
            unpack_all_in_dir(abs_path)  # recurse this function with inner folder

        i+=1
        print(Path(abs_path).name, i)

    return '\nАрхивы распакованы'



def del_sig (_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension_sig):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            os.remove(file_name)


    return '\nУдалены файлы подписи'


def del_pdf(_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension_pdf):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            os.remove(file_name)

    return '\nУдалены файлы пдф'

def del_zip(_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            os.remove(file_name)

    return '\nУдалены файлы архивов'


#def exct_xml(base_dir):
#    unpack_all_in_dir(base_dir)
#    del_sig(base_dir)
#    del_pdf(base_dir)



#unpack_all_in_dir(base_dir)








