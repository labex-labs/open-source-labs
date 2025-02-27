# 結果を可視化する

最後に、予測値と実際の値をプロットして、モデルがデータにどの程度適合しているかを可視化します。

```python
import matplotlib.pyplot as plt

# 出力をプロットする
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
```
