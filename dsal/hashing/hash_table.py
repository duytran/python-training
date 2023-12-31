import unittest


class HashItem:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value


class HashTable:
    def __init__(self) -> None:
        self.size = 256
        self.slots = [None for i in range(self.size)]
        self.count = 0

    def _hash(self, key):
        mult = 1
        hv = 0
        for ch in key:
            hv += mult * ord(ch)
            mult += 1
        return hv % self.size

    def put(self, key, value):
        item = HashItem(key, value)
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                break
            h = (h + 1) % self.size
            if self.slots[h] is None:
                self.count += 1
        self.slots[h] = item


    def get(self, key):
        h = self._hash(key)
        while self.slots[h] is not None:
            if self.slots[h].key is key:
                return self.slots[h].value
            h = (h + 1) % self.size

        return None

class TestHashTable(unittest.TestCase):
    def test_hashtable(self):
        ht = HashTable()
        ht.put("good", "eggs")
        ht.put("better", "ham")
        ht.put("best", "spam")
        ht.put("ad", "do not")
        ht.put("ga", "collide")
        for key in ("good", "better", "best", "worst", "ad", "ga"):
            v = ht.get(key)
            print(v)


if __name__ == "__main__":
    unittest.main()
