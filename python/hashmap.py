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

    def put(self, key, value):
        hash_key = hash(key) % self.size
        bucket = self.hashmap[hash_key]
        bucket_index = -1
        for index, pair in enumerate(bucket):
            current_key, current_value = pair
            if current_key == key:
                bucket_index = index
        if bucket_index == -1:
            bucket.append((key, value))
            self.num_keys += 1
            self._rehash_upsize()
        else:
            bucket[bucket_index] = (key, value)

    def _rehash_upsize(self):
        if self.num_keys < self.size:
            return
        new_size = self.size * 2
        new_hashmap = [[] for _ in range(new_size)]
        for bucket in self.hashmap:
            for key, value in bucket:
                new_hash_key = hash(key) % new_size
                new_bucket = new_hashmap[new_hash_key]
                new_bucket.append((key, value))
        self.size = new_size
        self.hashmap = new_hashmap

    def get(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hashmap[hash_key]
        for current_key, current_value in bucket:
            if current_key == key:
                return current_value
        raise KeyError(f'Cannot retrieve with key {key} as key not found.')

    def remove(self, key):
        hash_key = hash(key) % self.size
        bucket = self.hashmap[hash_key]
        bucket_index = -1
        for index, pair in enumerate(bucket):
            current_key, current_value = pair
            if current_key == key:
                bucket_index = index
        if bucket_index == -1:
            raise KeyError(f'Cannot remove with key {key} as key not found.')
        else:
            del bucket[bucket_index]
            self.num_keys -= 1
            self._rehash_downsize()

    def _rehash_downsize(self):
        if self.num_keys > self.size // 4:
            return
        new_size = self.size // 4
        new_hashmap = [[] for _ in range(new_size)]
        for bucket in self.hashmap:
            for key, value in bucket:
                new_hash_key = hash(key) % new_size
                new_bucket = new_hashmap[new_hash_key]
                new_bucket.append((key, value))
        self.size = new_size
        self.hashmap = new_hashmap

    def __str__(self):
        to_return = ''
        for bucket in self.hashmap:
            for key, value in bucket:
                to_return += f'Key: {key}, Value: {value}\n'
        return to_return


if __name__ == '__main__':
    hashmap = HashMap(size=2)
    hashmap[1] = 'one'
    print(f'Expected size 2: {hashmap.size}')

    hashmap[2] = 'two'
    print(f'Expected size 4: {hashmap.size}')

    hashmap[3] = 'three'
    hashmap[1] = 'new one'

    print()
    print(hashmap)

    print(f"Expected to print 'two': {hashmap[2]}")

    del hashmap[2]
    del hashmap[3]

    print(f'Expected size 1: {hashmap.size}')

    print()
    print(hashmap)
