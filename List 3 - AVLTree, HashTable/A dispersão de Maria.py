class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        
    def hash_function(self, key):
        n = len(key)
        hash_value = 0
        for i in range(n):
            hash_value += (i+1) * ord(key[i])
        return (19 * hash_value) % self.size
    
    def rehash_function(self, key, i):
        return (key + i**2 + 23*i) % self.size
    
    def insert(self, key):
        hash_value = self.hash_function(key)
        if self.keys[hash_value] == key:
            return
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
        else:
            i = 1
            while True:
                hash_value = self.rehash_function(hash_value, i)
                if self.keys[hash_value] == key:
                    return
                if self.keys[hash_value] is None:
                    self.keys[hash_value] = key
                    break
                i += 1
                if i > 19:
                    break
            
    def remove(self, key):
        hash_value = self.hash_function(key)
        if self.keys[hash_value] == key:
            self.keys[hash_value] = None
            return True
        i = 1
        while True:
            hash_value = self.rehash_function(hash_value, i)
            if self.keys[hash_value] == key:
                self.keys[hash_value] = None
                return True
            if i > 19:
                return False
            i += 1
            
    def count_elements(self):
        print(sum(key is not None for key in self.keys))
    
    def print_table(self):
        for i, key in enumerate(self.keys):
            if key is not None:
                print("{}:{}".format(i,key))

def main(): 
    size = int(input())
    qtnd = int(input())

    table = HashTable(size)

    key = []

    for _ in range(qtnd):
        user_input = input().split(":")
        if user_input[0] == "ADD" and user_input[1] not in key: 
            table.insert(user_input[1])
            key.append(user_input[1])
        elif user_input[0] == "DEL" and user_input[1] in key: 
            table.remove(user_input[1])
            key.remove(user_input[1])

    table.count_elements()
    table.print_table()
    
if __name__ == "__main__":
    main()