revenues=int(input("Какая у Вас выручка? "))
cost=int(input("Какие издержки? "))
if revenues<cost:
    print("К сожалению, Вы в убытке")
elif revenues==cost:
    print("Вы работаете в ноль")
else:
    profit=revenues/cost
    employees=int(input("Сколько у Вас работников? "))
    profitonempoyee=revenues//employees
    print("Соотношение прибыли к выручке - ", profit)
    print("Прибыль на одного сотрудника составила - ", profitonempoyee)


