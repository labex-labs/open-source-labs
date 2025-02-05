# 重复字符串

编写一个名为 `repeat_string` 的函数，它接受两个参数：一个字符串 `s` 和一个整数 `n`。该函数应返回一个新字符串，其中包含重复 `n` 次的 `s`。

例如，如果 `s` 是 `"hello"` 且 `n` 是 `3`，则该函数应返回 `"hellohellohello"`。如果 `s` 是 `"abc"` 且 `n` 是 `5`，则该函数应返回 `"abcabcabcabcabc"`。

```python
def n_times_string(s, n):
  return (s * n)
```

```python
n_times_string('py', 4) #'pypypypy'
```
