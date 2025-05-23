# はじめに

この手順に従った実験では、Matplotlib における日付の精度とエポックの扱い方を示します。Matplotlib は、これらの日付を認識して浮動小数点数に変換する単位変換機を使用して、`.datetime`オブジェクトと`numpy.datetime64`オブジェクトと共に動作することができます。Matplotlib 3.3 以前では、この変換のデフォルトは、「0000-12-31T00:00:00」からの日数を返す浮動小数点数でした。Matplotlib 3.3 以降では、デフォルトは「1970-01-01T00:00:00」からの日数です。これにより、現代の日付に対してより高い解像度が可能になります。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

Jupyter Notebook が読み込み終わるまで数秒待つことがあります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題がある場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
