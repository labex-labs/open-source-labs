# Create a Figure with Two Subplots

First, we need to create a figure with two subplots. We will use the `plt.subplots()` method to create a figure with two subplots side by side.

```python
import matplotlib.pyplot as plt

fig, (ax, ax2) = plt.subplots(1, 2, figsize=[5.5, 2.8])
```
