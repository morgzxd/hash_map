import random
import math

class MyHashMap:

    def __init__(self, expt=4, debug=False):
        self.radix = 2**expt
        self.rehash_count = 0
        self.num_items = 0
        self.max_probes = self.radix

        self.keys = [None]*self.radix
        self.values = [None]*self.radix
        self.debug = debug

    def load_factor(self):
        return self.num_items / self.radix

    def compute_hash(self, key):
        return hash(key) % self.radix

    def __getitem__(self, key):
        keyhash = self.compute_hash(key)

        #TODO: Implement the rest!
        pass


    def __setitem__(self, key, value):
        keyhash = self.compute_hash(key)

        #TODO: Implement the rest!
        pass

    def rehash(self):
        if self.debug:
            print("Rehashing...")
        self.keys += [None]*self.radix
        self.values += [None]*self.radix
        self.radix *= 2

        #TODO: Implement the rest!

        self.rehash_count += 1

    def __contains__(self, key):
        keyhash = self.compute_hash(key)
        #TODO: Implement the rest!

    def __delitem__(self, key):
        keyhash = self.compute_hash(key)
        #TODO: Implement the rest!

    def fill_ratio(self):
        return self.num_items/len(self.keys)

def main():
    print("Generating keys")
    test_keys = random.sample(range(2**32), 2**8)
    print("Generating values")
    test_values = random.sample(range(2**32), 2**8)
    print()
    test_hash = MyHashMap(debug=True)

    for k, v in zip(test_keys, test_values):
        print("Inserting key {} with value {}".format(k, v))
        test_hash[k] = v
    print()

    print("Rehashed {} times".format(test_hash.rehash_count))
    print("Expected array size: {}".format(2**(4+test_hash.rehash_count)))
    print("Actual array size: {}".format(len(test_hash.keys)))
    print()

    print("{} items inserted".format(test_hash.num_items))
    print("Fill ratio: {}".format(test_hash.fill_ratio()))
    print()

    looks_good = True
    for k, v in zip(test_keys, test_values):
        if k not in test_hash:
            print("key {} not found!".format(k))
            looks_good = False
        elif test_hash[k] is not v:
            print("key {} has incorrect value (expected {}. found {})".format(k, v, test_hash[k]))
            looks_good = False

    if looks_good:
        print("Tests passed!")
    else:
        print("Tests failed. See output above.")

if __name__ == "__main__":
    main()
