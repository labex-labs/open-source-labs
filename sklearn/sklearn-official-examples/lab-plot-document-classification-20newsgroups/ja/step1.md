# 20ニュースグループのテキストデータセットの読み込みとベクトル化

20newsgroups_datasetからデータを読み込む関数を定義します。このデータセットは、20のトピックに関する約18,000のニュースグループ投稿から構成されており、2つのサブセットに分割されています。1つは訓練用、もう1つはテスト用です。メタデータを削除せずにデータセットを読み込み、ベクトル化します。

```python
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
    "alt.atheism",
    "talk.religion.misc",
    "comp.graphics",
    "sci.space",
]

def load_dataset(verbose=False, remove=()):
    """20ニュースグループのデータセットを読み込み、ベクトル化します。"""
    data_train = fetch_20newsgroups(
        subset="train",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    data_test = fetch_20newsgroups(
        subset="test",
        categories=categories,
        shuffle=True,
        random_state=42,
        remove=remove,
    )

    # `target_names` のラベルの順序は `categories` と異なる場合があります
    target_names = data_train.target_names

    # 訓練セットとテストセットにターゲットを分割します
    y_train, y_test = data_train.target, data_test.target

    # 疎ベクトル化器を使用して訓練データから特徴を抽出します
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # 同じベクトル化器を使用してテストデータから特徴を抽出します
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)} の文書")
        print(f"{len(data_test.data)} の文書")
        print(f"{len(target_names)} のカテゴリ")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
