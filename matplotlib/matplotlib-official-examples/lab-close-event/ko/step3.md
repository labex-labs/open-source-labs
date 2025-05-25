# Figure 에 텍스트 추가

이 단계에서는 사용자에게 figure 를 닫도록 안내하기 위해 figure 에 텍스트를 추가합니다. 이는 Matplotlib 의 `text` 메서드를 사용하여 수행됩니다.

```python
plt.text(0.35, 0.5, 'Close Me!', dict(size=30))
```
