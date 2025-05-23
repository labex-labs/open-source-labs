# はじめに

このチュートリアルでは、分類、回帰、アウトライア検出に使用される教師付き学習手法のセットであるサポートベクターマシン（SVM）について学びます。SVM は高次元空間で効果的で、次元数がサンプル数よりも多い場合でも良好な性能を発揮します。

SVM の利点としては、高次元空間での有効性、メモリ効率、およびさまざまなカーネル関数に関する汎用性が挙げられます。ただし、過学習を回避し、与えられた問題に適したカーネルと正則化項を選ぶことが重要です。

このチュートリアルでは、以下のトピックを扱います。

1. SVM による分類
2. 多クラス分類
3. スコアと確率
4. 不均衡問題
5. SVM による回帰
6. 密度推定と新奇性検出

## VM のヒント

VM の起動が完了したら、左上隅をクリックして**ノートブック**タブに切り替え、Jupyter Notebook を使って練習しましょう。

時々、Jupyter Notebook が読み込み終了するまで数秒待つ必要がある場合があります。Jupyter Notebook の制限により、操作の検証を自動化することはできません。

学習中に問題が発生した場合は、Labby にお問い合わせください。セッション後にフィードバックを提供してください。そうすれば、迅速に問題を解決します。
