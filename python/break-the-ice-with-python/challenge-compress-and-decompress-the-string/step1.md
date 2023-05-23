# Compress and Decompress the String

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

## Example

If you are given the following string:

```bash
'hello world!hello world!hello world!hello world!'
```

Then, the output of the program should be:

```bash
b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
b'hello world!hello world!hello world!hello world!'
```

## Hints

- Use `zlib.compress()` and `zlib.decompress()` to compress and decompress a string.
