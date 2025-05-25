# 노치 박스 플롯 생성

이제 `boxplot()` 함수를 사용하여 노치 박스 플롯을 생성합니다. 노치 박스 플롯을 생성하기 위해 `notch` 매개변수를 `True`로 설정합니다.

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # notch shape
                     vert=True,  # vertical box alignment
                     patch_artist=True,  # fill with color
                     labels=labels)  # x-tick labels
ax2.set_title('Notched Box Plot')
```
