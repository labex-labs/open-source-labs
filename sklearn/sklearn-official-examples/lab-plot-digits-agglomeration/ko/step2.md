# 데이터셋 로드

이 단계에서는 scikit-learn 에서 숫자 데이터셋을 로드합니다. 이 데이터셋에는 0 부터 9 까지의 손글씨 숫자 이미지가 포함되어 있습니다.

```python
digits = datasets.load_digits()
images = digits.images
X = np.reshape(images, (len(images), -1))
```
