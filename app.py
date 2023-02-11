# from exct_xml_oks import del_zip
from exct_xml_oks import del_pdf
from exct_xml_oks import del_sig
from exct_xml_oks import unpack_all_in_dir
# from xml_read_oks import read_oks
import os
import datetime
from pathlib import Path
import time

from bs4 import BeautifulSoup
import pandas as pd
import codecs
import datetime

import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Выгрузка данных ОКС")
        self.geometry(f"{700}x{310}")
        self.resizable(False, False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(5, weight=1)

        # self.sidebar_frame1 = customtkinter.CTkFrame(self, width=0, corner_radius=0)
        # self.sidebar_frame1.grid(row=0, column=2, rowspan=4, sticky="nsew")
        # self.sidebar_frame1.grid_rowconfigure(2, weight=0)
        self.iconbitmap(r'C:\Users\User\PycharmProjects\xml\oks\9957d6a37c0ccdd4085cf7a739e7ca14.ico')
        #
        # scrollb = ttk.Scrollbar(self, command=self.textbox.yview)
        # scrollb.grid(row=0, column=3, sticky='nsew')
        # self.textbox['yscrollcommand'] = scrollb.set

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, height=290)
        self.scrollable_frame.grid(row=0, column=2,rowspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(2, weight=1)

        self.textbox = customtkinter.CTkTextbox(self.scrollable_frame, width=465, height=300,activate_scrollbars="true")
        self.textbox.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        # self.textbox.insert("0.0", "...Ход выполнения...\n\n\n\n")




        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=0, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ООО Геосфера", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Путь к архивам", command=self.open_input_dialog_event_arch)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Путь к выгрузке", command=self.open_output_dialog_event_exct)
        self.sidebar_button_2.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Обработать", command=self.engien, font = customtkinter.CTkFont(size=14,weight="bold"))
        self.sidebar_button_3.grid(row=6, column=0, padx=20, pady=10)




        # create checkbox and switch frame
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.sidebar_frame, onvalue=1, offvalue=0, text="Удалять архивы",command=self.sidebar_button_event_acrh)
        # self.checkbox_1.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="nsew")
        # print (self.checkbox_1.get())
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.sidebar_frame,onvalue=1, offvalue=0, text="Удалять файлы подписи",command=self.sidebar_button_event_sig)
        self.checkbox_2.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="nsew")
        print(self.checkbox_2.get())
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.sidebar_frame,onvalue=1, offvalue=0, text="Удалять пдф",command=self.sidebar_button_event_pdf)
        self.checkbox_3.grid(row=4, column=0, pady=20, padx=20, sticky="nsew")
        print(self.checkbox_3.get())


    def open_input_dialog_event_arch(self):
        self.dialog = tkinter.filedialog.askdirectory()
        self.base_dir = self.dialog
        print("Путь Архивов:", self.base_dir)
        self.base_dir.replace("\"", "\\")
        os.chdir(self.base_dir)
        self.textbox.insert("1.0","Папка с архивами:"+self.base_dir+"\n")
        os.chdir(self.base_dir)
        now1 = datetime.datetime.now()
        s = []
        for item in Path('.').glob('*'):
            file_path = os.path.abspath(str(item))
            if file_path.endswith('.zip'):
                s.append(1)
        self.textbox.insert("0.0", "Ищу zip файлы...:\n")
        time.sleep(0)
        s_s = str(sum(s))
        self.textbox.insert("0.0", "Найдено "+s_s+" zip файлов:\n")
        return self.base_dir

    def open_output_dialog_event_exct(self):
        self.exct = tkinter.filedialog.asksaveasfilename(filetypes=(
                    ("Excel files", "*.xlsx"),
                    ("All files", "*.*")))
        self.exct.replace("\"", "\\")
        print("Путь файла результата:", self.exct+".xlsx")
        self.textbox.insert("0.0","Путь файла результата:" + self.exct+".xlsx"+"\n")

        return self.exct



    # def sidebar_button_event_acrh(self):
    #     self.checkbox_1.get()
    #     print (self.checkbox_1.get())
    #     return self.checkbox_1.get()

    def sidebar_button_event_sig(self):
        self.checkbox_2.get()
        print (self.checkbox_2.get())
        if self.checkbox_2.get() == 1:
            self.textbox.insert("0.0","Опция удаления файлов подписи - Включена\n")
        elif self.checkbox_2.get() == 0:
            self.textbox.insert("0.0","Опция удаления файлов подписи - Выключна\n")
        return self.checkbox_2.get()

    def sidebar_button_event_pdf(self):
        self.checkbox_3.get()
        print (self.checkbox_3.get())
        if self.checkbox_3.get() == 1:
            self.textbox.insert("0.0","Опция удаления файлов пдф - Включена\n")
        elif self.checkbox_3.get() == 0:
            self.textbox.insert("0.0","Опция удаления файлов пдф - Выключна\n")
        return self.checkbox_3.get()

    def engien (self):
        self.base_dir
        self.textbox.insert("0.0","Выполняется...\n")
        print(unpack_all_in_dir(self.base_dir))
        self.textbox.insert("0.0", unpack_all_in_dir(self.base_dir)+"\n")
