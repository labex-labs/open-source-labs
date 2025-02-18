# 結果の可視化

棒グラフを使用して、非ネスト交差検証とネスト交差検証の結果を可視化します。

```python
from matplotlib import pyplot as plt

# Plot bar chart of the difference.
plt.bar(["Non-Nested", "Nested"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("Score")
plt.title("Non-Nested and Nested Cross-Validation Scores")
plt.show()
```
