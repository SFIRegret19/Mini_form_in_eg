from easygui import *

rate = 0.05
max_sum = 100000
fieldNames = ['Имя',"Фамилия","Возраст","Сумма",'Количество лет, за которое вы хотите отдать сумму']
fieldValues = []
fieldValues = multenterbox('Форма','Заполните форму',fieldNames)
print(fieldValues)

age = int(fieldValues[2])
summ = int(fieldValues[3])
years = int(fieldValues[4])
result = (summ * rate + summ)/years*12

if age < 18:
    msgbox('В кредите отказано.')
elif 18 <= age <= 25:
    if summ > 100000:
        msgbox('В кредите отказано.') 
    else:
        msgbox('Вам одобрен кредит!')
        msgbox('Ваш ежемесечный платёж:' + str(result))
else:
    msgbox('Вам одобрен кредит!') 
    msgbox('Ваш ежемесечный платёж:' + str(result))