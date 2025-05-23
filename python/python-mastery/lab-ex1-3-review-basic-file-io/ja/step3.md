# データの処理

ファイルの読み取り方法を学んだので、次のステップは、ファイルの各行を処理して、各株式購入のコストを計算することです。これは、Python でデータを扱う上で重要な部分であり、ファイルから有意義な情報を抽出することができます。

ファイルの各行は特定の形式に従っています：`[株式シンボル] [株式数] [1株あたりの価格]`。各株式購入のコストを計算するには、各行から株式数と 1 株あたりの価格を抽出する必要があります。そして、これら 2 つの値を掛け合わせて、その特定の株式購入のコストを求めます。最後に、このコストを累計に加えて、ポートフォリオの総コストを求めます。

これを実現するために、`pcost.py` ファイルの `portfolio_cost()` 関数を修正しましょう。以下は修正後のコードです。

```python
def portfolio_cost(filename):
    """
    ポートフォリオファイルの総コスト (株式数*価格) を計算する
    """
    total_cost = 0.0

    # ファイルを開く
    with open(filename, 'r') as file:
        # ファイル内のすべての行を読み取る
        for line in file:
            # 先頭と末尾の空白を削除する
            line = line.strip()

            # 空行をスキップする
            if not line:
                continue

            # 行をフィールドに分割する
            fields = line.split()

            # 関連するデータを抽出する
            # fields[0] は株式シンボル (計算には必要ない)
            shares = int(fields[1])  # 株式数 (2 番目のフィールド)
            price = float(fields[2])  # 1 株あたりの価格 (3 番目のフィールド)

            # この株式購入のコストを計算する
            cost = shares * price

            # 総コストに追加する
            total_cost += cost

            # デバッグ情報を表示する
            print(f'{fields[0]}: {shares} 株、価格 ${price:.2f} = 合計 ${cost:.2f}')

    # 総コストを返す
    return total_cost
```

この修正後の関数がどのように動作するかをステップごとに分解してみましょう。

1. **空白を削除する**: `strip()` メソッドを使用して、各行の先頭と末尾の空白を削除します。これにより、行をフィールドに分割する際に余分な空白を誤って含めないようになります。
2. **空行をスキップする**: 行が空の場合 (つまり、空白のみを含む場合)、`continue` 文を使用してその行をスキップします。これにより、空行を分割しようとしたときのエラーを回避できます。
3. **行をフィールドに分割する**: `split()` メソッドを使用して、各行を空白を基準にフィールドのリストに分割します。これにより、行の各部分に個別にアクセスできるようになります。
4. **関連するデータを抽出する**: フィールドのリストから株式数と 1 株あたりの価格を抽出します。株式数は 2 番目のフィールドで、1 株あたりの価格は 3 番目のフィールドです。これらの値を適切なデータ型 (`株式数は int、価格は float`) に変換して、算術演算を行えるようにします。
5. **コストを計算する**: 株式数に 1 株あたりの価格を掛けて、この株式購入のコストを計算します。
6. **総コストに追加する**: この株式購入のコストを累計の総コストに追加します。
7. **デバッグ情報を表示する**: 各株式購入に関する情報を表示して、何が起こっているかを確認します。これには、株式シンボル、株式数、1 株あたりの価格、および購入の総コストが含まれます。

それでは、このコードが動作するかどうかを確認するために実行しましょう。ターミナルを開き、以下のコマンドを実行します。

```bash
python3 ~/project/pcost.py
```

コマンドを実行した後、各株式購入に関する詳細情報が表示され、その後にポートフォリオの総コストが表示されるはずです。この出力により、関数が正しく動作していること、および総コストが正確に計算されていることを確認できます。
