# はじめに

このチュートリアルでは、scikit-learn でカーネル近似手法を使用するプロセスを案内します。

サポートベクターマシン (SVM) などのカーネル手法は、非線形分類に強力な手法です。これらの手法は、入力データを高次元特徴空間にマッピングするカーネル関数の概念に依存しています。ただし、明示的な特徴マッピングを使用すると、計算コストが高くなる場合があり、特に大規模なデータセットの場合です。カーネル近似手法は、カーネル特徴空間の低次元近似を生成することで解決策を提供します。

このチュートリアルでは、scikit-learn で利用可能ないくつかのカーネル近似手法を検討します。これには、ニストローム法、ラジアルベーシス関数 (RBF) カーネル近似、加算チカ二乗 (ACS) カーネル近似、歪チカ二乗 (SCS) カーネル近似、およびテンソルスケッチを使用した多項式カーネル近似が含まれます。これらの手法の使用方法を示し、その利点と制限について説明します。

## VM のヒント

VM の起動が完了したら、左上隅をクリックして **ノートブック** タブに切り替え、Jupyter Notebook を使用して練習します。

場合によっては、Jupyter Notebook が読み込み完了するまで数秒待つ必要があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題が発生した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。そうすると、迅速に問題を解決します。
