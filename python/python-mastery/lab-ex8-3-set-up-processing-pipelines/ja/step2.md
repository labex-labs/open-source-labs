# コルーチンパイプラインコンポーネントの作成

このステップでは、株式データを処理するためのより特殊なコルーチンを作成します。コルーチンは、実行を一時停止して再開できる特殊なタイプの関数であり、データ処理パイプラインの構築に非常に役立ちます。作成する各コルーチンは、全体の処理パイプラインの中で特定のタスクを実行します。

1. まず、新しいファイルを作成する必要があります。`/home/labex/project`ディレクトリに移動し、`coticker.py`という名前のファイルを作成します。このファイルには、コルーチンベースのデータ処理に関するすべてのコードが含まれます。

2. 次に、`coticker.py`ファイルにコードを書き始めましょう。まず、必要なモジュールをインポートし、基本構造を定義します。モジュールは、便利な関数やクラスを提供する事前に書かれたコードライブラリです。以下のコードがその役割を果たします。

```python
# coticker.py
from structure import Structure

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

3. 上記のコードを見ると、`String()`、`Float()`、`Integer()`に関連するエラーがあることに気づくでしょう。これらはインポートする必要があるクラスです。そのため、ファイルの先頭に必要なインポートを追加します。これにより、Pythonはこれらのクラスの場所を知ることができます。以下は更新後のコードです。

```python
# coticker.py
from structure import Structure, String, Float, Integer

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow
from tableformat import create_formatter
import csv
```

4. 次に、データ処理パイプラインを形成するコルーチンコンポーネントを追加します。各コルーチンは、パイプライン内で特定の役割を持っています。以下はこれらのコルーチンを追加するコードです。

```python
@consumer
def to_csv(target):
    def producer():
        while True:
            line = yield

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
```

5. これらの各コルーチンが何をするかを理解しましょう。

   - `to_csv`: このコルーチンの役割は、生のテキスト行を解析されたCSV行に変換することです。これは、データが最初はテキスト形式であり、構造化されたCSVデータに分割する必要があるため重要です。
   - `create_ticker`: このコルーチンは、CSV行を受け取り、それらから`Ticker`オブジェクトを作成します。`Ticker`オブジェクトは、株式データをより整理された方法で表します。
   - `negchange`: このコルーチンは、`Ticker`オブジェクトをフィルタリングします。価格が下落している株式のみを通過させます。これにより、価値が低下している株式に焦点を当てることができます。
   - `ticker`: このコルーチンは、ティッカーデータを整形して表示します。フォーマッタを使用して、データを見やすい表形式で表示します。

6. 最後に、これらすべてのコンポーネントを接続するメインプログラムコードを追加する必要があります。このコードは、パイプラインを通じたデータの流れを設定します。以下はそのコードです。

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change']

    # Create the processing pipeline
    t = ticker('text', fields)
    neg_filter = negchange(t)
    tick_creator = create_ticker(neg_filter)
    csv_parser = to_csv(tick_creator)

    # Connect the pipeline to the data source
    follow('stocklog.csv', csv_parser)
```

7. すべてのコードを書いた後、`coticker.py`ファイルを保存します。次に、ターミナルを開き、以下のコマンドを実行します。`cd`コマンドは、ファイルが保存されているディレクトリに移動し、`python3`コマンドはPythonスクリプトを実行します。

```bash
cd /home/labex/project
python3 coticker.py
```

8. すべてがうまくいけば、ターミナルに整形された表が表示されるはずです。この表は、価格が下落している株式を示しています。出力は次のようになります。

```
      name      price     change
---------- ---------- ----------
      MSFT      72.50      -0.25
        AA      35.25      -0.15
       IBM      50.10      -0.15
      GOOG     100.02      -0.01
      AAPL     102.50      -0.06
```

表の実際の値は、生成される株式データによって異なることに注意してください。

## パイプラインの流れの理解

このプログラムの最も重要な部分は、データがコルーチンを通じてどのように流れるかです。以下に、その流れを段階的に説明します。

1. `follow`関数は、`stocklog.csv`ファイルから行を読み取り始めます。これがデータソースです。
2. 読み取られた各行は、`csv_parser`コルーチンに送信されます。`csv_parser`は、生のテキスト行を受け取り、それをCSVフィールドに解析します。
3. 解析されたCSVデータは、`tick_creator`コルーチンに送信されます。このコルーチンは、CSV行から`Ticker`オブジェクトを作成します。
4. `Ticker`オブジェクトは、`neg_filter`コルーチンに送信されます。このコルーチンは、各`Ticker`オブジェクトをチェックします。株式の価格が下落している場合、オブジェクトを通過させます。そうでない場合は、破棄します。
5. 最後に、フィルタリングされた`Ticker`オブジェクトは、`ticker`コルーチンに送信されます。`ticker`コルーチンは、データを整形し、表形式で表示します。

このパイプラインアーキテクチャは、各コンポーネントが単一のタスクに集中できるため非常に便利です。これにより、コードがよりモジュール化され、理解、変更、および保守が容易になります。
