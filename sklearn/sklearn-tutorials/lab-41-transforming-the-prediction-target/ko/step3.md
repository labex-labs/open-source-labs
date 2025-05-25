# 레이블 인코딩

레이블 인코딩은 숫자가 아닌 레이블을 숫자 레이블로 변환하는 과정입니다. `LabelEncoder` 클래스를 사용하여 이를 수행할 수 있습니다.

```python
from sklearn import preprocessing

# LabelEncoder 인스턴스 생성
le = preprocessing.LabelEncoder()

# 숫자가 아닌 레이블 목록으로 LabelEncoder 를 학습
le.fit(["paris", "paris", "tokyo", "amsterdam"])

# LabelEncoder 가 학습한 클래스 가져오기
list(le.classes_)

# 숫자가 아닌 레이블 목록을 숫자 레이블로 변환
le.transform(["tokyo", "tokyo", "paris"])

# 숫자 레이블을 다시 숫자가 아닌 레이블로 역변환
list(le.inverse_transform([2, 2, 1]))
```
