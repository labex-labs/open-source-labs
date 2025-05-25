# 커널 밀도 추정기 적합

이제 `KernelDensity` 추정기의 인스턴스를 만들고 데이터에 맞춥니다. 추정기의 커널 유형과 대역폭을 선택할 수 있습니다. 예를 들어, 가우시안 커널을 사용하고 대역폭을 0.2 로 설정할 수 있습니다.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
