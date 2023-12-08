from table import Cell, CellAlignStyle, Row, Table, TableStyle

#testtable = Table()
#print(testtable)
#testtable.addrow(["One", "Two"])
#print(testtable)

table = [
    ['Имя', 'Возраст', 'Рост', 'Вес', 'Профессия'],

]

testtable = Table(['Имя', 'Возраст', 'Рост', 'Вес', 'Профессия'], [    ['Алекс', 25, 180, 75, 'Врач'],
    ['Анна', 30, 165, 60, 'Учитель'],
    ['Марк', 42, 175, 80, 'Инженер'],
    ['Елена', 38, 170, 65, 'Менеджер'],
    ['Иван', 50, 190, 90, 'Художник'],
    ['Мария', 27, 160, 55, 'Студент'],
    ['Денис', 35, 175, 70, 'Программист'],
    ['Ольга', 45, 165, 68, 'Бухгалтер'],
    ['Макс', 33, 180, 75, 'Дизайнер'],
    ['Алиса', 28, 170, 62, 'Фотограф']], style=TableStyle.GRID)

print(testtable)


testtable = Table(['One', 'Two', 123], style=TableStyle.DOTTED)
testtable.header[0].set_maxlen(6)
row = testtable.addrow(['34523523452',None,'АБВГД'])
row = testtable.addrow(['34523523452',459709367957609346,'АБВГД'])
row = testtable.addrow(['34523523452',None,'АБВГД'])

row[0].align = CellAlignStyle.RIGHT_TOP
row[0].indenttext = '*'
row[0].indent = 5


tablelist = []
for style in TableStyle:
    testtable.style = style
    print(f'STYLE: {style.name}')
    tablelist.append(str(testtable))
    print(testtable)

testtable2 = Table(['One', 'Two', 123], style=TableStyle.ROUNDED_GRID)
row = testtable2.addrow(['1',None,'2'])
row = testtable.addrow([testtable2,None,''])
row[0].height = 0
testtable.header[0].set_maxlen(0)

print(testtable)
testtable.header[0].set_maxlen(15)
testtable.addrow(['','',''])
print(testtable)
testtable.header[0].set_maxlen(3)
testtable.addrow(['','3452352',''])
print(testtable)
print(testtable)
testtable.addrow(['','34523523452',''],  indent = 5, indenttext = '*')
print(testtable)

testtable2 = Table(['One', 'Two', 123], style='fancy_grid')
testtable.addrow([testtable2,'34523523452',''],  indent = 5, indenttext = '*')



