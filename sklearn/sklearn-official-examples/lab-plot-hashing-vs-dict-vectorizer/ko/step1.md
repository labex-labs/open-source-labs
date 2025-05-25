# 데이터 로드

`20newsgroups_dataset`에서 데이터를 로드합니다. 이 데이터는 20 개 주제에 대한 약 18,000 개의 뉴스그룹 게시물로 구성되며, 두 개의 하위 집합 (하나는 학습용, 하나는 테스트용) 으로 나뉩니다. 간결성과 계산 비용 절감을 위해 7 개 주제의 하위 집합을 선택하고 학습용 집합만 사용합니다.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "comp.graphics",
    "comp.sys.ibm.pc.hardware",
    "misc.forsale",
    "rec.autos",
    "sci.space",
    "talk.religion.misc",
]

print("20 뉴스그룹 학습 데이터 로드 중")
raw_data, _ = fetch_20newsgroups(subset="train", categories=categories, return_X_y=True)
data_size_mb = sum(len(s.encode("utf-8")) for s in raw_data) / 1e6
print(f"{len(raw_data)} 문서 - {data_size_mb:.3f}MB")
```
