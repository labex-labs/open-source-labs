# 진폭 슬라이더에 대한 허용 값 정의

이 단계에서는 진폭 슬라이더에 대한 허용 값을 정의합니다. 진폭 슬라이더는 이러한 값을 사용하여 가장 가까운 허용 값으로 스냅합니다.

```python
# define the values to use for snapping
allowed_amplitudes = np.concatenate([np.linspace(.1, 5, 100), [6, 7, 8, 9]])
```
