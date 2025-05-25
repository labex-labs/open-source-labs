# 텍스트 플롯

이제 텍스트를 정의했으므로 Matplotlib 을 사용하여 플롯할 수 있습니다. 이 단계에서는 figure 를 생성하고 `fig.text()` 메서드를 사용하여 텍스트를 추가합니다.

```python
fig = plt.figure(figsize=(8, len(tests) + 2))
for i, s in enumerate(tests[::-1]):
    fig.text(0, (i + .5) / len(tests), s, fontsize=32)

plt.show()
```
