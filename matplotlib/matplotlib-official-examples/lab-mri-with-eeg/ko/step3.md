# EEG 데이터 로드 및 트레이스 플롯

다음 단계는 EEG 데이터를 로드하고 트레이스를 플롯하는 것입니다. `fromfile()` 함수를 사용하여 파일에서 데이터를 로드하고, `LineCollection()`을 사용하여 트레이스를 플롯합니다. 또한 y 축 눈금 레이블을 전극 채널로 설정합니다.

```python
# Load the EEG data
n_samples, n_rows = 800, 4
data = np.load('eeg_data.npy')
t = 10 * np.arange(n_samples) / n_samples

# Plot the EEG
ax2 = fig.add_subplot(2, 1, 2)
ax2.set_xlim(0, 10)
ax2.set_xticks(np.arange(10))
dmin = data.min()
dmax = data.max()
dr = (dmax - dmin) * 0.7  # Crowd them a bit.
y0 = dmin
y1 = (n_rows - 1) * dr + dmax
ax2.set_ylim(y0, y1)

segs = []
for i in range(n_rows):
    segs.append(np.column_stack((t, data[:, i])))

offsets = np.zeros((n_rows, 2), dtype=float)
offsets[:, 1] = np.arange(n_rows) * dr

lines = LineCollection(segs, offsets=offsets, transOffset=None)
ax2.add_collection(lines)

# Set the yticks to use axes coordinates on the y-axis
ax2.set_yticks(offsets[:, 1])
ax2.set_yticklabels(['PG3', 'PG5', 'PG7', 'PG9'])
ax2.set_xlabel('Time (s)')
```
