# 다른 텍스트 상자 생성

```python
plt.text(0.55, 0.6, "spam", size=50, rotation=-25.,
         ha="right", va="top",
         bbox=dict(boxstyle="square",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

"spam"이라는 단어가 포함된 다른 텍스트 상자를 생성합니다. 이번에는 `boxstyle` 매개변수를 "square"로 설정하여 사각형 상자를 만들고, `ha` 및 `va` 매개변수를 "right" 및 "top"으로 설정하여 텍스트를 상자의 오른쪽과 상단에 정렬합니다.
