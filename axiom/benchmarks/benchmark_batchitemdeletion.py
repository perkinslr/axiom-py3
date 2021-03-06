
"""
Benchmark batch creation of a large number of simple Items in a transaction.
"""

from epsilon.scripts import benchmark

from axiom.store import Store
from axiom.item import Item
from axiom.attributes import integer, text

class AB(Item):
    a = integer()
    b = text()

def main():
    s = Store("TEMPORARY.axiom")
    rows = [(x, str(x)) for x in range(10000)]
    s.transact(lambda: s.batchInsert(AB, (AB.a, AB.b), rows))

    benchmark.start()
    s.transact(s.query(AB).deleteFromStore)
    benchmark.stop()


if __name__ == '__main__':
    main()
