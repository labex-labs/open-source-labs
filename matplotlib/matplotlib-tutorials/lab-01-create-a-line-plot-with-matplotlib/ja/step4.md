# グラフをカスタマイズする

x 軸と y 軸にラベルを付け、グラフにタイトルを付け、凡例を追加することで、グラフをカスタマイズできます。また、線のスタイルや色も変更できます。

```python
plt.plot(x, y, linestyle='--', color='red', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Plot')
plt.legend()
```
