# Настраиваем гистограмму

В этом шаге мы настроим гистограмму, добавив подписи, заголовок и настроив макет.

```python
ax.set_xlabel('Smarts')
ax.set_ylabel('Probability density')
ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
fig.tight_layout()
plt.show()
```
