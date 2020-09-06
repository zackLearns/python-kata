class HashMap:

    def __init__(self, size=16):
        self.hashmap = [[] for _ in range(size)]

    def put(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        key_exists = False
        key_index = -1
        for index, pair in enumerate(bucket):
            current_key, current_value = pair
            if current_key == key:
                key_exists = True
                key_index = index
        if key_exists:
            key_index = key_index if key_index != -1 else 0
            bucket[key_index] = (key,value)
        else:
            bucket.append((key, value))

    def get(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for index, pair in enumerate(bucket):
            current_key, current_value = pair
            if current_key == key:
                return current_value
        raise KeyError(f'HashMap has no entry with key: {key!r}')


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap.put('key1', 'value1')
    hashmap.put('key2', 'value2')

    print(hashmap.get('key1'))  # should print 'value1'
    print(hashmap.get('key3'))  # should encounter KeyError
