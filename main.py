#так как в задании явно не сказано, что конкретно нужно тестировать, я протестировала встроенные методы языка
#рандом добавлен для того, чтобы тесты были разнообразные

import pytest
from random import randint

#проверка метода append
def test_list_append():
    lst = [randint(0, 9) for i in range(randint(5, 10))]
    elem = randint(10, 15) #чтобы точно не было совпадений, и прибавляемый элемент отличался от всего списка
    lst.append(elem)
    assert lst[-1] == elem

#проверка метода insert
def test_list_insert():
    lst = [randint(0, 9) for i in range(10)]
    i = randint(0, 9)
    elem = randint(10, 15)
    lst.insert(i, elem)
    assert lst[i] == elem

#проверка метода remove - негативный тест
@pytest.mark.parametrize("lst,elem", [([randint(0, 9) for i in range(10)], randint(10, 15)) for i in range(10)])
def test_list_remove(lst, elem):
    lst = [randint(0, 9) for i in range(10)]
    elem = randint(10, 15)
    with pytest.raises(ValueError):
        lst.remove(elem)
        assert True

#проверка метода count
def test_tuple_count():
    check = randint(1, 10) #сколько будет элементов в неизменяемом списке
    tupl = ['a' for i in range(check)]
    tupl  = tuple(tupl)
    assert tupl.count('a') == check

#проверка работы срезов
def test_tuple_slices():
    check = randint(1, 10)  # сколько будет элементов в неизменяемом списке
    tupl = [i for i in range(check)]
    tupl = tuple(tupl)
    reversd = [i for i in range(check-1, -1, -1)]
    reversd = tuple(reversd)
    assert tupl[::-1] == reversd

#проверка метода index
def test_tuple_indexes():
    check = randint(1, 10)  # сколько будет элементов в неизменяемом списке
    tupl = [(i for i in range(check))]
    tupl = tuple(tupl)
    for i in range(check):
        assert tupl.index(i) == i