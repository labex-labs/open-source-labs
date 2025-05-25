# 피쉬본 다이어그램 (Fishbone Diagram) 생성

이제 피쉬본 다이어그램을 생성합니다. 먼저 figure 와 axis 객체를 생성합니다.

```python
fig, ax = plt.subplots(figsize=(10, 6), layout='constrained')
```

다음으로, axis 의 x 및 y 제한을 설정하고 axis 를 끕니다.

```python
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.axis('off')
```
