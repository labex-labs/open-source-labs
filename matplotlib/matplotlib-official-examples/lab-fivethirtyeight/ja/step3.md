# 折れ線グラフ用のデータを作成する

このステップでは、折れ線グラフ用のデータを作成します。0 から 10 の間の等間隔の値の配列を作成するために、NumPy の`linspace`関数を使用します。また、NumPy の`random.randn`関数を使って、いくらかのランダムノイズを生成します。

```python
x = np.linspace(0, 10)
np.random.seed(19680801)
noise = np.random.randn(50)
```
