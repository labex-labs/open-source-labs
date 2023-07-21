# Create violin plot

We will create a violin plot using `violinplot()` method. This method takes multiple arguments such as data, showmeans, showmedians etc.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
