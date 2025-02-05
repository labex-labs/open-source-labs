# 使用 Unicode 字符

Matplotlib 还支持直接在字符串中使用 Unicode 字符。

```python
import matplotlib.pyplot as plt

# Unicode 演示
fig, ax = plt.subplots()
ax.set_title("吉斯卡尔在议会上大闹")
ax.set_xlabel("戴高乐的决定性一击")
ax.set_ylabel('安德烈曾在此！')
ax.text(0.2, 0.8, '固体物理研究所', rotation=45)
ax.text(0.4, 0.2, 'AVA（检查字距调整）')

plt.show()
```

需注意，你提供的英文内容中部分表述似乎不太符合常规的专业文档语境，翻译后的中文可能在语义理解上也会存在一定奇特之处，但完全是按照要求进行的逐字翻译。
