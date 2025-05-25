# 데이터셋 로드

20 뉴스그룹 데이터셋을 로드하고 벡터화합니다. 불필요한 용어를 조기에 걸러내기 위해 몇 가지 휴리스틱을 사용합니다. 게시물에서 헤더, 푸터, 인용 답변을 제거하고, 일반적인 영어 단어, 단일 문서에만 나타나는 단어 또는 최소 95% 의 문서에 나타나는 단어를 제거합니다.

```python
from sklearn.datasets import fetch_20newsgroups

n_samples = 2000
n_features = 1000

print("데이터셋 로드 중...")
data, _ = fetch_20newsgroups(
    shuffle=True,
    random_state=1,
    remove=("headers", "footers", "quotes"),
    return_X_y=True,
)
data_samples = data[:n_samples]
```
