def item_c(st):
    item_cost = 0
    item_name = ''
    list_log = st.split(';')
    for element in list_log:
        part = element.split(':')
        if part[0] == 'item':
            item_name = part[1]
        if part[0] == 'item_cost':
            item_cost = int(part[1])
    return item_cost, item_name


log = """name:Иван;gender:m;item:Часы;item_cost:9800
name:Иван;gender:m;item:Фитнес-браслет;item_cost:12300
name:Иван;gender:m;item:Кофемашина;item_cost:23500
name:Петр;gender:m;item:Часы;item_cost:9800
name:Петр;gender:m;item:Фитнес-браслет;item_cost:12300
name:Петр;gender:m;item:Айфон;item_cost:77900
name:Петр;gender:m;item:Чехол для телефона;item_cost:350
name:Петр;gender:m;item:Кофемашина;item_cost:23500
name:Дарья;gender:m;item:Айфон;item_cost:77900
name:Марья;gender:m;item:Кофемашина;item_cost:23500
name:Юлия;gender:m;item:Фитнес-браслет;item_cost:12300"""

list_log = log.split('\n')
for line in list_log:
    item = item_c(line)
    if item[0] < 13000:
        print(item[1])
        