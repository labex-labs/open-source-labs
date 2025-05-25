# 데이터셋 로드 및 분할

먼저, Scikit-Learn 라이브러리를 사용하여 숫자 데이터셋을 로드합니다. 이 데이터셋은 0 부터 9 까지의 숫자 이미지 (8x8 픽셀) 로 구성되어 있으며, 각 이미지는 64 개의 특징으로 이루어진 배열로 표현됩니다. 데이터를 특징 (features) 과 목표 변수 (target variables) 로 분할할 것입니다.

```python
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.images.reshape((len(digits.images), -1))
y = digits.target
```
