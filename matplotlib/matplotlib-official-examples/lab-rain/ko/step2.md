# 비 데이터 생성

다음으로, 비 데이터를 생성합니다. 무작위 위치, 무작위 성장률 및 무작위 색상으로 50 개의 빗방울을 생성합니다.

```python
n_drops = 50
rain_drops = np.zeros(n_drops, dtype=[('position', float, (2,)),
                                      ('size',     float),
                                      ('growth',   float),
                                      ('color',    float, (4,))])

rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)
```
