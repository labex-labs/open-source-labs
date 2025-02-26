# 遅延評価

次のような関数を考えてみましょう。

```python
def after(seconds, func):
    import time
    time.sleep(seconds)
    func()
```

使用例：

```python
def greeting():
    print('Hello Guido')

after(30, greeting)
```

`after` は、後で、提供された関数を実行します。

クロージャは、追加の情報を持ち運びます。

```python
def add(x, y):
    def do_add():
        print(f'Adding {x} + {y} -> {x+y}')
    return do_add

def after(seconds, func):
    import time
    time.sleep(seconds)
    func()

after(30, add(2, 3))
# `do_add` は x -> 2 と y -> 3 の参照を持っています
```
