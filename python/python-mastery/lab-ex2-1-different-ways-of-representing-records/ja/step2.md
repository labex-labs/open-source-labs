# 異なる保存方法によるメモリ使用量の測定

このステップでは、データの保存方法がメモリ使用量にどのように影響するかを見ていきます。メモリ使用量は、特に大規模なデータセットを扱う場合、プログラミングにおいて重要な要素です。Python コードが使用するメモリを測定するために、Python の `tracemalloc` モジュールを使用します。このモジュールは、Python によるメモリ割り当てを追跡できるため非常に便利です。これを使用することで、データ保存方法がどれだけのメモリを消費しているかを確認できます。

## 方法 1: ファイル全体を単一の文字列として保存する

まず、新しい Python ファイルを作成しましょう。`/home/labex/project` ディレクトリに移動し、`memory_test1.py` という名前のファイルを作成します。テキストエディタを使用してこのファイルを開きます。ファイルを開いたら、以下のコードを追加します。このコードは、ファイルの内容全体を単一の文字列として読み込み、メモリ使用量を測定します。

```python
# memory_test1.py
import tracemalloc

def test_single_string():
    # メモリの追跡を開始する
    tracemalloc.start()

    # ファイル全体を単一の文字列として読み込む
    with open('/home/labex/project/ctabus.csv') as f:
        data = f.read()

    # メモリ使用量の統計を取得する
    current, peak = tracemalloc.get_traced_memory()

    print(f"File length: {len(data)} characters")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # メモリの追跡を停止する
    tracemalloc.stop()

if __name__ == "__main__":
    test_single_string()
```

コードを追加したら、ファイルを保存します。次に、このスクリプトを実行するには、ターミナルを開き、以下のコマンドを実行します。

```bash
python3 /home/labex/project/memory_test1.py
```

スクリプトを実行すると、以下のような出力が表示されるはずです。

```
File length: 12361039 characters
Current memory usage: 11.80 MB
Peak memory usage: 23.58 MB
```

正確な数値はシステムによって異なる場合がありますが、一般的には、現在のメモリ使用量が約 12 MB、ピークメモリ使用量が約 24 MB となります。

## 方法 2: 文字列のリストとして保存する

次に、別のデータ保存方法をテストします。同じ `/home/labex/project` ディレクトリに `memory_test2.py` という名前の新しいファイルを作成します。エディタでこのファイルを開き、以下のコードを追加します。このコードは、ファイルを読み込み、各行を別々の文字列としてリストに保存し、メモリ使用量を測定します。

```python
# memory_test2.py
import tracemalloc

def test_list_of_strings():
    # メモリの追跡を開始する
    tracemalloc.start()

    # ファイルを文字列のリストとして読み込む（1 行ごとに 1 つの文字列）
    with open('/home/labex/project/ctabus.csv') as f:
        lines = f.readlines()

    # メモリ使用量の統計を取得する
    current, peak = tracemalloc.get_traced_memory()

    print(f"Number of lines: {len(lines)}")
    print(f"Current memory usage: {current/1024/1024:.2f} MB")
    print(f"Peak memory usage: {peak/1024/1024:.2f} MB")

    # メモリの追跡を停止する
    tracemalloc.stop()

if __name__ == "__main__":
    test_list_of_strings()
```

ファイルを保存し、ターミナルで以下のコマンドを使用してスクリプトを実行します。

```bash
python3 /home/labex/project/memory_test2.py
```

以下のような出力が表示されるはずです。

```
Number of lines: 577564
Current memory usage: 43.70 MB
Peak memory usage: 43.74 MB
```

データを単一の文字列として保存する前の方法と比較すると、メモリ使用量が大幅に増加していることに注意してください。これは、リスト内の各行が別々の Python 文字列オブジェクトであり、各オブジェクトには独自のメモリオーバーヘッドがあるためです。

## メモリ使用量の違いを理解する

2 つのアプローチ間のメモリ使用量の違いは、Python プログラミングにおけるオブジェクトオーバーヘッドと呼ばれる重要な概念を示しています。データを文字列のリストとして保存する場合、各文字列は別々の Python オブジェクトです。各オブジェクトには、以下を含むいくつかの追加のメモリ要件があります。

1. Python オブジェクトヘッダー（通常、オブジェクトごとに 16 - 24 バイト）。このヘッダーには、オブジェクトのタイプや参照カウントなどの情報が含まれています。
2. 文字列自体の実際の表現で、文字列の文字を格納します。
3. メモリアライメントパディング。これは、オブジェクトのメモリアドレスが効率的なアクセスのために適切にアライメントされるように追加される余分なスペースです。

一方、ファイルの内容全体を単一の文字列として保存する場合、オブジェクトは 1 つだけであり、したがってオーバーヘッドも 1 セットだけです。これにより、データの総サイズを考慮すると、メモリ効率が向上します。

大規模なデータセットを扱うプログラムを設計する際には、メモリ効率とデータのアクセス性の間のトレードオフを考慮する必要があります。場合によっては、データを文字列のリストとして保存するとアクセスが便利になることがありますが、メモリをより多く使用します。他の場合には、メモリ効率を優先して、データを単一の文字列として保存することがあります。
