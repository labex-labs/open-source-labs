# 20 뉴스그룹 텍스트 데이터셋 로드 및 벡터화

20 개 주제에 대한 약 18,000 개의 뉴스그룹 게시물로 구성된 20newsgroups 데이터셋에서 데이터를 로드하는 함수를 정의합니다. 이 데이터셋은 학습용과 테스트용 두 개의 하위 집합으로 나뉩니다. 메타데이터 제거 없이 데이터셋을 로드하고 벡터화합니다.

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
    """20 뉴스그룹 데이터셋을 로드하고 벡터화합니다."""
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

    # `target_names` 의 레이블 순서는 `categories` 와 다를 수 있습니다.
    target_names = data_train.target_names

    # 학습용 및 테스트용 데이터셋으로 타겟 분할
    y_train, y_test = data_train.target, data_test.target

    # 희소 벡터화기를 사용하여 학습 데이터에서 특징 추출
    vectorizer = TfidfVectorizer(
        sublinear_tf=True, max_df=0.5, min_df=5, stop_words="english"
    )
    X_train = vectorizer.fit_transform(data_train.data)

    # 동일한 벡터화기를 사용하여 테스트 데이터에서 특징 추출
    X_test = vectorizer.transform(data_test.data)

    feature_names = vectorizer.get_feature_names_out()

    if verbose:
        print(f"{len(data_train.data)}개의 문서")
        print(f"{len(data_test.data)}개의 문서")
        print(f"{len(target_names)}개의 카테고리")
        print(f"n_samples: {X_train.shape[0]}, n_features: {X_train.shape[1]}")
        print(f"n_samples: {X_test.shape[0]}, n_features: {X_test.shape[1]}")

    return X_train, X_test, y_train, y_test, feature_names, target_names

X_train, X_test, y_train, y_test, feature_names, target_names = load_dataset(verbose=True)
```
