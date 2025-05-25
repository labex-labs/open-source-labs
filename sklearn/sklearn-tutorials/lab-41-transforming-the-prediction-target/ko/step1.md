# 레이블 이진화

레이블 이진화는 다중 클래스 레이블을 이진 표시 행렬로 변환하는 과정입니다. `LabelBinarizer` 클래스를 사용하여 수행할 수 있습니다.

```python
from sklearn import preprocessing

# LabelBinarizer 인스턴스 생성
lb = preprocessing.LabelBinarizer()

# 다중 클래스 레이블 목록으로 LabelBinarizer 를 학습
lb.fit([1, 2, 6, 4, 2])

# LabelBinarizer 가 학습한 클래스 가져오기
lb.classes_

# 다중 클래스 레이블 목록을 이진 표시 행렬로 변환
lb.transform([1, 6])
```
