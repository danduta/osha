from random import randbytes
from time import time, time_ns
import matplotlib.pyplot as plt
from osha.osha import hash
import hashlib
from statistics import stdev

message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent finibus sollicitudin mauris ut pellentesque. Curabitur vel \
    augue quis magna placerat ultrices vel id leo. Fusce eget dignissim ex. Fusce non luctus felis, nec fringilla lectus. Quisque \
    accumsan tristique ipsum, at placerat lectus. Ut leo sem, sagittis id condimentum nec, venenatis vel mi. Donec vehicula mauris \
    mattis, suscipit eros ac, pellentesque odio. Donec euismod a mauris maximus fermentum. Sed iaculis fermentum arcu, sit amet \
    lobortis est molestie quis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.'


def plot_performance_osha(show):
    plt.xlabel('Output size (bits)')
    plt.ylabel('Time (ms)')
    plt.title('OSHA function performance and time complexity - O(bitsize)')

    times = []
    for i in range(3, 13):
        t0 = time()
        hash(message, 1 << i)
        t1 = time()
        times.append((t1 - t0) * 1000)

    plt.plot([1 << i for i in range(3, 13)], times, 'red')
    if show:
        plt.show()


def plot_performance_comparison_osha(show):
    plt.xlabel('Input size (bytes)')
    plt.ylabel('Time (ms)')
    plt.title('State of the art hashing functions performance comparison')

    times_osha = list()
    times_md5 = list()
    times_sha3_256 = list()
    times_sha3_512 = list()
    times_shake_256 = list()
    times_blake_2b = list()
    times_blake_2s = list()

    input_len = 20

    for i in range(3, input_len):
        message = randbytes(1 << i)

        t0 = time()
        hash(message, 256)
        t1 = time()
        times_osha.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.md5(message).hexdigest()
        t1 = time()
        times_md5.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.sha3_256(message)
        t1 = time()
        times_sha3_256.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.sha3_512(message)
        t1 = time()
        times_sha3_512.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.shake_256(message).hexdigest(32)
        t1 = time()
        times_shake_256.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.blake2b(message, digest_size=32).hexdigest()
        t1 = time()
        times_blake_2b.append((t1 - t0) * 1000)

        t0 = time()
        hashlib.blake2s(message, digest_size=32).hexdigest()
        t1 = time()
        times_blake_2s.append((t1 - t0) * 1000)

    x = [1 << i for i in range(3, input_len)]
    plt.plot(x, times_osha)
    # plt.plot(x, times_md5, 'red', label='MD5')
    # plt.plot(x, times_sha3_256, 'green', label='SHA3-256')
    # plt.plot(x, times_sha3_512, 'blue', label='SHA3-512')
    # plt.plot(x, times_shake_256, 'yellow', label='SHAKE 256')
    # plt.plot(x, times_blake_2b, 'brown', label='BLAKE 2b')
    # plt.plot(x, times_blake_2s, 'black', label='BLAKE 2s')

    plt.legend()

    if show:
        plt.show()


def collisions_osha(samples, outsize, keysize):
    hashes = set()
    collisions = 0

    for _ in range(samples):
        random_str = randbytes(keysize)
        h = hash(str(random_str), outsize)
        if h in hashes:
            collisions += 1

        hashes.add(h)

    return collisions


def plot_collisions_osha(show):
    samples = 1000
    keysize = 1024
    max_bitsize = 8

    plt.xlabel('Output size (bits)')
    plt.ylabel('Collision rate (%)')
    plt.title('Collision rate for the OSHA function')

    cols = []
    for i in range(3, max_bitsize + 1):
        print(
            f'Computing collision rate for {samples} samples of size {keysize}. Output size: {1 << i} bits')
        cols.append(collisions_osha(samples, 1 << i, keysize))

    plt.plot([1 << i for i in range(3, max_bitsize + 1)],
             [col / samples * 100 for col in cols], 'green')

    if show:
        plt.show()


# plot_collisions_osha()
# plot_performance_osha()
plot_performance_comparison_osha(True)
