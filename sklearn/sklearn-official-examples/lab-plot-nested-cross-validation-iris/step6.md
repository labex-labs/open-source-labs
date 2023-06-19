# Visualize the Results

We visualize the results of the non-nested and nested cross-validation using a bar chart.

```python
from matplotlib import pyplot as plt

# Plot bar chart of the difference.
plt.bar(["Non-Nested", "Nested"], [non_nested_score, nested_scores.mean()])
plt.ylim([0.9, 1.0])
plt.ylabel("Score")
plt.title("Non-Nested and Nested Cross-Validation Scores")
plt.show()
```
