# 플롯 생성

다음으로, 다양한 `CapStyle` 옵션을 시연하기 위해 간단한 플롯을 생성합니다.

```python
fig, ax = plt.subplots()

# Plotting the line with different CapStyle options
for i, cap_style in enumerate(CapStyle):
    ax.plot([0, 1], [i, i], label=str(cap_style), linewidth=10, solid_capstyle=cap_style)

# Adding legend and title
ax.legend(title='CapStyle')
ax.set_title('CapStyle Demo')
```
