# はじめに

この実験では、Wikipedia記事内のリンクのグラフを分析して、固有ベクトル中心性に基づいて相対的な重要性によって記事をランキング付けします。主固有ベクトルを計算する従来の方法は、パワー反復法を使用することです。ここでは、scikit-learnで実装されたMartinssonのランダム化SVDアルゴリズムを使用します。

## VMのヒント

VMの起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替えて、Jupyter Notebookを使って練習しましょう。

時々、Jupyter Notebookが読み込み終了するまで数秒待つ必要がある場合があります。Jupyter Notebookの制限により、操作の検証を自動化することはできません。

学習中に問題に直面した場合は、Labbyにお問い合わせください。セッション後にフィードバックを提供してください。すぐに問題を解決いたします。
