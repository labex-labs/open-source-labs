# 基本的な統計を行う

Pandas には、統計を行うための多くの機能が用意されています。たとえば、`max()` を使用して列の最大値を求めることができます。

```python
# Finding the maximum age
df["Age"].max()
```

また、`describe()` を使用することで、DataFrame 内の数値データの概要をすばやく把握することができます。

```python
# Describing the numerical data
df.describe()
```
