# 데이터 로드

20 개의 서로 다른 카테고리에 걸쳐 약 20,000 개의 뉴스그룹 문서가 모인 20newsgroups 데이터셋을 로드합니다. 이 실습에서는 alt.atheism 및 talk.religion.misc 두 가지 카테고리에 집중합니다.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "talk.religion.misc",
]

data_train = fetch_20newsgroups(
    subset="train",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

data_test = fetch_20newsgroups(
    subset="test",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

print(f"Loading 20 newsgroups dataset for {len(data_train.target_names)} categories:")
print(data_train.target_names)
print(f"{len(data_train.data)} documents")
```
