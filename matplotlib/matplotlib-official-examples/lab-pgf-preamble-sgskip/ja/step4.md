# グラフをカスタマイズする

色、線のスタイル、マーカーを変更することで、グラフをカスタマイズできます。以下は例です。

```python
plt.plot(x, y1, 'r--', label='sin')
plt.plot(x, y2, 'g:', label='cos')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.show()
```
