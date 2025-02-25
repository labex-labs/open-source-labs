# エイリアス

対話型モードでの入力回数を減らすために、多くのプロパティには短いエイリアスがあります。たとえば、'linewidth' の 'lw' や'markeredgecolor' の'mec' などです。インスペクションモードで set または get を呼び出すとき、これらのプロパティは 'fullname' または 'aliasname' としてリストされます。

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```
