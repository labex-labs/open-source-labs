# 信号をプロットする

生成した 2 つの信号を、Matplotlib の plot 関数を使ってプロットすることができます。

```python
fig, ax = plt.subplots()
ax.plot(t, s1, label='s1')
ax.plot(t, s2, label='s2')
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
ax.legend()
plt.show()
```
