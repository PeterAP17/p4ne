import matplotlib.pyplot
import openpyxl

def GetCallValue(cell):
    return cell.value

WorkBook=openpyxl.load_workbook('C:\\p4ne\\1.2\\data_analysis_lab.xlsx')#, data_only=True)

DataSheet = WorkBook['Data']

years = list(map(GetCallValue, DataSheet['A'][1:]))
temperature = list(map(GetCallValue, DataSheet['C'][1:]))
activity = list(map(GetCallValue, DataSheet['D'][1:]))

matplotlib.pyplot.plot(years, temperature, label="Относительная температура")
matplotlib.pyplot.plot(years, activity, label="Активность солнца")

matplotlib.pyplot.xlabel('Время')
matplotlib.pyplot.ylabel('Температура/Активность солнца')
matplotlib.pyplot.legend(loc='upper left')

matplotlib.pyplot.show()

#ColumnA = DataSheet ['A'][1:]
#ColumnC = DataSheet ['C'][1:]
#ColumnD = DataSheet ['D'][1:]
#print(ColumnA)
#print(ColumnC)
#print(ColumnD)
