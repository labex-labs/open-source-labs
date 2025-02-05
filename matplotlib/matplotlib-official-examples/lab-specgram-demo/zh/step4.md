# 自定义绘图

我们可以通过添加标题、轴标签和颜色映射来自定义绘图。

```python
fig, (ax1, ax2) = plt.subplots(nrows=2)
ax1.set_title('时间域信号')
ax1.set_xlabel('时间 (秒)')
ax1.set_ylabel('幅度')
ax1.plot(t, x)

ax2.set_title('频谱图')
ax2.set_xlabel('时间 (秒)')
ax2.set_ylabel('频率 (赫兹)')
im = ax2.specgram(x, NFFT=NFFT, Fs=Fs, noverlap=900, cmap='viridis')
fig.colorbar(im[3], ax=ax2)
```
