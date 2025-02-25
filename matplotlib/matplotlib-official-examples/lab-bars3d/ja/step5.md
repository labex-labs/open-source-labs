# 軸のカスタマイズ

次に、3D プロットの軸をカスタマイズします。それぞれ `set_xlabel()`、`set_ylabel()`、および `set_zlabel()` メソッドを使用して、x 軸、y 軸、および z 軸のラベルを設定します。また、`set_yticks()` メソッドを使用して y 軸の目盛りを設定します。

```python
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_yticks(yticks)
```
