def get_count_char(str_):
    d = {}
    str_ = str_.lower()
    for i in range(len(str_)):
        if str_[i].isalpha():
            if str_[i] not in d:
                d[str_[i]] = 1
            else:
                d[str_[i]] += 1
    return d


def percent(d):
    summa = sum(d.values())             # сумма всех букв в строке
    for x in d:                         # x пробегает значения всех ключей в словаре
        d[x] *= 100/summa               # каждому старому ключу присваивается новое значение в процентах
    return d


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(percent(get_count_char(main_str)))