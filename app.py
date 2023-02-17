from exct_xml_oks import del_pdf
from exct_xml_oks import del_sig
from exct_xml_oks import unpack_all_in_dir
import os
from pathlib import Path
import time
import re
from bs4 import BeautifulSoup
import pandas as pd
import codecs
import datetime
import tkinter
import tkinter.messagebox
import customtkinter
import threading


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Выгрузка данных выписок")
        self.geometry(f"{700}x{400}")
        self.resizable(False, False)


        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(7, weight=1)


        self.iconbitmap(r'9957d6a37c0ccdd4085cf7a739e7ca14.ico')


        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, height=370)
        self.scrollable_frame.grid(row=0, column=2,rowspan=2, padx=(5, 0), pady=(5, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(2, weight=1)

        self.textbox = customtkinter.CTkTextbox(self.scrollable_frame, width=465, height=380,activate_scrollbars="true")
        self.textbox.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")



        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=0, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ООО Геосфера", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Путь к архивам", command=self.open_input_dialog_event_arch)
        self.sidebar_button_1.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Путь к выгрузке", command=self.open_output_dialog_event_exct)
        self.sidebar_button_2.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Обработать", command=self.start_action, font = customtkinter.CTkFont(size=14,weight="bold"))
        self.sidebar_button_3.grid(row=8, column=0, padx=20, pady=10)

        self.radio_var = tkinter.IntVar(value=1)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.sidebar_frame, text="Выписки ОКС",command=self.sidebar_button_event_oks_zy, variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.sidebar_frame, text="Выписки ЗУ",command=self.sidebar_button_event_oks_zy, variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")



        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.sidebar_frame,onvalue=1, offvalue=0, text="Удалять файлы подписи",command=self.sidebar_button_event_sig)
        self.checkbox_2.grid(row=5, column=0, pady=(20, 0), padx=20, sticky="nsew")
        print(self.checkbox_2.get())
        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.sidebar_frame,onvalue=1, offvalue=0, text="Удалять пдф",command=self.sidebar_button_event_pdf)
        self.checkbox_3.grid(row=6, column=0, pady=20, padx=20, sticky="nsew")
        print(self.checkbox_3.get())


    def open_input_dialog_event_arch(self):
        self.dialog = tkinter.filedialog.askdirectory()
        self.base_dir = self.dialog
        print("Путь Архивов:", self.base_dir)
        self.base_dir.replace("\"", "\\")
        os.chdir(self.base_dir)
        self.textbox.insert("1.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Папка с архивами:"+self.base_dir+"\n")
        os.chdir(self.base_dir)
        now1 = datetime.datetime.now()
        s = []
        for item in Path('.').glob('*'):
            file_path = os.path.abspath(str(item))
            if file_path.endswith('.zip'):
                s.append(1)
        self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Ищу zip файлы...:\n")
        time.sleep(0)
        s_s = str(sum(s))
        self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Найдено "+s_s+" zip файлов:\n")
        return self.base_dir

    def open_output_dialog_event_exct(self):
        self.exct = tkinter.filedialog.asksaveasfilename(filetypes=(
                    ("Excel files", "*.xlsx"),
                    ("All files", "*.*")))
        self.exct.replace("\"", "\\")
        print("Путь файла результата:", self.exct+".xlsx")
        self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Путь файла результата:" + self.exct+".xlsx"+"\n")

        return self.exct



    # def sidebar_button_event_acrh(self):
    #     self.checkbox_1.get()
    #     print (self.checkbox_1.get())
    #     return self.checkbox_1.get()

    def sidebar_button_event_sig(self):
        self.checkbox_2.get()
        print (self.checkbox_2.get())
        if self.checkbox_2.get() == 1:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Опция удаления файлов подписи - Включена\n")
        elif self.checkbox_2.get() == 0:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Опция удаления файлов подписи - Выключна\n")
        return self.checkbox_2.get()

    def sidebar_button_event_pdf(self):
        self.checkbox_3.get()
        print (self.checkbox_3.get())
        if self.checkbox_3.get() == 1:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Опция удаления файлов пдф - Включена\n")
        elif self.checkbox_3.get() == 0:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Опция удаления файлов пдф - Выключна\n")
        return self.checkbox_3.get()

    def sidebar_button_event_oks_zy(self):
        self.radio_var.get()

        print (self.radio_var.get())
        if self.radio_var.get() == 1:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Выбрана обработка выписок ЗУ\n")
        elif self.radio_var.get() == 0:
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Выбрана обработка выписок ОКС\n")
        return self.radio_var.get()

    def start_action(self):

        thread = threading.Thread(target=self.engien)
        print(threading.main_thread().name)
        print(thread.name)
        thread.start()



    def engien (self):
        # выгрузка ОКС
        if self.radio_var.get() == 0:
            self.base_dir
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Выполняется...\n")
            print(unpack_all_in_dir(self.base_dir))
            self.textbox.insert("0.0", unpack_all_in_dir(self.base_dir)+"\n")

            if self.checkbox_2.get() == 1:
                print(del_sig(self.base_dir))
                self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" -"+del_sig(self.base_dir) + "\n")
            if self.checkbox_3.get() == 1:
                print(del_pdf(self.base_dir))
                self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" -"+del_pdf(self.base_dir) + "\n")

            list_oks = []
            list_cadastr = []
            list_file_name = []
            list_nazn = []
            list_name = []
            list_addres = []
            extension = ".xml"


            os.chdir(self.base_dir)
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
                    self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - "+ file_path+"--"+er+"/"+eee_poi+"\n")

                df_1 = pd.DataFrame({'Имя файла': list_file_name, 'Кадастровый номер': list_cadastr, 'ОКС': list_oks,
                                     'Назначение': list_nazn, 'Наименование': list_name, 'Адрес': list_addres})

                df_1.to_excel(self.exct+".xlsx")

            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Готово!\n")



        #выгрузка ЗУ
        elif self.radio_var.get() == 1:
            self.base_dir
            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Выполняется...\n")
            print(unpack_all_in_dir(self.base_dir))
            self.textbox.insert("0.0", unpack_all_in_dir(self.base_dir) + "\n")
            #        if self.checkbox_1.get() == 1:
            #           print(del_sig(self.base_dir))

            if self.checkbox_2.get() == 1:
                print(del_sig(self.base_dir))
                self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" -"+del_sig(self.base_dir) + "\n")
            if self.checkbox_3.get() == 1:
                print(del_pdf(self.base_dir))
                self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" -"+del_pdf(self.base_dir) + "\n")
            time.sleep(2)
            list_cadastr = []
            list_file_name = []
            list_oks = []
            list_vid_on = []
            list_vri = []
            list_area = []
            list_address = []
            list_cad_numb = []
            list_address_smej = []
            list_special_notes = []
            list_right_records = []
            list_right_owner = []
            list_mail_address = []
            extension = ".xml"

            os.chdir(self.base_dir)
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

                        b_unique = BS_data.find('object')
                        b_unique = b_unique.find('cad_number')
                        b_unique = b_unique.text
                        list_cadastr.append(b_unique)
                        list_file_name.append(file_name)

                    # собираем ОКСы
                    try:
                        b_unique = BS_data.find('cad_links')
                        b_unique = b_unique.find_all('included_object')

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

                    # собираем Вид ОН
                    try:
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
                        b_unique = BS_data.find('land_record')
                        b_unique = b_unique.find('params')
                        b_unique = b_unique.find('permitted_use')
                        b_unique = b_unique.find('by_document')
                        b_unique = b_unique.text
                        list_vri.append(b_unique)
                    except:
                        b_unique = " "
                        list_vri.append(b_unique)

                    # собираем Площади
                    try:
                        b_unique = BS_data.find('land_record')
                        b_unique = b_unique.find('params')
                        b_unique = b_unique.find('area')
                        b_unique = b_unique.find_all('value')
                        b_unique = b_unique[-1]
                        b_unique = b_unique.getText()
                        result = b_unique[0]
                        for letter in b_unique[1:]:
                            if letter.isupper():
                                result += f' {letter}'
                            else:
                                result += letter
                        result = float(result)
                        list_area.append(result)
                    except:
                        b_unique = "0"
                        b_unique = float(b_unique)
                        list_area.append(b_unique)

                    # собираем Адрес
                    try:
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
                        b_unique = BS_data.find('borders')
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

                        list_cad_numb.append(b_unique1)
                    except:
                        b_unique = " "
                        list_cad_numb.append(b_unique)

                    # собираем адреса смежников
                    try:
                        b_unique = BS_data.find('borders')
                        b_unique = b_unique.find_all('mailing_addess')
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

                        list_address_smej.append(b_unique1)
                    except:
                        b_unique = " "
                        list_address_smej.append(b_unique)

                    # собираем специальные заметки
                    try:
                        b_unique = BS_data.find('special_notes')
                        b_unique = b_unique.text
                        list_special_notes.append(b_unique)
                    except:
                        b_unique = " "
                        list_special_notes.append(b_unique)

                    # собираем собственность
                    try:
                        b_unique = BS_data.find_all('right_type')

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

                        list_right_records.append(b_unique1)
                    except:
                        b_unique = " "
                        list_right_records.append(b_unique)

                    # собираем ФИО собственников
                    try:
                        b_unique = BS_data.find('right_records')
                        b_unique = b_unique.find_all('right_holders')
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

                        list_right_owner.append(b_unique1)
                    except:
                        b_unique = " "
                        list_right_owner.append(b_unique)

                    # собираем Адреса для почты
                    try:
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
                    path = Path(self.base_dir)
                    d = d + 1
                    # print(file_path, "--", d, "/", sum(s))
                    eee_poi = sum(poi)
                    eee_poi = str(eee_poi)
                    er = str(d)
                    #                print(file_path+"--"+d+"/"+eee_poi)
                    self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - "+file_path + "--" + er + "/" + eee_poi + "\n")

                df_1 = pd.DataFrame( {'Имя файла':list_file_name,'Кадастровый номер':list_cadastr,'ОКС':list_oks, 'Вид ОН':list_vid_on, 'ВРИ':list_vri, 'Площадь':list_area, 'Адрес':list_address, 'Кад номера смежников':list_cad_numb, 'Адреса смежников':list_address_smej, 'Специальные отметки':list_special_notes, 'Вид права':list_right_records, 'ФИО собственников':list_right_owner})

                df_1.to_excel(self.exct + ".xlsx")

            self.textbox.insert("0.0",str(datetime.datetime.now().strftime("%H:%M:%S"))+" - Готово!\n")
            os.startfile(self.exct+".xlsx")


if __name__ == "__main__":
    app = App()
    app.mainloop()
