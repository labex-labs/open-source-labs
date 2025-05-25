# 텍스트 추가

이 단계에서는 `text()` 함수를 사용하여 플롯에 텍스트를 추가합니다.

```python
tex = r'$\mathcal{R}\prod_{i=\alpha_{i+1}}^\infty a_i\sin(2 \pi f x_i)$'
ax.text(1, 1.6, tex, fontsize=20, va='bottom')
```
