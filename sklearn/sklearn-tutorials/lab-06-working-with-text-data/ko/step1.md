# 텍스트 데이터 로드

먼저, 작업할 텍스트 데이터를 로드해야 합니다. 20 개의 서로 다른 주제의 뉴스 기사를 포함하는 20 개 뉴스그룹 (20 Newsgroups) 데이터셋을 사용할 것입니다. 데이터셋을 로드하려면 scikit-learn 의 `fetch_20newsgroups` 함수를 사용할 수 있습니다.

```python
from sklearn.datasets import fetch_20newsgroups

# 데이터셋 로드
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
```

이제 데이터를 로드했으므로 데이터의 구조와 내용을 살펴볼 수 있습니다.
