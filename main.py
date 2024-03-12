from tabulate import tabulate
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# Graphics in SVG format are more sharp and legible
#%config InlineBackend.figure_format = 'svg'
pd.set_option("display.precision", 2)

def printTable(data):
    df = pd.DataFrame(data)
    print(tabulate(df, headers='keys', tablefmt='psql'))

data = pd.read_csv('titanic_train.csv', index_col='PassengerId')
#
# # printTable(data.head(5))
# 1 question
print('\n1.Сколько мужчин / женщин было на борту? \n')
number_all_person = len(data)
number_female = data[data['Sex'] == 'female'].shape[0]
number_male = data[data['Sex'] == 'male'].shape[0]

print(f'Количество пассажиров = {number_all_person} | мужчин = {number_male} | женщин = {number_female} |')
# print('\n')

# 2 question
print('\n2. Определите распределение функции Pclass. Теперь Для мужчин и женщин отдельно. Сколько людей из второго класса было на борту? \n')
numberMiddleClass = data[data['Pclass'] == 2].count().Pclass
numberMiddleClassFemale = data[(data['Pclass'] == 2) & (data['Sex'] == 'female')].count().Pclass
numberMiddleClassMale = data[(data['Pclass'] == 2) & (data['Sex'] == 'male')].count().Pclass
print(f'Количество пассажиров среднего класса = {numberMiddleClass} | мужчин = {numberMiddleClassMale} | женщин = {numberMiddleClassFemale} |')

# # 3 question
print('\n3.Каковы медиана и стандартное отклонение Fare?. Округлите до 2-х знаков после запятой. \n')
print('медиана ', '%.2f' % data['Fare'].median(), ', стандартное отклонение ','%.2f' % data['Fare'].std())

# 4 question

print('\n4. Правда ли, что средний возраст выживших людей выше, чем у пассажиров, которые в конечном итоге умерли? \n')

mean_age_deads = data[data['Survived'] == 0]['Age'].mean()
mean_age_alives = data[data['Survived'] == 1]['Age'].mean()

survived_higher_mean_age = mean_age_alives > mean_age_deads

result = "Да!" if survived_higher_mean_age else "Нет!"

print(f' - {result}')
print(f'(выживших-{mean_age_alives:.2f}, не выживших-{mean_age_deads:.2f})')

# 5 question

print('\n5. Это правда, что пассажиры моложе 30 лет. выжили чаще, чем те, кому больше 60 лет. Каковы доли выживших людей среди молодых и пожилых людей? \n')

young = data[data['Age'] < 30]
young_procent_alives = len(young[young['Survived'] == 1]) / len(young)
old = data[data['Age'] > 60]
old_procent_alives = len(old[old['Survived'] == 1]) / len(old)

print('%.1f' % (young_procent_alives * 100), '% среди молодежи и ', '%.1f' % (old_procent_alives * 100), '% среди пожилых')

# 6 question

print('\n6. Правда ли, что женщины выживали чаще мужчин? Каковы доли выживших людей среди мужчин и женщин? \n')

women_proportion = data[data['Sex'] == 'female']['Survived'].mean()
men_proportion = data[data['Sex'] == 'male']['Survived'].mean()

print(f'{men_proportion*100:.1f}% среди мужчин и {women_proportion*100:.1f}% среди женщин')

# 7 question

print('\n7. Какое имя наиболее популярно среди пассажиров мужского пола? \n')

most_common_name = data[data['Sex'] == 'male']['Name'].str.split().str[2].value_counts().idxmax()

print(f'Answer: {most_common_name}')

# 8 question

print('\n8. Как средний возраст мужчин / женщин зависит от Pclass? Выберите все правильные утверждения: ')

pclass_avg_age = data.groupby(['Pclass', 'Sex'])['Age'].mean().unstack()

# Additional statements
number8questMale = data[(data['Pclass'] == 1) & (data['Sex'] == 'male')]['Age']
number8anserMale = number8questMale.sum()/len(number8questMale)

print('\nВ среднем мужчины 1 класса старше 40 лет: ')
if (number8anserMale > 40):
    print('Да')
else:
    print('Нет')

print('В среднем женщины 1 класса старше 40 лет:', 'Да' if pclass_avg_age.loc[1, 'female'] > 40 else 'Нет')
print('Мужчины всех классов в среднем старше, чем женщины того же класса:', 'Да' if (pclass_avg_age.loc[:, 'male'] > pclass_avg_age.loc[:, 'female']).all() else 'Нет')
print('В среднем пассажиры первого класса старше, чем пассажиры 2-го класса, которые старше, чем пассажиры 3-го класса:', 'Да' if (pclass_avg_age.loc[1] > pclass_avg_age.loc[2]).all() and (pclass_avg_age.loc[2] > pclass_avg_age.loc[3]).all() else 'Нет')