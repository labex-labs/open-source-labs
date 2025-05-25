# 다중 레이블 이진화

다중 레이블 이진화는 레이블들의 집합 (컬렉션) 을 표시 형식으로 변환하는 과정입니다. `MultiLabelBinarizer` 클래스를 사용하여 이를 수행할 수 있습니다.

```python
from sklearn.preprocessing import MultiLabelBinarizer

# 레이블들의 집합 (컬렉션) 목록 정의
y = [[2, 3, 4], [2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2]]

# MultiLabelBinarizer 인스턴스를 생성하고, 목록에 fit_transform 적용
MultiLabelBinarizer().fit_transform(y)
```
