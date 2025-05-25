# 플롯 생성

이 단계에서는 플롯을 생성합니다. `fig.text()` 메서드를 사용하여 플롯에 텍스트를 추가합니다. 폰트 목록과 해당 텍스트를 반복하며, `zip()` 함수를 사용하여 매칭합니다. `usetex` 매개변수를 `True`로 설정하여 usetex 모드를 활성화합니다.

```python
fig = plt.figure()
for y, font, text in zip(
    range(5),
    ['ptmr8r', 'ptmri8r', 'ptmro8r', 'ptmr8rn', 'ptmrr8re'],
    [f'Nimbus Roman No9 L {x}'
     for x in ['', 'Italics (real italics for comparison)',
               '(slanted)', '(condensed)', '(extended)']],
):
    fig.text(.1, 1 - (y + 1) / 6, setfont(font) + text, usetex=True)

fig.suptitle('Usetex font effects')
plt.show()
```
