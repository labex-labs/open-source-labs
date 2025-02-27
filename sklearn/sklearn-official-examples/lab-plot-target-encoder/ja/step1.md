# OpenMLからのデータの読み込み

まず、scikit-learn.datasetsモジュールの`fetch_openml`関数を使ってワインレビューデータセットを読み込みます。データの中では、数値型とカテゴリ型の特徴量のサブセットのみを使用します。データの中では、以下の数値型とカテゴリ型の特徴量のサブセットを使用します：`numerical_features = ["price"]` および `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`。
