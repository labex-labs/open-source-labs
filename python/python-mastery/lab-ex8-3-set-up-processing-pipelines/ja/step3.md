# コルーチンパイプラインの拡張

基本的なパイプラインが稼働したので、これをより柔軟にする時が来ました。プログラミングにおいて、柔軟性はコードが様々な要件に適応できるため、非常に重要です。これを実現するために、`coticker.py`プログラムを修正して、様々なフィルタリングとフォーマットオプションをサポートするようにします。

1. まず、コードエディタで`coticker.py`ファイルを開きます。コードエディタは、プログラムに必要なすべての変更を加える場所です。コードを表示、編集、保存する便利な環境を提供します。

2. 次に、株式名でデータをフィルタリングする新しいコルーチンを追加します。コルーチンは、実行を一時停止して再開できる特殊なタイプの関数です。これにより、データがさまざまな処理ステップを流れるパイプラインを作成することができます。以下は新しいコルーチンのコードです。

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

このコードでは、`filter_by_name`コルーチンは株式名とターゲットコルーチンをパラメータとして受け取ります。`yield`キーワードを使用してレコードを待ち続けます。レコードが到着すると、レコードの名前が指定された名前と一致するかどうかをチェックします。一致する場合は、レコードをターゲットコルーチンに送信します。

3. 次に、価格の閾値に基づいてフィルタリングする別のコルーチンを追加しましょう。このコルーチンは、特定の価格範囲内の株式を選択するのに役立ちます。以下はコードです。

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

前のコルーチンと同様に、`price_threshold`コルーチンはレコードを待ちます。そして、レコードの価格が指定された最小価格と最大価格の範囲内にあるかどうかをチェックします。範囲内にある場合は、レコードをターゲットコルーチンに送信します。

4. 新しいコルーチンを追加した後、これらの追加フィルタを実証するためにメインプログラムを更新する必要があります。メインプログラムはアプリケーションのエントリポイントで、処理パイプラインを設定し、データの流れを開始します。以下は更新後のコードです。

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

この更新されたコードでは、3 つの異なる処理パイプラインを作成しています。最初のパイプラインは価格が下落している株式を表示し、2 番目のパイプラインは名前が'AAPL'の株式をフィルタリングし、3 番目のパイプラインは価格が 50 から 75 の間の株式をフィルタリングします。スレッドを使用して最初の 2 つのパイプラインを同時に実行し、データをより効率的に処理できるようにしています。

5. すべての変更を加えたら、ファイルを保存します。ファイルを保存することで、すべての変更が保存されます。次に、ターミナルで以下のコマンドを使用して更新されたプログラムを実行します。

```bash
cd /home/labex/project
python3 coticker.py
```

`cd`コマンドは現在のディレクトリをプロジェクトディレクトリに変更し、`python3 coticker.py`コマンドは Python プログラムを実行します。

6. プログラムを実行した後、3 つの異なる出力が表示されるはずです。
   - まず、価格が下落している株式が表示されます。
   - 次に、すべての AAPL 株式の更新情報が表示されます。
   - 最後に、価格が 50 から 75 の間のすべての株式が表示されます。

## 拡張されたパイプラインの理解

拡張されたプログラムはいくつかの重要な概念を示しています。

1. **複数のパイプライン**：同じデータソースから複数の処理パイプラインを作成することができます。これにより、同じデータに対して異なるタイプの分析を同時に行うことができます。
2. **特殊なフィルタ**：特定のフィルタリングタスクのために異なるコルーチンを作成することができます。これらのフィルタは、特定の基準を満たすデータのみを選択するのに役立ちます。
3. **並行処理**：スレッドを使用して、複数のパイプラインを同時に実行することができます。これにより、データを並列に処理できるため、プログラムの効率が向上します。
4. **パイプラインの構成**：コルーチンをさまざまな方法で組み合わせて、異なるデータ処理の目標を達成することができます。これにより、必要に応じてデータ処理パイプラインをカスタマイズする柔軟性が得られます。

このアプローチは、ストリーミングデータを柔軟かつモジュール化された方法で処理する手段を提供します。プログラムの全体的なアーキテクチャを変更することなく、処理ステップを追加または変更することができます。
