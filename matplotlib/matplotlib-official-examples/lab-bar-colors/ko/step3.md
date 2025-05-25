# 막대 차트 생성

이제 2 단계에서 정의한 데이터를 사용하여 막대 차트를 만들 수 있습니다. Matplotlib 의 `pyplot` 모듈의 `bar()` 메서드를 사용하여 차트를 생성합니다. 또한 범례 항목과 막대 색상을 각각 제어하기 위해 `label` 및 `color` 매개변수를 전달합니다. 다음 코드는 막대 차트를 만드는 방법을 보여줍니다.

```python
fig, ax = plt.subplots()
ax.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')
plt.show()
```
