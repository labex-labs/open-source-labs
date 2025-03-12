# 列指向データによるメモリ最適化

従来のデータストレージでは、各レコードを個別の辞書として格納することが多く、これは行指向アプローチと呼ばれます。しかし、この方法はかなりの量のメモリを消費する可能性があります。別の方法は、データを列で格納することです。列指向アプローチでは、各属性に対して個別のリストを作成し、各リストにはその特定の属性のすべての値が格納されます。これにより、メモリを節約することができます。

1. まず、プロジェクトディレクトリに新しい Python ファイルを作成する必要があります。このファイルには、列指向でデータを読み取るためのコードが含まれます。ファイル名を `readrides.py` とします。これを実現するには、ターミナルで以下のコマンドを使用できます。

```bash
cd ~/project
touch readrides.py
```

`cd ~/project` コマンドは、現在のディレクトリをプロジェクトディレクトリに変更し、`touch readrides.py` コマンドは `readrides.py` という名前の新しい空のファイルを作成します。

2. 次に、WebIDE エディタで `readrides.py` ファイルを開きます。そして、以下の Python コードをファイルに追加します。このコードは、`read_rides_as_columns` 関数を定義しており、CSV ファイルからバスの乗車データを読み取り、それを 4 つの個別のリストに格納します。各リストはデータの列を表します。

```python
# readrides.py
import csv
import sys
import tracemalloc

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)
```

このコードでは、まず必要なモジュール `csv`、`sys`、および `tracemalloc` をインポートしています。`csv` モジュールは CSV ファイルを読み取るために使用され、`sys` はシステム関連の操作に使用できます（ただし、この関数では使用されていません）。`tracemalloc` はメモリプロファイリングに使用されます。関数内では、データの異なる列を格納するために 4 つの空のリストを初期化します。その後、ファイルを開き、ヘッダー行をスキップし、ファイル内の各行を反復処理して、対応する値を適切なリストに追加します。最後に、これら 4 つのリストを含む辞書を返します。

3. では、列指向アプローチがなぜメモリを節約できるのかを分析しましょう。これは Python シェルで行います。以下のコードを実行します。

```python
import readrides
import tracemalloc

# Estimate memory for row-oriented approach
nrows = 577563     # Number of rows in original file
dict_overhead = 240  # Approximate dictionary overhead in bytes
row_memory = nrows * dict_overhead
print(f"Estimated memory for row-oriented data: {row_memory} bytes ({row_memory/1024/1024:.2f} MB)")

# Estimate memory for column-oriented approach
pointer_size = 8   # Size of a pointer in bytes on 64-bit systems
column_memory = nrows * 4 * pointer_size  # 4 columns with one pointer per entry
print(f"Estimated memory for column-oriented data: {column_memory} bytes ({column_memory/1024/1024:.2f} MB)")

# Estimate savings
savings = row_memory - column_memory
print(f"Estimated memory savings: {savings} bytes ({savings/1024/1024:.2f} MB)")
```

このコードでは、まず先ほど作成した `readrides` モジュールと `tracemalloc` モジュールをインポートします。そして、行指向アプローチのメモリ使用量を見積もります。各辞書のオーバーヘッドが 240 バイトであると仮定し、これを元のファイルの行数で乗算して、行指向データの総メモリ使用量を求めます。列指向アプローチの場合、64 ビットシステムで各ポインタが 8 バイトを占めると仮定します。4 つの列があり、各エントリに 1 つのポインタがあるため、列指向データの総メモリ使用量を計算します。最後に、行指向のメモリ使用量から列指向のメモリ使用量を引いて、メモリ節約量を計算します。

この計算により、列指向アプローチは辞書を使用した行指向アプローチに比べて約 120MB のメモリを節約できることがわかります。

4. これを `tracemalloc` モジュールを使用して実際のメモリ使用量を測定することで検証しましょう。以下のコードを実行します。

```python
# Start tracking memory
tracemalloc.start()

# Read the data
columns = readrides.read_rides_as_columns('ctabus.csv')

# Get current and peak memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current/1024/1024:.2f} MB")
print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

# Stop tracking memory
tracemalloc.stop()
```

このコードでは、まず `tracemalloc.start()` を使用してメモリの追跡を開始します。次に、`read_rides_as_columns` 関数を呼び出して `ctabus.csv` ファイルからデータを読み取ります。その後、`tracemalloc.get_traced_memory()` を使用して現在のメモリ使用量とピークメモリ使用量を取得します。最後に、`tracemalloc.stop()` を使用してメモリの追跡を停止します。

出力結果から、列指向データ構造の実際のメモリ使用量がわかります。これは、行指向アプローチの理論上の見積もりよりも大幅に少ないはずです。

大幅なメモリ節約は、何千もの辞書オブジェクトのオーバーヘッドを排除することによって実現されます。Python の各辞書には、含まれるアイテムの数に関係なく固定的なオーバーヘッドがあります。列指向ストレージを使用することで、何千もの辞書の代わりに数個のリストだけが必要になります。
