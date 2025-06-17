import matplotlib.pyplot
import openpyxl

def GetCallValue(cell):# расспросить преподавателя, не понял, как это работает, такое впечатление что метод value определен для объекта любого типа. Почему у функции не указан тип параметра?!
    return cell.value

WorkBook=openpyxl.load_workbook('C:\\p4ne\\1.2\\data_analysis_lab.xlsx')#, data_only=True) Пока не разобрался, что дает этот параметр!!!

DataSheet = WorkBook['Data']

Уears = list(map(GetCallValue, DataSheet['A'][1:]))
Temperature = list(map(GetCallValue, DataSheet['B'][1:]))
RelativeTemperature = list(map(GetCallValue, DataSheet['C'][1:]))
Activity = list(map(GetCallValue, DataSheet['D'][1:]))

matplotlib.pyplot.plot(Уears, Temperature, linestyle='-', label='Температура')
matplotlib.pyplot.plot(Уears, RelativeTemperature, linestyle='-.', label='Относительная температура')
matplotlib.pyplot.plot(Уears, Activity,linestyle='--', label='Активность Cолнца')

matplotlib.pyplot.xlabel('Время (год)', fontsize=12, color='blue', fontweight='bold', fontstyle='italic')
matplotlib.pyplot.ylabel('Температура / Активность Cолнца', fontsize=12, color='green', fontweight='bold', fontstyle='italic')
matplotlib.pyplot.legend(title='Легенда',loc='best')
matplotlib.pyplot.show()
