# `yield from` 文の理解

このステップでは、Python の `yield from` 文について詳しく調べます。この文は、ジェネレーターを扱う際の強力なツールであり、他のジェネレーターに操作を委任するプロセスを簡素化します。このステップの終わりまでに、`yield from` が何であるか、どのように動作するか、そして異なるジェネレーター間での値の受け渡しをどのように処理するかを理解するでしょう。

## `yield from` とは何か？

`yield from` 文は Python 3.3 で導入されました。その主な目的は、サブジェネレーターへの操作の委任を簡素化することです。サブジェネレーターとは、メインのジェネレーターが作業を委任できる別のジェネレーターのことです。

通常、あるジェネレーターが別のジェネレーターから値を生成する場合、ループを使用する必要があります。たとえば、`yield from` を使わない場合、次のようなコードを書くことになります。

```python
def delegating_generator():
    for value in subgenerator():
        yield value
```

このコードでは、`delegating_generator` が `for` ループを使って `subgenerator` が生成する値を反復処理し、それぞれの値を 1 つずつ生成します。

しかし、`yield from` 文を使うと、コードははるかに簡単になります。

```python
def delegating_generator():
    yield from subgenerator()
```

この 1 行のコードは、前の例のループと同じ結果を達成します。ただし、`yield from` は単なるショートカットではありません。呼び出し元とサブジェネレーター間の双方向通信も管理します。つまり、委任するジェネレーターに送られた値は、直接サブジェネレーターに渡されます。

## 基本的な例

`yield from` が実際にどのように動作するかを見るために、簡単な例を作成しましょう。

1. まず、エディタで `cofollow.py` ファイルを開く必要があります。これを行うには、`cd` コマンドを使って正しいディレクトリに移動します。ターミナルで次のコマンドを実行します。

```bash
cd /home/labex/project
```

2. 次に、`cofollow.py` ファイルに 2 つの関数を追加します。`subgen` 関数は、0 から 4 までの数を生成する単純なジェネレーターです。`main_gen` 関数は、`yield from` を使ってこれらの数の生成を `subgen` に委任し、その後 `'Done'` という文字列を生成します。`cofollow.py` ファイルの末尾に次のコードを追加します。

```python
def subgen():
    for i in range(5):
        yield i

def main_gen():
    yield from subgen()
    yield 'Done'
```

3. これで、これらの関数をテストしましょう。Python シェルを開き、次のコードを実行します。

```python
from cofollow import subgen, main_gen

# Test subgen directly
for x in subgen():
    print(x)

# Test main_gen that delegates to subgen
for x in main_gen():
    print(x)
```

このコードを実行すると、次の出力が表示されるはずです。

```
0
1
2
3
4

0
1
2
3
4
Done
```

この出力は、`yield from` が `main_gen` から `subgen` が生成するすべての値を呼び出し元に直接渡すことを可能にすることを示しています。

## `yield from` を使った値の受け渡し

`yield from` の最も強力な機能の 1 つは、双方向の値の受け渡しを処理する能力です。これを実証するために、もう少し複雑な例を作成しましょう。

1. `cofollow.py` ファイルに次の関数を追加します。

```python
def accumulator():
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value

def caller():
    acc = accumulator()
    yield from acc
    yield 'Total accumulated'
```

`accumulator` 関数は、累計値を追跡するコルーチンです。現在の累計値を生成し、次の値を受け取るのを待ちます。`None` を受け取った場合、ループを停止します。`caller` 関数は `accumulator` のインスタンスを作成し、`yield from` を使ってすべての送受信操作を委任します。

2. Python シェルでこれらの関数をテストします。

```python
from cofollow import caller

c = caller()
print(next(c))  # Start the coroutine
print(c.send(1))  # Send value 1, get accumulated value
print(c.send(2))  # Send value 2, get accumulated value
print(c.send(3))  # Send value 3, get accumulated value
print(c.send(None))  # Send None to exit the accumulator
```

このコードを実行すると、次の出力が表示されるはずです。

```
0
1
3
6
'Total accumulated'
```

この出力は、`yield from` がサブジェネレーターが使い果たされるまで、すべての送受信操作を完全に委任することを示しています。

これで `yield from` の基本を理解したので、次のステップでより実用的なアプリケーションに移りましょう。
