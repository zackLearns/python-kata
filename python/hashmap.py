class HashMap:

    def __init__(self, size=16):
        self.num_keys = 0
        self.size = size
        self.hashmap = [[] for _ in range(size)]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.remove(key)
        print(f'Deleted key {key} from hashmap.')

    def put(self, key, value):
        hash_key = hash(key) % self.size
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
            self.num_keys += 1
            if self.num_keys >= self.size:
                self._rehash_keys()

    def _rehash_keys(self):
        new_size = self.size * 2
        new_hashmap = [[] for _ in range(new_size)]
        for bucket in self.hashmap:
            for key, value in bucket:
                hash_key = hash(key) % new_size
                new_bucket = new_hashmap[hash_key]
                new_bucket.append((key, value))
        self.size = new_size
        self.hashmap = new_hashmap

    def get(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hashmap[hash_key]
        for index, pair in enumerate(bucket):
            current_key, current_value = pair
            if current_key == key:
                return current_value
        raise KeyError(f'HashMap has no entry with key: {key!r}')

    def remove(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hashmap[hash_key]
        bucket_index_to_del = -1
        for index, pair in enumerate(bucket):
            current_key, _ = pair
            if current_key == key:
                bucket_index_to_del = index
                break
        if bucket_index_to_del == -1:
            raise KeyError(f'No existing key {key!r} in hashmap to remove.')
        else:
            del bucket[bucket_index_to_del]

    def __str__(self):
        to_return = ''
        for bucket in self.hashmap:
            for key, value in bucket:
                to_return += f'Key: {key}, Value: {value}\n'
        return to_return


if __name__ == '__main__':
    hashmap = HashMap()
    hashmap[1] = 'one'
    hashmap[2] = 'two'
    hashmap[3] = 'three'
    hashmap[1] = 'new one'

    print(hashmap[1])  # should print 'new one'
    print(hashmap[2])  # should print 'two'
    print(hashmap[3])  # should print 'three'
    try:
        print(hashmap[4])  # should encounter KeyError
    except KeyError as e:
        print(f"Accessing hashmap with key '4' encountered KeyError as expected.")

    del hashmap[2]
    try:
        print(hashmap[2])
    except KeyError as e:
        print(f"Accessing hashmap with key '2' after it is deleted encountered KeyError as expected.")

    print(hashmap)
