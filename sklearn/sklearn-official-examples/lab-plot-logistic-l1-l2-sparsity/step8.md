# Set Titles and Labels

We will set the titles and labels for the subplots.

```python
    if i == 0:
        axes_row[0].set_title("L1 penalty")
        axes_row[1].set_title("Elastic-Net\nl1_ratio = %s" % l1_ratio)
        axes_row[2].set_title("L2 penalty")

    axes_row[0].set_ylabel("C = %s" % C)
```


