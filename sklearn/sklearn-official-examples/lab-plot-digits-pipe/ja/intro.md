# はじめに

この実験では、主成分分析 (PCA) とロジスティック回帰を使用して次元削減と分類のパイプラインを構築します。scikit-learn ライブラリを使用して、PCA を使って digits データセットに対して非監督学習による次元削減を行います。その後、分類にはロジスティック回帰モデルを使用します。GridSearchCV を使って PCA の次元を設定し、PCA トランケーションと分類器の正則化の最適な組み合わせを見つけます。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **ノートブック** タブに切り替えて、Jupyter Notebook を使った練習を行います。

時々、Jupyter Notebook が読み込み終わるまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証は自動化できません。

学習中に問題がある場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
