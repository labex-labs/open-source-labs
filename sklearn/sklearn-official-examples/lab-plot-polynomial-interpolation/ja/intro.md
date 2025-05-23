# はじめに

この実験では、リッジ回帰を使ってある次数までの多項式で関数を近似する方法を学びます。1 次元の点 `x_i` の `n_samples` が与えられたとき、これを行う 2 つの異なる方法を示します。

1. `PolynomialFeatures`：指定された次数までのすべての単項式を生成します。これにより、`n_samples` 行と `degree + 1` 列のヴァンデルモンド行列が得られます。
2. `SplineTransformer`：B スプライン基底関数を生成します。B スプラインの基底関数は、次数 `degree` の逐次多項式関数で、`degree+1` 個の連続するノットの間のみ非ゼロです。

非線形特徴を追加するために `make_pipeline` 関数を使い、線形モデルで非線形効果をモデル化するのにこれらの変換器がどのように適しているかを示します。関数、訓練点、および多項式特徴と B スプラインを使った補間を描画します。また、両方の変換器のすべての列を個別に描画し、スプラインのノットを表示します。最後に、周期スプラインの使用方法を示します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **ノートブック** タブに切り替えて、Jupyter Notebook を使って練習します。

時々、Jupyter Notebook が読み込み終了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題に遭遇した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
