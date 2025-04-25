# ジェネレータ式とメモリ効率

このステップでは、ジェネレータ式について探索します。Python で大規模なデータセットを扱う際に、これらは非常に便利です。ジェネレータ式を使うと、コードのメモリ効率を大幅に向上させることができ、大量のデータを扱う際には非常に重要です。

## ジェネレータ式の理解

ジェネレータ式はリスト内包表記に似ていますが、重要な違いがあります。リスト内包表記を使うと、Python はすべての結果を一度に含むリストを作成します。これは、特に大規模なデータセットを扱う場合、大量のメモリを消費することがあります。一方、ジェネレータ式は必要になったときに結果を 1 つずつ生成します。つまり、すべての結果を一度にメモリに格納する必要がないため、かなりのメモリを節約することができます。

これがどのように機能するかを見るために、簡単な例を見てみましょう。

```python
# Start a new Python session if needed
# python3

# List comprehension (creates a list in memory)
nums = [1, 2, 3, 4, 5]
squares_list = [x*x for x in nums]
print(squares_list)

# Generator expression (creates a generator object)
squares_gen = (x*x for x in nums)
print(squares_gen)  # This doesn't print the values, just the generator object

# Iterate through the generator to get values
for n in squares_gen:
    print(n)
```

このコードを実行すると、以下の出力が表示されます。

```
[1, 4, 9, 16, 25]
<generator object <genexpr> at 0x7f...>
1
4
9
16
25
```

ジェネレータに関して重要なことは、一度しか反復処理できないということです。ジェネレータ内のすべての値を処理した後は、そのジェネレータは枯渇し、再度値を取得することはできません。

```python
# Try to iterate again over the same generator
for n in squares_gen:
    print(n)  # Nothing will be printed, as the generator is already exhausted
```

`next()` 関数を使って、ジェネレータから値を 1 つずつ手動で取得することもできます。

```python
# Create a fresh generator
squares_gen = (x*x for x in nums)

# Get values one by one
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
print(next(squares_gen))  # 9
```

ジェネレータに値が残っていない場合、`next()` を呼び出すと `StopIteration` 例外が発生します。

## yield を使ったジェネレータ関数

より複雑なジェネレータロジックには、`yield` 文を使ってジェネレータ関数を書くことができます。ジェネレータ関数は、一度に単一の結果を返すのではなく、`yield` を使って値を 1 つずつ返す特殊な関数です。

```python
def squares(nums):
    for x in nums:
        yield x*x

# Use the generator function
for n in squares(nums):
    print(n)
```

このコードを実行すると、以下の出力が表示されます。

```
1
4
9
16
25
```

## ジェネレータ式によるメモリ使用量の削減

では、大規模なデータセットを扱う際に、ジェネレータ式がどのようにメモリを節約できるかを見てみましょう。非常に大きい CTA バスデータファイルを使用します。

まず、メモリを大量に消費するアプローチを試してみましょう。

```python
import tracemalloc
tracemalloc.start()

import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')
rt22 = [row for row in rows if row['route'] == '22']
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

次に、Python を終了して再起動し、ジェネレータベースのアプローチと比較します。

```bash
exit() python3
```

```python
import tracemalloc
tracemalloc.start()

import csv
f = open('ctabus.csv')
f_csv = csv.reader(f)
headers = next(f_csv)

# Use generator expressions for all operations
rows = (dict(zip(headers, row)) for row in f_csv)
rt22 = (row for row in rows if row['route'] == '22')
max_row = max(rt22, key=lambda row: int(row['rides']))
print(max_row)

# Check memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

これら 2 つのアプローチのメモリ使用量には大きな違いがあることに気づくはずです。ジェネレータベースのアプローチは、すべてのデータを一度にメモリにロードすることなく、データを逐次処理するため、はるかにメモリ効率が良いです。

## 集約関数との組み合わせによるジェネレータ式の活用

ジェネレータ式は、`sum()`、`min()`、`max()`、`any()`、`all()` などの、シーケンス全体を処理して単一の結果を生成する関数と組み合わせると特に便利です。

いくつかの例を見てみましょう。

```python
from readport import read_portfolio
portfolio = read_portfolio('portfolio.csv')

# Calculate the total value of the portfolio
total_value = sum(s['shares']*s['price'] for s in portfolio)
print(f"Total portfolio value: {total_value}")

# Find the minimum number of shares in any holding
min_shares = min(s['shares'] for s in portfolio)
print(f"Minimum shares in any holding: {min_shares}")

# Check if any stock is IBM
has_ibm = any(s['name'] == 'IBM' for s in portfolio)
print(f"Portfolio contains IBM: {has_ibm}")

# Check if all stocks are IBM
all_ibm = all(s['name'] == 'IBM' for s in portfolio)
print(f"All stocks are IBM: {all_ibm}")

# Count IBM shares
ibm_shares = sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
print(f"Total IBM shares: {ibm_shares}")
```

ジェネレータ式は文字列操作にも便利です。タプル内の値を結合する方法を見てみましょう。

```python
s = ('GOOG', 100, 490.10)
# This would fail: ','.join(s)
# Use a generator expression to convert all items to strings
joined = ','.join(str(x) for x in s)
print(joined)  # Output: 'GOOG,100,490.1'
```

これらの例でジェネレータ式を使う主な利点は、中間リストが作成されないため、メモリ効率の高いコードになることです。
