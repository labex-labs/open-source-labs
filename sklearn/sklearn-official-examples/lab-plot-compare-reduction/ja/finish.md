# まとめ

この実験では、scikit-learn の `Pipeline` と `GridSearchCV` を使用して、単一の交差検証実行でさまざまな種類の推定器を最適化しました。また、キャッシュを有効にするために `memory` 引数を使用して特定のトランスフォーマーの状態を保存する方法を示しました。トランスフォーマーの適合にコストがかかる場合、これは特に役立ちます。
