# 疑似データを作成する

X、Y、Z の値に基づいてデータを計算する式を使って、プロットする疑似データを作成します。最小値が 0 より大きくなるように、結果に 1 を加えます。

```python
# Create fake data
data = (((X+100)**2 + (Y-20)**2 + 2*Z)/1000+1)
```
