# MRI 強度のヒストグラムをプロットする

次に、`hist()`関数を使って MRI 強度のヒストグラムをプロットします。強度値を 0 から 1 の範囲に正規化します。

```python
# MRI 強度のヒストグラムをプロットする
ax1 = fig.add_subplot(2, 2, 2)
im = np.ravel(im)
im = im[np.nonzero(im)]  # 背景を無視する
im = im / im.max()  # 正規化する
ax1.hist(im, bins=100)
ax1.set_xlabel('Intensity (a.u.)')
ax1.set_ylabel('MRI density')
```
