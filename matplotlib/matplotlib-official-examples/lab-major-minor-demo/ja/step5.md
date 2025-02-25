# 主目盛りと副目盛りの自動目盛り選択

```python
# Create data
t = np.arange(0.0, 100.0, 0.01)
s = np.sin(2 * np.pi * t) * np.exp(-t * 0.01)

# Plot the data
fig, ax = plt.subplots()
ax.plot(t, s)

# Set the minor locator
ax.xaxis.set_minor_locator(AutoMinorLocator())

# Set the tick parameters
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='r')

# Display the plot
plt.show()
```

このステップでは、新しいデータを作成して描画します。その後、副目盛りの数を自動的に選択するように副目盛りを設定します。その後、主目盛りと副目盛りの両方に対して、目盛りの幅と長さ、およびそれらの色などの目盛りパラメータを設定します。最後に、グラフを表示します。
