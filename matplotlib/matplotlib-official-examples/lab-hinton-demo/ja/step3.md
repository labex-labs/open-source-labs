# ヒントン図の生成

次に、numpy を使ってランダムな重み行列を生成し、その後`hinton`関数を使ってヒントン図を生成します。

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```
