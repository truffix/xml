import pandas as pd
import xlrd
import numpy as np




df = pd.read_csv(r'out/out.csv',encoding='utf-16',header=0)
df = df.drop(columns=df.columns [0])
df.rename(columns = {'Кадастровый номер':'К№ земельного участка'}, inplace = True )
#print (df['Площадь'])
#df['Площадь'].info()
df['Площадь'].apply(lambda x: x.replace(',', '.'))
#df['Площадь'].astype('float')
#print (df['Площадь'].info())


df_1 = pd.read_excel(r'out/Сводная таблица (22_27_011601).xls')

#df_1['S по докум (кв.м.)'].apply(lambda x: x.replace('.', '')).astype('float')
#print (df['S по докум (кв.м.)'].info())

res = df_1.merge(df, on=["К№ земельного участка"])
res = res[['№ п/п',
           'К№ земельного участка',
           'Вид объекта',
           'Вид ОН',
           'Адрес_x',
           'Адрес_y',
           'Адрес правообладателя',
           'Статус объекта:',
           'Уточнение границ, исправление РО (нужное выбрать)',
           'S по докум (кв.м.)',
           'Площадь',
           'S фактическая (по реультатам съемки) (кв.м.)',
           'разница (кв.м.)',
           'ВРИ_x',
           'ВРИ_y',
           'К№ ОКС',
           'ОКС',
           'Статус ОКС',
           'Вид права_x',
           'Вид права_y',
           'ФИО ',
           'ФИО собственников',
           'Примечания',
           'Специальные отметки',
           'Имя файла',
           'Кад номера смежников',
           'Адрес правообла-я смежного ЗУ', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21']]




res["Вид права_y"] = res["Вид права_y"].str.replace("[", "")
res["Вид права_y"] = res["Вид права_y"].str.replace("'", "")
res["Вид права_y"] = res["Вид права_y"].str.replace("]", "")
res["ФИО собственников"] = res["ФИО собственников"].str.replace("[", "")
res["ФИО собственников"] = res["ФИО собственников"].str.replace("'", "")
res["ФИО собственников"] = res["ФИО собственников"].str.replace("]", "")
res["Кад номера смежников"] = res["Кад номера смежников"].str.replace("[", "")
res["Кад номера смежников"] = res["Кад номера смежников"].str.replace("'", "")
res["Кад номера смежников"] = res["Кад номера смежников"].str.replace("]", "")

res["Площадь"] = res["Площадь"].str.replace(" ", "")

#df['S по докум (кв.м.)'] = df['S по докум (кв.м.)'].str.replace('\n', '')

#
#print(list(df))
#print (list(df_1))


print (list(res))
print(res.dtypes)
res.to_excel(r'C:\Users\User\PycharmProjects\xml\out\res.xlsx',  encoding='utf-16')





