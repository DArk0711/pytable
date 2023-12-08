import textwrap
from collections import namedtuple
import enum

Line = namedtuple("Line", ["begin", "hline", "sep", "end"])
DataRow = namedtuple("DataRow", ["begin", "sep", "end"])                   
# Предполагается, что структура таблицы должна быть:
#
#     --- lineabove ---------
#         headerrow
#     --- linebelowheader ---
#         datarow
#     --- linebetweenrows ---
#     ... (строки данных) ...
#     --- linebetweenrows ---
#         last datarow
#     --- linebelow ---------
#
TableFormat = namedtuple(
    "TableFormat",
    [
        "lineabove",
        "linebelowheader",
        "linebetweenrows",
        "linebelow",
        "headerrow",
        "datarow",
    ],
)

class TableStyle(enum.Enum):
    SIMPLE = TableFormat(
        lineabove=Line("", "-", "  ", ""),
        linebelowheader=Line("", "-", "  ", ""),
        linebetweenrows=None,
        linebelow=Line("", "-", "  ", ""),
        headerrow=DataRow("", "  ", ""),
        datarow=DataRow("", "  ", ""))
    PLAIN = TableFormat(
        lineabove=None,
        linebelowheader=None,
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("", "  ", ""),
        datarow=DataRow("", "  ", ""))
    GRID = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("+", "=", "+", "+"),
        linebetweenrows=Line("+", "-", "+", "+"),
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    SIMPLE_GRID = TableFormat(
        lineabove=Line("┌", "─", "┬", "┐"),
        linebelowheader=Line("├", "─", "┼", "┤"),
        linebetweenrows=Line("├", "─", "┼", "┤"),
        linebelow=Line("└", "─", "┴", "┘"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    ROUNDED_GRID = TableFormat(
        lineabove=Line("╭", "─", "┬", "╮"),
        linebelowheader=Line("├", "─", "┼", "┤"),
        linebetweenrows=Line("├", "─", "┼", "┤"),
        linebelow=Line("╰", "─", "┴", "╯"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    HEAVY_GRID = TableFormat(
        lineabove=Line("┏", "━", "┳", "┓"),
        linebelowheader=Line("┣", "━", "╋", "┫"),
        linebetweenrows=Line("┣", "━", "╋", "┫"),
        linebelow=Line("┗", "━", "┻", "┛"),
        headerrow=DataRow("┃", "┃", "┃"),
        datarow=DataRow("┃", "┃", "┃"))
    MIXED_GRID = TableFormat(
        lineabove=Line("┍", "━", "┯", "┑"),
        linebelowheader=Line("┝", "━", "┿", "┥"),
        linebetweenrows=Line("├", "─", "┼", "┤"),
        linebelow=Line("┕", "━", "┷", "┙"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    DOUBLE_GRID = TableFormat(
        lineabove=Line("╔", "═", "╦", "╗"),
        linebelowheader=Line("╠", "═", "╬", "╣"),
        linebetweenrows=Line("╠", "═", "╬", "╣"),
        linebelow=Line("╚", "═", "╩", "╝"),
        headerrow=DataRow("║", "║", "║"),
        datarow=DataRow("║", "║", "║"))
    FANCY_GRID = TableFormat(
        lineabove=Line("╒", "═", "╤", "╕"),
        linebelowheader=Line("╞", "═", "╪", "╡"),
        linebetweenrows=Line("├", "─", "┼", "┤"),
        linebelow=Line("╘", "═", "╧", "╛"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    OUTLINE = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("+", "=", "+", "+"),
        linebetweenrows=None,
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    SIMPLE_OUTLINE = TableFormat(
        lineabove=Line("┌", "─", "┬", "┐"),
        linebelowheader=Line("├", "─", "┼", "┤"),
        linebetweenrows=None,
        linebelow=Line("└", "─", "┴", "┘"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    ROUNDED_OUTLINE = TableFormat(
        lineabove=Line("╭", "─", "┬", "╮"),
        linebelowheader=Line("├", "─", "┼", "┤"),
        linebetweenrows=None,
        linebelow=Line("╰", "─", "┴", "╯"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))
    HEAVY_OUTLINE = TableFormat(
        lineabove=Line("┏", "━", "┳", "┓"),
        linebelowheader=Line("┣", "━", "╋", "┫"),
        linebetweenrows=None,
        linebelow=Line("┗", "━", "┻", "┛"),
        headerrow=DataRow("┃", "┃", "┃"),
        datarow=DataRow("┃", "┃", "┃"))
    MIXED_OUTLINE = TableFormat(
        lineabove=Line("┍", "━", "┯", "┑"),
        linebelowheader=Line("┝", "━", "┿", "┥"),
        linebetweenrows=None,
        linebelow=Line("┕", "━", "┷", "┙"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│")) 
    DOUBLE_OUTLINE = TableFormat(
        lineabove=Line("╔", "═", "╦", "╗"),
        linebelowheader=Line("╠", "═", "╬", "╣"),
        linebetweenrows=None,
        linebelow=Line("╚", "═", "╩", "╝"),
        headerrow=DataRow("║", "║", "║"),
        datarow=DataRow("║", "║", "║"))
    FANCY_OUTLINE = TableFormat(
        lineabove=Line("╒", "═", "╤", "╕"),
        linebelowheader=Line("╞", "═", "╪", "╡"),
        linebetweenrows=None,
        linebelow=Line("╘", "═", "╧", "╛"),
        headerrow=DataRow("│", "│", "│"),
        datarow=DataRow("│", "│", "│"))  
    GITHUB = TableFormat(
        lineabove=Line("|", "-", "|", "|"),
        linebelowheader=Line("|", "-", "|", "|"),
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    ORGTBL = TableFormat(
        lineabove=None,
        linebelowheader=Line("|", "-", "+", "|"),
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    PRESTO = TableFormat(
        lineabove=None,
        linebelowheader=Line("", "-", "+", ""),
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("", "|", ""),
        datarow=DataRow("", "|", "")) 
    PRETTY = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("+", "-", "+", "+"),
        linebetweenrows=None,
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    PSQL = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("|", "-", "+", "|"),
        linebetweenrows=None,
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    RST = TableFormat(
        lineabove=Line("", "=", "  ", ""),
        linebelowheader=Line("", "=", "  ", ""),
        linebetweenrows=None,
        linebelow=Line("", "=", "  ", ""),
        headerrow=DataRow("", "  ", ""),
        datarow=DataRow("", "  ", ""))
    DOTTED = TableFormat(
        lineabove=Line("", ".", "", ""),
        linebelowheader=Line("", ".", "", ""),
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("", "", ""),
        datarow=DataRow("", "", ""))
    MINIMAL = TableFormat(
        lineabove=None,
        linebelowheader=None,
        linebetweenrows=None,
        linebelow=None,
        headerrow=DataRow("", "", ""),
        datarow=DataRow("", "", ""))
    BOX = TableFormat(
        lineabove=Line("╔", "═", "╦", "╗"),
        linebelowheader=Line("╠", "═", "╬", "╣"),
        linebetweenrows=Line("╟", "─", "┼", "╢"),
        linebelow=Line("╚", "═", "╩", "╝"),
        headerrow=DataRow("║", "║", "║"),
        datarow=DataRow("║", "║", "║"))
    CUSTOM2 = TableFormat(
        lineabove=Line("~", "=", "~", "~"),
        linebelowheader=Line("~", "-", "~", "~"),
        linebetweenrows=None,
        linebelow=Line("~", "=", "~", "~"),
        headerrow=DataRow("#", "#", "#"),
        datarow=DataRow("~", "~", "~"))
    DIM = TableFormat(
        lineabove=Line(".", ".", ".", "."),
        linebelowheader=Line(".", "-", ".", "."),
        linebetweenrows=None,
        linebelow=Line(".", ".", ".", "."),
        headerrow=DataRow(".", ".", "."),
        datarow=DataRow(".", ".", "."))
    DOTS = TableFormat(
        lineabove=Line(".", ".", ".", "."),
        linebelowheader=Line(".", "-", ".", "."),
        linebetweenrows=None,
        linebelow=Line(".", ".", ".", "."),
        headerrow=DataRow(".", ".", "."),
        datarow=DataRow(".", ".", "."))
    WAVE = TableFormat(
        lineabove=Line("~", "~", "~", "~"),
        linebelowheader=Line("~", "~", "~", "~"),
        linebetweenrows=None,
        linebelow=Line("~", "~", "~", "~"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    ZEBRA = TableFormat(
        lineabove=Line("-", "-", "-", "-"),
        linebelowheader=Line("-", "-", "-", "-"),
        linebetweenrows=Line(".", ".", ".", "."),
        linebelow=Line("-", "-", "-", "-"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    DIAMOND = TableFormat(
        lineabove=Line("◆", "◆", "◆", "◆"),
        linebelowheader=Line("◇", "◇", "◇", "◇"),
        linebetweenrows=None,
        linebelow=Line("◆", "◆", "◆", "◆"),
        headerrow=DataRow("◈", "◈", "◈"),
        datarow=DataRow("◈", "◈", "◈"))
    HEXAGON = TableFormat(
        lineabove=Line("⬡", "⬡", "⬡", "⬡"),
        linebelowheader=Line("⬠", "⬠", "⬠", "⬠"),
        linebetweenrows=None,
        linebelow=Line("⬡", "⬡", "⬡", "⬡"),
        headerrow=DataRow("⬢", "⬢", "⬢"),
        datarow=DataRow("⬢", "⬢", "⬢"))
    PLUS_MINUS = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("+", "-", "+", "+"),
        linebetweenrows=None,
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "-", "|"),
        datarow=DataRow("|", "-", "|"))    
    CUSTOM_DIAGONAL = TableFormat(
        lineabove=Line("/", "/", "/", "/"),
        linebelowheader=Line("\\", "\\", "\\", "\\"),
        linebetweenrows=None,
        linebelow=Line("\\", "\\", "\\", "\\"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    HORIZONTAL_DASHED = TableFormat(
        lineabove=Line("-", "-", "-", "-"),
        linebelowheader=Line("-", "-", "-", "-"),
        linebetweenrows=None,
        linebelow=Line("-", "-", "-", "-"),
        headerrow=DataRow("|", "|", "|"),
        datarow=DataRow("|", "|", "|"))
    CROSS_PLUS = TableFormat(
        lineabove=Line("+", "-", "+", "+"),
        linebelowheader=Line("+", "-", "+", "+"),
        linebetweenrows=None,
        linebelow=Line("+", "-", "+", "+"),
        headerrow=DataRow("|", "-", "|"),
        datarow=DataRow("|", "-", "|"))
    
class CellAlignStyle(enum.Enum):
    LEFT_TOP = "left_top"
    LEFT_MIDDLE = "left_middle"
    LEFT_BOTTOM = "left_bottom"
    CENTER_TOP = "center_top"
    CENTER_MIDDLE = "center_middle"
    CENTER_BOTTOM = "center_bottom"
    RIGHT_TOP = "right_top"
    RIGHT_MIDDLE = "right_middle"
    RIGHT_BOTTOM = "right_bottom"

class Table:
    __slots__ = ('maxsize','style', 'header', 'rows', 'glob',)
    'Класс для создания таблицы'
    def __init__(self, 
                 header = [],                           #Заголовок
                 rowslist = None,                       #Строки
                 style:TableStyle = TableStyle.PRETTY,  #Стиль таблицы
                 maxsize: int = 0,                      #Максимальный размер таблицы
                 **kwargs
                ):
        self.maxsize = maxsize
        if isinstance(style, str):
            self.style = TableStyle.PRETTY #def
            for tablestyle in TableStyle:
                if style.upper() == tablestyle.name:
                    self.style = tablestyle
                    break
        else:
            self.style = style
        self.header = Row(header, style=self.style.value.headerrow, **kwargs) if len(header) != 0 else None
        if isinstance(rowslist, list):
            self.rows = [Row(rowlist, style=self.style.value.datarow, **kwargs) for rowlist in rowslist]
        else:
            self.rows = []
        self.glob = kwargs
    def addrow(self, rowdata:list, **kwargs):
        args = self.glob | kwargs
        newrow = Row(rowdata, style=self.style.value.datarow, **args)
        self.rows.append(newrow)
        return newrow
    def __reset_all_cells(self):
        if self.header is not None:
            for hcell in self.header:
                hcell.reset_maxlen()
        if (self.rows is not None) and (len(self.rows) > 0):
            for drow in self.rows:
                for dcell in drow:
                    dcell.reset_maxlen()
    def __create_special_row(self, sample, fill, style):
        line =  Row(style=style)
        for headercell in sample:
            new_cell = Cell(fill*len(headercell[0]), indent=0)
            line.append(new_cell)
        return line
    def __str__(self) -> str:
        if (self.header is None) and (self.rows is None or len(self.rows) == 0):
            return ''
        if isinstance(self.style, str):
            style = self.style
            self.style = TableStyle.PRETTY #def
            for tablestyle in TableStyle:
                if style.upper() == tablestyle.name:
                    self.style = tablestyle
                    break
        if self.header is not None:
            self.header.update()
            for trow in self.rows:
                trow.update()
            #Расчёт таблицы
            if self.maxsize == 0: #Если не стоит придельный размер таблицы
                for i, headercell in enumerate(self.header):
                    if headercell.maxlen == 0: #Размер по содержимому
                        maxsize = len(headercell[0])
                        for rowdata in self.rows:
                            size = len(rowdata[i][0])
                            maxsize = size if size > maxsize else maxsize
                        headercell.maxlen = maxsize
                    else:
                        maxsize = headercell.maxlen
                    #Выставляем размер ячеек в строке
                    for rowdata in self.rows:
                        rowdata[i].maxlen = maxsize
                        #rowdata[i].update()
            else:
                pass        
            #Верх
            tablestr = ''
            if self.style.value.lineabove is not None:
                tablestr += self.__create_special_row(self.header, self.style.value.lineabove.hline, self.style.value.lineabove).__str__()
            
            self.header.style=self.style.value.headerrow #Обновим стиль
            tablestr += self.header.__str__() #Заголовок
            
            if self.style.value.linebelowheader is not None:
                tablestr +=  self.__create_special_row(self.header, self.style.value.linebelowheader.hline, self.style.value.linebelowheader).__str__()

        #Строки
        if isinstance(self.rows, list):
            for i, datarow in enumerate(self.rows):
                datarow.style=self.style.value.datarow
                tablestr += datarow.__str__()
                if i < len(self.rows) - 1:
                    if self.style.value.linebetweenrows is not None:
                        tablestr +=  self.__create_special_row(self.header, self.style.value.linebetweenrows.hline, self.style.value.linebetweenrows).__str__()
                else:
                    if self.style.value.linebelow is not None:
                        tablestr +=  self.__create_special_row(self.header, self.style.value.linebelow.hline, self.style.value.linebelow).__str__()                  
        #Восстанавливаем значения размеров
        self.__reset_all_cells()
        return tablestr
    def tablewidth(self):
        #Расчёт таблицы
        if self.maxsize == 0:
            for i, headercell in enumerate(self.header):
                if headercell.maxlen == 0: #Размер по содержимому
                    maxsize = len(headercell[0])
                    for rowdata in self.rows:
                        size = len(rowdata[i][0])
                        maxsize = size if size > maxsize else maxsize
                    headercell.maxlen = maxsize
        else:
            pass #Todo       
        #Верх
        tablestr = ''
        self.header.style=self.style.value.headerrow #Обновим стиль
        tablestr += self.header.__str__() #Заголовок
        for i, headercell in enumerate(self.header):
            headercell.reset_maxlen()
        return len(tablestr) - 1#'\n'      

class Row:
    __slots__ = ('cells','style',)
    'Класс для создания строки ячеек(Cell) или заголовка'
    def __init__(self, style = None):
        self.cells = []
        if style is None:
            self.style = TableStyle.PRETTY.value.datarow
        else:
            self.style = style        
    def __init__(self, listtext:list = [],   #Значение ячейки
                 style = None,               #Стиль вывода
                 **kwargs
                 ): 
                    self.cells = []
                    for data in listtext:
                        self.cells.append(Cell(data, 
                                               kwargs.get('wordwrap', False), 
                                               kwargs.get('maxlen', 0), 
                                               kwargs.get('height', 1), 
                                               kwargs.get('align', CellAlignStyle.LEFT_TOP),
                                               kwargs.get('indent', 1), 
                                               kwargs.get('indenttext', ' ')))
                    if style is None:
                        self.style = TableStyle.PRETTY.value.datarow
                    else:
                        self.style = style
    def __str__(self) -> str:
        maxrow = 1
        for cell in self.cells:
            maxrow = maxrow if len(cell) < maxrow else len(cell)
        strout = ''
        for i in range(maxrow):
            for cellnum, cell in enumerate(self.cells):                           
                text = (' ' * len(cell[0])) if i >= len(cell) else cell[i]
                if self.style is not None:
                    strout += f"{self.style.begin if cellnum == 0 and self.style is not None else ''}"
                strout += f"{text}"
                if self.style is not None:                                    
                    strout += f"{self.style.end if cellnum == len(self.cells) - 1 else self.style.sep}"
            strout += '\n'    
        return strout
    def __getitem__(self, i):
        return self.cells[i]        
    def __len__(self):
        return len(self.cells)
    def __iter__(self):
        return iter(self.cells)
    def append(self, cell):
        self.cells.append(cell)
    def update(self):
        for rcell in self.cells:
            rcell.update()
    
class Cell:
    'Форматированный вывод теста, представление виде невидимой ячейки'
    __slots__ = ('maxlen','height', 'text', 'wordwrap', 'align','indent','indenttext','textlist','saveargs')
    def __init__(self, text = "",        #Значение ячейки
                 wordwrap:bool =False,   #Перенос слов
                 maxlen:int =0,          #Максимальная длинна ячейки в символах 
                 height:int =1,          #Максимальная высота ячейки
                 align:CellAlignStyle = CellAlignStyle.LEFT_TOP, #Выравнивание ячейки
                 indent:int = 1,         #Отступ вначале и в конце, длинна
                 indenttext:str = ' '    #Заполнитель для отступа
                 ):
        self.saveargs = {arg: value for arg, value in locals().items() if arg != 'self'}
        self.maxlen = maxlen
        self.height = height
        if text is None:
            self.text = ""
        else:
            self.text = str(text)
        self.wordwrap = wordwrap
        self.align = align
        self.indent = indent
        self.indenttext = indenttext
    def reset_maxlen(self):
        self.maxlen = self.saveargs['maxlen']
        self.update()
    def set_maxlen(self, maxlen):
        self.maxlen = maxlen
        self.saveargs['maxlen'] = maxlen 
        self.update()
    def update(self):
        height = self.height
        linefeed = False
        if height == 0: #Авто перенос строк, расчёт количества строк в зависимости от maxlen
            if self.maxlen != 0: #Если есть максимальная длина, есть что переносить
                warptext = textwrap.wrap(self.text, width=self.maxlen, placeholder="...")
                height = len(warptext)
                if height == 0: height = 1
            else:
                height = len(self.text.split('\n')) #Перенос с учётом символа \n
                linefeed = True   
        self.textlist = ["" for _ in range(height)] #Список по количеству строк
        if height > 1: 
            textlen = len(self.text) if self.maxlen == 0 else (self.maxlen - (self.indent*2))
            if linefeed and self.maxlen == 0: 
                warptext = self.text.split('\n')
            else:
                warptext = textwrap.wrap(self.text, width=textlen, max_lines=height, placeholder= "..." if textlen >= 3 else textlen*".")
            startpos = 0
            if len(warptext) < height: #Можно выравнивать, по вертикали
                if ((self.align == CellAlignStyle.CENTER_BOTTOM) or (self.align == CellAlignStyle.LEFT_BOTTOM) or (self.align == CellAlignStyle.RIGHT_BOTTOM)): startpos = len(self.textlist) - len(warptext)
                elif ((self.align == CellAlignStyle.RIGHT_MIDDLE) or (self.align == CellAlignStyle.LEFT_MIDDLE) or (self.align == CellAlignStyle.CENTER_MIDDLE)): startpos =  (int(len(self.textlist)/2)) - int(len(warptext)/2)
            for line in warptext: #За
                self.textlist[startpos] = line
                startpos += 1
        else:
            self.textlist[0] = self.text
        #Поиск максимального размера текста в ячейке
        tempmaxlen = 0
        if self.maxlen != 0: #Размер уже фиксирован
            tempmaxlen = self.maxlen
        else: #Надо рассчитать
            for i, line in enumerate(self.textlist):
                rowlen =  (len(line) + (self.indent*2))
                tempmaxlen = tempmaxlen if tempmaxlen > rowlen else rowlen 
        #Формирование вывода
        for i, line in enumerate(self.textlist): 
            rowlen =  (len(line) + (self.indent*2))
            if tempmaxlen >= rowlen: #Если длины достаточно для форматированого вывода
                align = tempmaxlen - (self.indent*2) #Выравнивание не зависимо от отсупов
                if ((self.align == CellAlignStyle.CENTER_MIDDLE) or (self.align == CellAlignStyle.CENTER_BOTTOM) or (self.align == CellAlignStyle.CENTER_TOP)): line = line.center(align)
                elif ((self.align == CellAlignStyle.RIGHT_BOTTOM) or (self.align == CellAlignStyle.RIGHT_MIDDLE) or (self.align == CellAlignStyle.RIGHT_TOP)): line = line.rjust(align)
                else: line = line.ljust(align)
                line = f"{self.indent*self.indenttext[0]}{line}{self.indent*self.indenttext[0]}"
            else: #Если длины не достаточно для форматированого вывода
                if tempmaxlen >= len(line): #Если хватает для вывода текста, убираем отступы
                    indent = int((tempmaxlen - len(line))/ 2)
                    line = f"{indent*self.indenttext[0]}{line}{((tempmaxlen - len(line))% 2) * ' '}{indent*self.indenttext[0]}"
                else:    
                    if tempmaxlen > 3: #Если длинны вмещяем троеточие для сокрашения
                        line = f"{line[0:tempmaxlen-3]}..."
                    else:
                        line = f"{'.'*tempmaxlen}"        
            self.textlist[i] = line        

    def __str__(self) -> str:
        self.update()
        return "\n".join(self.textlist)
    def __iter__(self):
        self.update()
        return iter(self.textlist)
    def __getitem__(self, i):
        self.update()
        return self.textlist[i]
    def __len__(self):
        self.update()
        return len(self.textlist)
    def __copy__(self):
        self.update()
        my_copy = type(self)()
        my_copy.__dict__.update(self.__dict__)
        return my_copy 
