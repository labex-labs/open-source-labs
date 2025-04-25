# 文字列を繰り返す

## 問題

`repeat_string` という関数を書きましょう。この関数は 2 つのパラメータを受け取ります。文字列 `s` と整数 `n` です。この関数は、`s` を `n` 回繰り返した新しい文字列を返す必要があります。

たとえば、`s` が `"hello"` で `n` が `3` の場合、関数は `"hellohellohello"` を返す必要があります。`s` が `"abc"` で `n` が `5` の場合、関数は `"abcabcabcabcabc"` を返す必要があります。

## 例

```python
assert repeat_string("hello", 3) == "hellohellohello"
assert repeat_string("abc", 5) == "abcabcabcabcabc"
assert repeat_string("123", 2) == "123123"
```
