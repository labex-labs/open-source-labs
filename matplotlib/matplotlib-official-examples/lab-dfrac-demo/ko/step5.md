# \dfrac 를 사용하여 데이터 플롯

\dfrac TeX 매크로를 사용하여 데이터를 플롯하고 결과 플롯을 표시합니다.

```python
fig, ax = plt.subplots()
ax.plot(x, y, label=r'$\dfrac{sin(x)}{x}$')
ax.legend()
plt.show()
```
