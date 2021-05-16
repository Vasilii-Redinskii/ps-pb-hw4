#Функция словаря с ранжированием по максимальным значениям
def get_max_val (data_dict, item_name):
    
    item_dict = defaultdict(int) # Создаем словарь с заранее заданным типом значений
    for element in data_dict:
        # Добавляем элемент в словарь item_dict
        # element[item_name] - название поля вычисления
        # Если ключа с таким названием в item_dict нет, то будет значение 0,
        # таким образом мы просто увеличим его на 1  
        item_dict[element[item_name]] += 1
    item_counter = Counter(item_dict)
    return item_counter

# Импортируем библиотеку pandas
import pandas
from openpyxl import load_workbook
from collections import defaultdict, Counter


# Читаем файл ексль и результат передаем в переменную excel_data
# Переменная excel_data имеет тип <class 'pandas.core.frame.DataFrame'>
excel_data = pandas.read_excel('logs.xlsx', sheet_name='log')

# Преобразуем переменную excel_data в список словарей с помощью метода to_dict()
# Результат передаем в переменную excel_data_dict
excel_data_dict = excel_data.to_dict(orient='records')
# Получаем список браузеров по популярности
browser_counter = get_max_val(excel_data_dict, 'Браузер')
# Преобразуем переменную excel_data в DataFrame
df = pandas.DataFrame(excel_data) 

#datatypes = df.dtypes  опреденение типа столбца

# Групперуем посещения по браузерам и месяцам
browser_by_month=df.groupby(['Браузер', pandas.Grouper(key='Дата посещения', freq='M')])['Браузер'].count()
# Создаем список месяцев 
month_series=['2020-01-31','2020-02-29','2020-03-31','2020-04-30','2020-05-31','2020-06-30','2020-07-31','2020-08-31','2020-09-30','2020-10-31','2020-11-30','2020-12-31']
#Проверочная печать
print(browser_by_month.get(key = 'Яндекс: мобильное приложение'))
print(month_series)


#Открытие ексель файла для записи
filename ='report.xlsx'
wb = load_workbook(filename)
sheet = wb['Лист1']
#Запись данных в ексель файл
for i in range (7):
    sheet.cell(row=i+5, column=1).value = browser_counter.most_common(7)[i][0]
    sheet.cell(row=i+5, column=15).value = browser_counter.most_common(7)[i][1]
    for j in range(12):
        sheet.cell(row=i+5, column=j+3).value = browser_by_month.get(key = browser_counter.most_common(7)[i][0]).get(key = month_series[j])
wb.save(filename)

