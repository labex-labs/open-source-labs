# 플롯 사용자 정의 및 저장

Matplotlib 의 사용자 정의 옵션을 사용하여 플롯을 추가로 사용자 정의할 수 있습니다. 또한 플롯을 파일로 저장할 수도 있습니다.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
