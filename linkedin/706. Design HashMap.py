class MyHashMap:
    def __init__(self):
        self.size = 1000  # Number of buckets
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        """Hash function to compute the bucket index."""
        return key % self.size

    def put(self, key, value):
        """Insert or update the (key, value) pair."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                self.buckets[index][i] = (key, value)  # Update value if key exists
                return
        self.buckets[index].append((key, value))  # Insert new pair if key not found

    def get(self, key):
        """Retrieve the value for the given key, or -1 if key doesn't exist."""
        index = self._hash(key)
        for k, v in self.buckets[index]:
            if k == key:
                return v
        return -1  # Key not found

    def remove(self, key):
        """Remove the key-value pair if it exists."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[index]):
            if k == key:
                del self.buckets[index][i]  # Remove the pair
                return
