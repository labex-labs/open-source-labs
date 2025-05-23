# 対話型実験

Python には、コードをすぐに実行できる対話型モードがあります。これは、コードのテストや新しいことの試行に非常に便利です。このステップでは、Python インタープリターから直接関数を呼び出す方法を学びます。

## 対話型モードで Python を実行する

Python スクリプトを実行してから対話型モードに入るには、`-i` フラグを使用できます。このフラグは、Python にスクリプトの実行後も対話型状態で実行を続けるよう指示します。以下はその方法です。

```bash
cd /home/labex/project
python3 -i pcost.py
```

このコマンドが行うことを分解してみましょう。

1. まず、`cd /home/labex/project` は現在のディレクトリを `/home/labex/project` に変更します。ここに `pcost.py` スクリプトがあります。
2. 次に、`python3 -i pcost.py` が `pcost.py` スクリプトを実行します。スクリプトの実行が終了した後、Python は対話型モードのままになります。
3. 対話型モードでは、Python コマンドを直接ターミナルに入力できます。

コマンドを実行すると、`pcost.py` スクリプトの出力が表示され、その後に Python プロンプト (`>>>`) が表示されます。このプロンプトは、Python コマンドを入力できることを示しています。

## 対話的に関数を呼び出す

対話型モードに入ると、`portfolio_cost()` 関数を異なるファイル名で呼び出すことができます。これにより、様々な入力に対する関数の動作を確認できます。以下は例です。

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

この対話型アプローチを使用すると、以下のことができます。

- 異なる入力で関数をテストし、期待どおりに動作するかを確認できます。
- 様々な条件下での関数の動作を実験できます。
- 関数呼び出しの即時結果を見ることで、コードを即座にデバッグできます。

## 対話型モードの利点

対話型モードにはいくつかの利点があります。

1. 毎回全体のスクリプトを実行する必要なく、さまざまなシナリオをすばやくテストできます。
2. 変数や式の結果をすぐに調べることができ、コード内で何が起こっているかを理解するのに役立ちます。
3. 完全なプログラムを作成することなく、小さなコード片をテストできます。これは学習や新しいアイデアの試行に最適です。
4. 即座にフィードバックが得られるため、Python の学習や実験に優れた方法です。

## 対話型モードを終了する

実験が終わったら、2 つの方法で対話型モードを終了できます。

- `exit()` と入力して Enter キーを押します。これは対話型セッションを終了する簡単な方法です。
- Ctrl+D（Unix/Linux の場合）を押します。これは対話型モードを終了するショートカットです。

Python のプログラミングの旅を通じて、関数を定義し、対話的にテストする手法は、開発とデバッグに非常に役立ちます。これにより、コードをすばやく反復し、問題を見つけて修正することができます。
