# リストを展開する

あなたの課題は、イテレータ関数と初期のシード値を引数として受け取る `unfold` 関数を実装することです。イテレータ関数は1つの引数 (`seed`) を受け取り、常に2つの要素を持つリスト ([`value`, `nextSeed`]) または終了するための `False` を返す必要があります。`unfold` 関数は、`while` ループを使用してイテレータ関数を呼び出し、`False` が返されるまで `value` を `yield` するジェネレータ関数 `fn_generator` を使用する必要があります。最後に、`unfold` 関数は、イテレータ関数を使用してジェネレータによって生成されるリストを返すためにリスト内包表記を使用する必要があります。

`unfold` 関数を実装します：

```python
def unfold(fn, seed):
    # ここにコードを記述してください
```

### 入力

- 1つの引数 (`seed`) を受け取り、常に2つの要素を持つリスト ([`value`, `nextSeed`]) または終了するための `False` を返すイテレータ関数 `fn`。
- 初期のシード値 `seed`。

### 出力

- イテレータ関数を使用してジェネレータによって生成されるリスト。

```python
def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
```

```python
f = lambda n: False if n > 50 else [-n, n + 10]
unfold(f, 10) # [-10, -20, -30, -40, -50]
```
