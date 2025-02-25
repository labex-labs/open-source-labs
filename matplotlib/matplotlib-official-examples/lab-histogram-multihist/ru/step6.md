# Строим несколько гистограмм

Мы можем построить несколько гистограмм на одном графике, передав массив данных в функцию `hist`.

```python
plt.hist(x, n_bins, color='green', alpha=0.5, edgecolor='black', label=['Sample 1', 'Sample 2', 'Sample 3'])
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Data')
plt.legend()
plt.show()
```
