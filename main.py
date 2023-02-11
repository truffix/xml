from exct_xml_oks import del_zip
from exct_xml_oks import del_pdf
from exct_xml_oks import del_sig
from exct_xml_oks import unpack_all_in_dir
from xml_read_oks import read_oks
import os
import datetime

print("Введите полный путь к папке с архивами выписок")
base_dir = input()
base_dir.replace("\"", "\\")
os.chdir(base_dir)  # change directory from working dir to dir with files

print("Удалять архивы? (Да/Нет)")
zip_del = input()
print("Удалять файлы подписи? (Да/Нет)")
sig_del = input()
print("Удалять пдф? (Да/Нет)")
pdf_del = input()

now1 = datetime.datetime.now()
print(unpack_all_in_dir(base_dir))

if zip_del == "да" or zip_del == "Да":
    print(del_zip(base_dir))

if sig_del == "да" or sig_del == "Да":
    print(del_sig(base_dir))

if pdf_del == "да" or pdf_del == "Да":
    print(del_pdf(base_dir))
now2 = datetime.datetime.now()


print("Прочитать выписки? (Да/Нет)")
read_oks_1 = input()
if read_oks_1 == "да" or read_oks_1 == "Да":
    df = read_oks(base_dir)
now3 = datetime.datetime.now()


print("Введите полный путь папки выгрузки результата")
puti = input()
print("Название файла")
name_res = input()
resol = ".xlsx"

full_puti = os.path.join(puti, name_res)
joint_puti = full_puti+resol

df.to_excel(joint_puti)