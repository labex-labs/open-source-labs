# 기능 데모 공식 플롯

이 단계에서는 기능 데모 공식을 플롯합니다.

```python
for i_line, (title, demo) in enumerate(mathtext_demos.items()):
    if i_line == 0:
        continue

    baseline = 1 - i_line * line_axesfrac
    baseline_next = baseline - line_axesfrac
    fill_color = ['white', 'tab:blue'][i_line % 2]
    ax.axhspan(baseline, baseline_next, color=fill_color, alpha=0.2)
    ax.annotate(f'{title}:',
                xy=(0.06, baseline - 0.3 * line_axesfrac),
                color=mpl_grey_rgb, weight='bold')
    ax.annotate(demo,
                xy=(0.04, baseline - 0.75 * line_axesfrac),
                color=mpl_grey_rgb, fontsize=16)
```
