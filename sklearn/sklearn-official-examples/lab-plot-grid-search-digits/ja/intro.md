# はじめに

この実験では、scikit-learn ライブラリを使って交差検証によるハイパーパラメータチューニングを行う方法を示します。目的は、分類を容易にするために 2 値分類を使って手書き数字画像を分類することです：数字が 8 であるかどうかを識別することです。使用するデータセットは、digits データセットです。その後、選択されたハイパーパラメータと学習済みモデルの性能を、モデル選択ステップでは使用されなかった専用の評価セットで測定します。

## VM のヒント

VM の起動が完了した後、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebook にアクセスして練習します。

時々、Jupyter Notebook が読み込み終了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題に直面した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。そうすれば、迅速に問題を解決します。
