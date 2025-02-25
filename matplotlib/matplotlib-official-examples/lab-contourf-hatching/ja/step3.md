# カラーバー付きの最もシンプルなハッチ付きプロット

このステップでは、カラーバー付きの最もシンプルなハッチ付きプロットを作成します。塗りつぶし等高線プロットを作成するために `contourf` 関数を使用し、`hatches` パラメータを使ってハッチを指定します。

```python
fig1, ax1 = plt.subplots()
cs = ax1.contourf(x, y, z, hatches=['-', '/', '\\', '//'],
                  cmap='gray', extend='both', alpha=0.5)
fig1.colorbar(cs)
```
