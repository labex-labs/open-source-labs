# 데이터 로드

digits 데이터셋을 로드하고 이미지를 벡터로 평탄화합니다. 각 8x8 픽셀 이미지는 64 픽셀 벡터로 변환되어야 합니다. 따라서 최종 데이터 배열의 형태는 `(n_images, n_pixels)`가 됩니다. 또한 데이터를 동일한 크기의 학습 및 테스트 세트로 분할합니다.

```python
from sklearn import datasets
from sklearn.model_selection import train_test_split

digits = datasets.load_digits()

n_samples = len(digits.images)
X = digits.images.reshape((n_samples, -1))
y = digits.target == 8

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
