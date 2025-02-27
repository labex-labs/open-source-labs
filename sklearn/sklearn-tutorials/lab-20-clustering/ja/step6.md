# クラスタリングを評価する

クラスタリング結果を評価するために、クラスタの不慣性を計算できます。これは、サンプルが最も近いクラスタ中心までの二乗距離の合計を表します。

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
