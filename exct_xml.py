import zipfile
import os
import bs4
import requests
import pandas as pd

rar_names =[]

base_dir = r'C:\Users\User\PycharmProjects\xml\pack'  # absolute path to the data folder
extension = ".zip"
extension_sig = ".sig"
extension_pdf = ".pdf"

os.chdir(base_dir)  # change directory from working dir to dir with files


def unpack_all_in_dir(_dir):
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
            os.remove(file_name)  # delete zipped file
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
            os.remove(file_name)  # delete zipped file
        elif os.path.isdir(abs_path):
            unpack_all_in_dir(abs_path)  # recurse this function with inner folder

    return (rar_names)



def del_sig (_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension_sig):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            os.remove(file_name)

def del_pdf(_dir):
    for item in os.listdir(_dir):  # loop through items in dir
        abs_path = os.path.join(_dir, item)  # absolute path of dir or file
        if item.endswith(extension_pdf):  # check for ".zip" extension
            file_name = os.path.abspath(abs_path)  # get full path of file
            os.remove(file_name)

def exct_xml(base_dir):
    unpack_all_in_dir(base_dir)
#    list = unpack_all_in_dir(base_dir)
    del_sig(base_dir)
    del_pdf(base_dir)
    return list


#def list_rar ():
#    list_rar = (unpack_all_in_dir(base_dir))
#    return list_rar

exct_xml(base_dir)
#list_rar()






