# 바이올린 플롯 생성

`violinplot()` 메서드를 사용하여 바이올린 플롯을 생성합니다. 이 메서드는 데이터, showmeans, showmedians 등과 같은 여러 인수를 받습니다.

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
