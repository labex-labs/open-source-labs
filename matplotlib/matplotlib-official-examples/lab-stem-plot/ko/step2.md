# 데이터 생성

다음으로, 줄기 플롯에 사용할 데이터를 생성해야 합니다. Numpy 라이브러리를 사용하여 두 개의 배열을 생성합니다.

```python
x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))
```
