# CSD 계산

두 신호의 CSD(Cross Spectral Density, 상호 스펙트럼 밀도) 를 계산하려면 Matplotlib 의 csd 함수를 사용해야 합니다. 이 함수는 두 신호, FFT(Fast Fourier Transform, 고속 푸리에 변환) 에 사용할 점의 수, 그리고 샘플링 주파수를 입력으로 받습니다.

```python
fig, ax = plt.subplots()
cxy, f = ax.csd(s1, s2, 256, 1. / dt)
ax.set_ylabel('CSD (dB)')
plt.show()
```
