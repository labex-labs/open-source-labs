# プロットの範囲を調整する

次に、プロットの範囲を調整して、画面上で見たときに対角線がもはや 45 度の角度にならないようにします。これにより、画面座標系ではなく、線に対してテキストを回転させる必要が生じるシナリオが作成されます。

```python
# set limits so that it no longer looks on screen to be 45 degrees
ax.set_xlim([-10, 20])
```
