# 스펙트로그램 생성

이제 신호의 스펙트로그램 플롯을 생성합니다. Matplotlib 의 `Axes` 클래스에서 `specgram` 메서드를 사용하여 스펙트로그램을 생성합니다. 이 메서드는 `Pxx`, `freqs`, `bins`, 그리고 `im`의 네 가지 객체를 반환합니다. `Pxx`는 periodogram(주기율도), `freqs`는 주파수 벡터, `bins`는 시간 빈 (time bin) 의 중심, 그리고 `im`은 플롯의 데이터를 나타내는 `AxesImage` 인스턴스입니다.

```python
NFFT = 1024  # the length of the windowing segments
Fs = int(1.0 / dt)  # the sampling frequency

fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.plot(t, x)
Pxx, freqs, bins, im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900)
```
