# 두 번째 이벤트 플롯을 위한 랜덤 데이터 생성

두 번째 이벤트 플롯을 위해 다른 랜덤 데이터 세트를 생성합니다. 미적인 목적을 위해 감마 분포 (gamma distribution) 를 사용합니다.

```python
data2 = np.random.gamma(4, size=[60, 50])
```
