# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import islice
from itertools import cycle

def task2():
    list = [5, 500, "something", 12]
    for el in islice(cycle(list), 20):
        print(el)
task2()