

      
from collections import OrderedDict

class LRUCache:
    # we use Ordered Dictionary for special features 

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Mark as recently used
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

        # 3 cases here .. 
        # 1 -> if it exists move to the end for mostly recently  used !! and then update it  
        # 2 -> if not in cache then add it 
        # 3 -> if the capacity exceeds then remove the least recently used 
        # using the .popitem
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the least recently used (first) item
            self.cache.popitem(last=False)  




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)