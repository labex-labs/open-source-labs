# 텍스트 상자 생성

```python
plt.text(0.6, 0.7, "eggs", size=50, rotation=30.,
         ha="center", va="center",
         bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   )
         )
```

`text()` 메서드를 사용하여 "eggs"라는 단어가 포함된 텍스트 상자를 생성합니다. `bbox` 매개변수는 상자의 스타일을 지정하는 데 사용됩니다. `boxstyle` 매개변수는 둥근 상자를 생성하기 위해 "round"로 설정되고, `ec` 및 `fc` 매개변수는 각각 상자의 테두리 및 채우기 색상을 설정합니다. `size` 매개변수는 글꼴 크기를 설정하고, `rotation` 매개변수는 회전 각도를 설정하며, `ha` 및 `va` 매개변수는 상자 내 텍스트의 가로 및 세로 정렬을 설정합니다.
