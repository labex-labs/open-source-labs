# 3D グラフとデータを作成する

このステップでは、3D グラフを作成し、サーフェスプロット用のテストデータを取得します。

```python
# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Get test data for the surface plot
X, Y, Z = axes3d.get_test_data(0.05)
```
