# 기본 단위를 사용하여 막대 그래프 생성

이 단계에서는 Matplotlib 의 `bar` 메서드를 사용하여 기본 단위를 갖는 막대 그래프를 생성합니다. 막대의 하단을 0 으로 설정하기 위해 `bottom` 매개변수를 사용합니다.

```python
fig, axs = plt.subplots(2, 2)

axs[0, 0].bar(cms, cms, bottom=bottom)
```
