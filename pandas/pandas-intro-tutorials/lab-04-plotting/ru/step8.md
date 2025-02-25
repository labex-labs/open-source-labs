# Настраиваем и сохраняем график

Мы можем дополнительно настроить график, используя параметры настройки Matplotlib. Мы также можем сохранить график в файл.

```python
# Customizing and saving the plot
fig, axs = plt.subplots(figsize=(12, 4))
air_quality.plot.area(ax=axs)
axs.set_ylabel("NO$_2$ concentration")
fig.savefig("no2_concentrations.png")
plt.show()
```
