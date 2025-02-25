# Создать скрипку-скрипку

Мы создадим скрипку-скрипку с использованием метода `violinplot()`. Этот метод принимает несколько аргументов, таких как data, showmeans, showmedians и т.д.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
