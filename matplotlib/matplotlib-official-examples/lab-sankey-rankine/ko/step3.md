# Figure 및 Axes 생성

figure 객체를 생성하고 단일 축 집합을 추가합니다. 또한 플롯의 제목을 설정합니다.

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Rankine Power Cycle: Example 8.6 from Moran and "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```
