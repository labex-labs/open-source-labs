# 데이터 생성

이 단계에서는 더 많은 수의 랜덤 워크 "노이즈/배경" 시계열 아래에 묻혀 있는 여러 개의 사인파 "신호" 시계열을 생성합니다. 우리는 편향되지 않은 가우시안 랜덤 워크와 사인파 신호를 생성할 것입니다.

```python
# 재현성을 위해 랜덤 상태 고정
np.random.seed(19680801)

# 일부 데이터 생성; 1D 랜덤 워크 + 작은 비율의 사인파
num_series = 1000
num_points = 100
SNR = 0.10  # 신호 대 잡음비 (Signal to Noise Ratio)
x = np.linspace(0, 4 * np.pi, num_points)

# 편향되지 않은 가우시안 랜덤 워크 생성
Y = np.cumsum(np.random.randn(num_series, num_points), axis=-1)

# 사인파 신호 생성
num_signal = round(SNR * num_series)
phi = (np.pi / 8) * np.random.randn(num_signal, 1)  # 작은 랜덤 오프셋
Y[-num_signal:] = (
    np.sqrt(np.arange(num_points))  # 랜덤 워크 RMS 스케일링 팩터
    * (np.sin(x - phi)
       + 0.05 * np.random.randn(num_signal, num_points))  # 작은 랜덤 노이즈
)
```
