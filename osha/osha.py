
from mmh3 import hash as murmur

__seed = 1243830022348823870120591
__a = 17
__b = 5

def __gen_prng(message, seed, size):
    bin_res = 0

    for i in range(size):
        d = murmur(message, seed, signed=False)
        e = murmur(d.to_bytes(16, 'big'), seed, signed=False)
        message = (d << d.bit_length() | e).to_bytes(16, 'big')
        seed = abs(d - e)
        bin_res = bin_res | (((d & 1) ^ 1) << i)

    return bin_res


def __rotate_left(n, d, size):
    assert d <= size, "Can't rotate with more than size bits."
    return ((n << d) % (1 << size)) | (n >> (size - d))


def __rotate_right(n, d, size):
    assert d <= size, "Can't rotate with more than size bits."
    return ((n % (1 << d)) << (size - d)) | (n >> d)


def hash(message, size):
    seed = __seed ^ size

    tau = __gen_prng(message, seed, size)
    hashed_message = murmur(message, seed, signed=False)
    rounds = (hashed_message % __a) + __b

    for _ in range(rounds):
        seed = seed ^ hashed_message
        rotations = hashed_message % size

        if (__gen_prng(message, seed, 1) & 1) ^ 1:
            tau = __rotate_left(tau, rotations, size)
        else:
            tau = __rotate_right(tau, rotations, size)

        message = hashed_message.to_bytes(16, 'big')
        
        hashed_message = murmur(message, seed, signed=False)
        tau = tau ^ __gen_prng(message, seed, size)
    
    return hex(tau)
