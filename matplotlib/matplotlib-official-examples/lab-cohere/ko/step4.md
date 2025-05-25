# Coherence (일관성) 플롯

이제 Matplotlib 의 `cohere` 함수를 사용하여 두 신호의 coherence (일관성) 를 플롯할 수 있습니다.

```python
cxy, f = axs[1].cohere(s1, s2, 256, 1. / dt)
axs[1].set_ylabel('Coherence')
```
