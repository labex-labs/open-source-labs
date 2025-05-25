# 다른 예시 플롯

이제 파수 (wavenumber) 에서 파장 (wavelength) 으로 변환하는 또 다른 예시를 로그 - 로그 (log-log) 스케일로 플롯합니다. 이 예시에서는 임의 스펙트럼을 사용합니다.

```python
fig, ax = plt.subplots(layout='constrained')
x = np.arange(0.02, 1, 0.02)
np.random.seed(19680801)
y = np.random.randn(len(x)) ** 2
ax.loglog(x, y)
ax.set_xlabel('f [Hz]')
ax.set_ylabel('PSD')
ax.set_title('Random spectrum')
```
