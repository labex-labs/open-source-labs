# グラフとプロットを作成する

```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], 'ro-', label='easy as 1 2 3')
ax.plot([1, 4, 9], 'gs--', label='easy as 1 2 3 squared')
ax.legend()
```

2 つのサブプロットを持つグラフを作成し、それらに 2 セットのデータをプロットします。また、プロットに凡例を追加します。
