# 텍스트 자동 줄 바꿈

이제 Matplotlib 에서 텍스트를 자동으로 줄 바꿈하는 방법을 살펴보겠습니다. 코드에서 `plt.text()` 줄을 다음으로 바꾸십시오.

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

`wrap=True` 인수는 Matplotlib 에 텍스트를 자동으로 줄 바꿈하도록 지시합니다.
