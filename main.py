import exct_xml
import xml_read
import datetime

now1 = datetime.datetime.now()

base_dir = r'C:\Users\User\PycharmProjects\xml\pack'
exct_dir = r'C:\Users\User\PycharmProjects\xml\pack\exct'
exct_xml.exct_xml(base_dir)
#list_rar = exct_xml.exct_xml(base_dir)
#print (list_rar)



df = xml_read.read()
#df.insert(loc=0, column='Имя zip', value=list_rar)\
print (df)
df.to_csv(r'C:\Users\User\PycharmProjects\xml\out\out.csv',  encoding='utf-16')


now2 = datetime.datetime.now()
now3 = now2 - now1
print(now3)