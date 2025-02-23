# プロットの保存

`savefig` 関数を使って、プロットを画像ファイルとして保存することができます。

```python
fig, ax = plt.subplots()
for shape in shapes:
    ax.add_artist(shape)
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.axis('off')
plt.savefig('shapes.png')
```
