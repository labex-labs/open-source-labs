# 文字列を繰り返す

`s` という文字列と `n` という整数を 2 つのパラメータとして受け取る `repeat_string` という関数を書きます。この関数は、`s` を `n` 回繰り返した新しい文字列を返す必要があります。

たとえば、`s` が `"hello"` で `n` が `3` の場合、関数は `"hellohellohello"` を返す必要があります。`s` が `"abc"` で `n` が `5` の場合、関数は `"abcabcabcabcabc"` を返す必要があります。

```python
def n_times_string(s, n):
  return (s * n)
```

```python
n_times_string('py', 4) #'pypypypy'
```
