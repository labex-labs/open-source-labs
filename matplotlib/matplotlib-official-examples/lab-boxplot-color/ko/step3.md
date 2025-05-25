# 직사각형 박스 플롯 생성

이제 Matplotlib 의 `boxplot()` 함수를 사용하여 직사각형 박스 플롯을 생성합니다. 상자를 색상으로 채우기 위해 `patch_artist` 매개변수를 `True`로 설정합니다.

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax1.set_title('Rectangular Box Plot')
```
