# ラベルとタイトルを追加する

このステップでは、グラフにタイトルを追加し、x 軸と y 軸にラベルを付けます。

```python
plt.plot(t, t, 'r--', label='linear')
plt.plot(t, t**2, 'bs', label='quadratic')
plt.plot(t, t**3, 'g^', label='cubic')
plt.legend()
plt.title("Multiple Datasets")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.show()
```
