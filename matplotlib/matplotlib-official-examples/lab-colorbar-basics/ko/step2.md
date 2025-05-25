# 데이터 생성

`numpy`의 `mgrid` 함수를 사용하여 플롯할 샘플 데이터를 생성합니다.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
