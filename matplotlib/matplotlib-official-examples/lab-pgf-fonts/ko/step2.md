# 글꼴 패밀리 설정

`font.family` 매개변수를 사용하여 글꼴 패밀리를 "serif"로 설정합니다. 또한, 기본 LaTeX serif 글꼴을 사용하기 위해 `font.serif` 매개변수를 빈 리스트로 설정합니다.

```python
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": [],
})
```
