from web3 import Web3

def bytearray_to_int(x: bytes) -> int:
    o = 0
    for b in x:
        o = (o << 8) + safe_ord(b)      # type: ignore
    return o

def safe_ord(value):
    if isinstance(value, int): return value
    return ord(value)


def int_to_big_endian(value: int) -> bytes:
    return value.to_bytes((value.bit_length() + 7) // 8 or 1, "big")


def big_endian_to_int(value: bytes) -> int:
    return int.from_bytes(value, "big")

def ceil32(x):
    return x if x % 32 == 0 else x + 32 - (x % 32)

def zpad(x, l):
    """ Left zero pad value `x` at least to length `l`.
    >>> zpad('', 1)
    '\x00'
    >>> zpad('\xca\xfe', 4)
    '\x00\x00\xca\xfe'
    >>> zpad('\xff', 1)
    '\xff'
    >>> zpad('\xca\xfe', 2)
    '\xca\xfe'
    """
    return b'\x00' * max(0, l - len(x)) + x

def encode_int32(v):
    return zpad(int_to_big_endian(v), 32)

def bytes_to_int(value):
    return big_endian_to_int(bytes(''.join(chr(c) for c in value)))
