import zlib


def compress_and_decompress_the_string():
    s = 'hello world!hello world!hello world!hello world!'
    # In Python 3 zlib.compress() accepts only DataType <bytes>
    y = bytes(s, 'utf-8')
    x = zlib.compress(y)
    print(x)
    print(zlib.decompress(x))


compress_and_decompress_the_string()
