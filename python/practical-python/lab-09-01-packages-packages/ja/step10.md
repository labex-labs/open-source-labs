# アプリケーション構造

コードの組織化とファイル構造は、アプリケーションの保守性にとって重要です。

Python には「万能」のアプローチはありません。ただし、多くの問題に対応できる構造の 1 つは、次のようなものです。

```code
porty-app/
  README.txt
  script.py         # スクリプト
  porty/
    # ライブラリコード
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

トップレベルの `porty-app` は、その他のすべてのもの（ドキュメント、トップレベルのスクリプト、サンプルなど）のコンテナです。

再び、トップレベルのスクリプト（あれば）はコードパッケージの外に存在する必要があります。1 階層上に。

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

この時点で、いくつかのプログラムが含まれるディレクトリがあります。

    pcost.py          # ポートフォリオのコストを計算する
    report.py         # レポートを作成する
    ticker.py         # リアルタイムの株価チェッカーを生成する

他の機能を持つさまざまなサポートモジュールがあります。

    stock.py          # 株式クラス
    portfolio.py      # ポートフォリオクラス
    fileparse.py      # CSV解析
    tableformat.py    # フォーマットされたテーブル
    follow.py         # ログファイルを追跡する
    typedproperty.py  # 型付きのクラスプロパティ

このチャレンジでは、コードを整理して共通のパッケージに入れます。