#        if self.checkbox_1.get() == 1:
 #           print(del_sig(self.base_dir))

        if self.checkbox_2.get() == 1:
            print(del_sig(self.base_dir))
            self.textbox.insert("0.0", del_sig(self.base_dir) + "\n")
        if self.checkbox_3.get() == 1:
            print(del_pdf(self.base_dir))
            self.textbox.insert("0.0", del_pdf(self.base_dir) + "\n")

        list_oks = []
        list_cadastr = []
        list_file_name = []
        list_nazn = []
        list_name = []
        list_addres = []
        extension = ".xml"


        os.chdir(self.base_dir)
        now1 = datetime.datetime.now()
        poi = []
        for item in Path('.').glob('*'):
            file_path = os.path.abspath(str(item))
            if file_path.endswith('.xml'):
                poi.append(1)

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
                path = Path(self.base_dir)
                d = d + 1
                # print(file_path, "--", d, "/", sum(s))
                eee_poi = sum(poi)
                eee_poi = str(eee_poi)
                er=str(d)
#                print(file_path+"--"+d+"/"+eee_poi)
                self.textbox.insert("0.0", file_path+"--"+er+"/"+eee_poi+"\n")

            df_1 = pd.DataFrame({'Имя файла': list_file_name, 'Кадастровый номер': list_cadastr, 'ОКС': list_oks,
                                 'Назначение': list_nazn, 'Наименование': list_name, 'Адрес': list_addres})
            # df_1.to_excel(r'C:\Users\User\PycharmProjects\xml\out_oks\out.xlsx', encoding='utf-16')
        # now2 = datetime.datetime.now()
        # now3 = now2 - now1
        #    print(now3)
        #    print(df_1)


            df_1.to_excel(self.exct+".xlsx")











        self.textbox.insert("0.0","Готово!\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()





# print("Введите полный путь к папке с архивами выписок")
# base_dir = input()
# base_dir.replace("\"", "\\")
# os.chdir(base_dir)  # change directory from working dir to dir with files
#
# print("Удалять архивы? (Да/Нет)")
# zip_del = input()
# print("Удалять файлы подписи? (Да/Нет)")
# sig_del = input()
# print("Удалять пдф? (Да/Нет)")
# pdf_del = input()
#
# now1 = datetime.datetime.now()
# print(unpack_all_in_dir(base_dir))
#
# if zip_del == "да" or zip_del == "Да":
#     print(del_zip(base_dir))
#
# if sig_del == "да" or sig_del == "Да":
#     print(del_sig(base_dir))
#
# if pdf_del == "да" or pdf_del == "Да":
#     print(del_pdf(base_dir))
# now2 = datetime.datetime.now()
#
#
# print("Прочитать выписки? (Да/Нет)")
# read_oks_1 = input()
# if read_oks_1 == "да" or read_oks_1 == "Да":
#     df = read_oks(base_dir)
# now3 = datetime.datetime.now()
#
#
# print("Введите полный путь папки выгрузки результата")
# puti = input()
# print("Название файла")
# name_res = input()
# resol = ".xlsx"
#
# full_puti = os.path.join(puti, name_res)
# joint_puti = full_puti+resol
#
# df.to_excel(joint_puti)