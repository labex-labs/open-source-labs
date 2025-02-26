# ローカル変数

内部関数が外部関数で定義された変数をどのように参照するかを見てみましょう。

```python
def add(x, y):
    def do_add():
        # `x` と `y` は `add(x, y)` の上で定義されています
        print('Adding', x, y)
        return x + y
    return do_add
```

さらに、`add()` が終了した後でも、それらの変数が何らかの方法で生き続けていることにも注意してください。

```python
>>> a = add(3,4)
>>> a
<function do_add at 0x6a670>
>>> a()
Adding 3 4      # これらの値はどこから来ているのでしょうか？
7
```
