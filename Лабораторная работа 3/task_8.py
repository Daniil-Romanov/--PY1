money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0
# вариант, предполагающий, что сначала траты, а потом в конце месяца зарплата:
while money_capital >= 0:                     # альтернативный вариант, если зарплата в начале месяца, а потом траты:
    money_capital = money_capital - spend     # money_capital = money_capital + salary - spend
    spend = spend*(1 + increase)              # spend = spend*(1 + increase)
    if money_capital >= 0:                    # if money_capital >= 0:
        month = month + 1                         # month = month + 1
    else:
        break
    money_capital = money_capital + salary
print(month)                                  # напечатает ответ 5.


