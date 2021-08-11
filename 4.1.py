# Рассчёт заработный платы сотрудника

def works_salary():
    work_time = int(input('Введите количество отработанных часов за месяц: '))
    bid = int(input('Введите рабочую ставку за час: '))
    prize = int(input('Введите премию сотрудника за месяц:  '))
    salary = round(work_time * bid + prize, 0)
    print(f'Заработная плата сотрудника  {salary}')

works_salary()