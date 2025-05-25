# 플롯 생성

이제 Matplotlib 의 `subplots` 함수를 사용하여 플롯을 생성합니다. 수직선과 수평선을 위한 두 개의 서브플롯을 생성합니다. 가시성을 높이기 위해 그림 크기를 (12, 6) 으로 설정합니다.

```python
# Create the plot
fig, (vax, hax) = plt.subplots(1, 2, figsize=(12, 6))
```
