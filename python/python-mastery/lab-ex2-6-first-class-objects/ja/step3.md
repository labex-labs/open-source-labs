# Python のメモリモデルの探索

Python のメモリモデルは、オブジェクトがメモリにどのように格納され、どのように参照されるかを決定する上で重要な役割を果たします。特に大規模なデータセットを扱う際には、このモデルを理解することが不可欠です。なぜなら、それが Python プログラムのパフォーマンスとメモリ使用量に大きな影響を与える可能性があるからです。このステップでは、特に Python で文字列オブジェクトがどのように扱われるかに焦点を当て、大規模なデータセットのメモリ使用量を最適化する方法を探索します。

## データセット内の文字列の繰り返し

CTA バスデータには、路線名などの多くの繰り返し値が含まれています。データセット内の繰り返し値は、適切に処理されない場合、メモリの非効率的な使用につながる可能性があります。この問題の程度を理解するために、まずデータセット内に何種類の一意の路線文字列があるかを調べてみましょう。

まず、Python インタープリタを開きます。ターミナルで以下のコマンドを実行することで、これを行うことができます。

```bash
python3
```

Python インタープリタが開いたら、CTA バスデータを読み込み、一意の路線を見つけます。これを実現するためのコードは以下の通りです。

```python
import reader
rows = reader.read_csv_as_dicts('ctabus.csv', [str, str, str, int])

# Find unique route names
routes = {row['route'] for row in rows}
print(f"Number of unique route names: {len(routes)}")
```

このコードでは、まず `reader` モジュールをインポートします。このモジュールには、CSV ファイルを辞書として読み取る関数が含まれていると思われます。次に、`read_csv_as_dicts` 関数を使用して `ctabus.csv` ファイルからデータを読み込みます。2 番目の引数 `[str, str, str, int]` は、CSV ファイルの各列のデータ型を指定します。その後、セット内包表記を使用して、データセット内のすべての一意の路線名を見つけ、一意の路線名の数を出力します。

出力は以下のようになるはずです。

```
Number of unique route names: 181
```

では、これらの路線に対して何種類の異なる文字列オブジェクトが作成されているかを確認しましょう。たとえ一意の路線名が 181 種類しかなくても、Python はデータセット内の路線名の各出現に対して新しい文字列オブジェクトを作成する可能性があります。これを検証するために、`id()` 関数を使用して各文字列オブジェクトの一意の識別子を取得します。

```python
# Count unique string object IDs
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects: {len(routeids)}")
```

出力は驚くかもしれません。

```
Number of unique route string objects: 542305
```

これは、一意の路線名は 181 種類しかないが、50 万を超える一意の文字列オブジェクトが存在することを示しています。これは、Python が値が同じであっても各行に対して新しい文字列オブジェクトを作成するために起こります。これは、特に大規模なデータセットを扱う際に、著しいメモリの浪費につながる可能性があります。

## メモリ節約のための文字列インターニング

Python は、`sys.intern()` 関数を使用して文字列の「インターニング」（再利用）を行う方法を提供しています。データセットに多くの重複する文字列がある場合、文字列インターニングはメモリを節約することができます。文字列にインターニングを適用すると、Python はインターンプール内に同じ文字列が既に存在するかどうかを確認します。存在する場合、新しいオブジェクトを作成する代わりに、既存の文字列オブジェクトへの参照を返します。

文字列インターニングがどのように機能するかを簡単な例で示しましょう。

```python
import sys

# Without interning
a = 'hello world'
b = 'hello world'
print(f"a is b (without interning): {a is b}")

# With interning
a = sys.intern(a)
b = sys.intern(b)
print(f"a is b (with interning): {a is b}")
```

このコードでは、まずインターニングを行わずに同じ値を持つ 2 つの文字列変数 `a` と `b` を作成します。`is` 演算子は、2 つの変数が同じオブジェクトを参照しているかどうかをチェックします。インターニングを行わない場合、`a` と `b` は異なるオブジェクトであるため、`a is b` は `False` を返します。次に、`sys.intern()` を使用して両方の文字列にインターニングを適用します。インターニングの後、`a` と `b` はインターンプール内の同じオブジェクトを参照するため、`a is b` は `True` を返します。

出力は以下のようになるはずです。

```
a is b (without interning): False
a is b (with interning): True
```

では、CTA バスデータを読み取る際に文字列インターニングを使用して、メモリ使用量を削減しましょう。また、`tracemalloc` モジュールを使用して、インターニングの前後のメモリ使用量を追跡します。

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for the route column
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, str, str, int])

# Check unique route objects again
routeids = {id(row['route']) for row in rows}
print(f"Number of unique route string objects (with interning): {len(routeids)}")

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

このコードでは、まず `tracemalloc.start()` を使用してメモリ追跡を開始します。次に、最初の列のデータ型として `sys.intern` を渡すことで、路線列にインターニングを適用して CTA バスデータを読み取ります。その後、再度一意の路線文字列オブジェクトの数を確認し、現在のメモリ使用量とピークメモリ使用量を出力します。

出力は以下のようになるはずです。

```
Number of unique route string objects (with interning): 181
Current memory usage: 189.56 MB
Peak memory usage: 209.32 MB
```

インタープリタを再起動し、路線と日付の両方の文字列にインターニングを適用して、メモリ使用量をさらに削減できるかどうかを試してみましょう。

```python
exit()
```

再度 Python を起動します。

```bash
python3
```

```python
import sys
import reader
import tracemalloc

# Start memory tracking
tracemalloc.start()

# Read data with interning for both route and date columns
rows = reader.read_csv_as_dicts('ctabus.csv', [sys.intern, sys.intern, str, int])

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage (interning route and date): {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage (interning route and date): {peak / 1024 / 1024:.2f} MB")
```

出力は、メモリ使用量がさらに減少していることを示すはずです。

```
Current memory usage (interning route and date): 170.23 MB
Peak memory usage (interning route and date): 190.05 MB
```

これは、Python のメモリモデルを理解し、文字列インターニングなどの技術を使用することで、特に繰り返し値を含む大規模なデータセットを扱う際に、プログラムを最適化するのに役立つことを示しています。

最後に、Python インタープリタを終了します。

```python
exit()
```
