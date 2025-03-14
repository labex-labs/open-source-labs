# はじめに

この実験では、PythonのScikit-learnライブラリを使ってガウス過程回帰（GPR）に異なるカーネルをどのように使用するかを示します。GPRは、ノイズのあるデータに複雑なモデルを適合させる非パラメトリック回帰手法です。カーネル関数は、任意の2つの入力点間の類似性を決定するために使用されます。カーネル関数の選択は重要であり、データに適合するモデルの形状を決定します。この実験では、GPRで最も一般的に使用されるカーネルを扱います。

## VMのヒント

VMの起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebookを使った練習にアクセスします。

時々、Jupyter Notebookが読み込み終了するまで数秒待つ必要があります。Jupyter Notebookの制限により、操作の検証を自動化することはできません。

学習中に問題に遭遇した場合は、Labbyにお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
