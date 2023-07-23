# Add Table to the Plot

We will add a table to the bottom of the plot using the `plt.table` function. We will pass the cell text, row labels, row colors, and column labels as parameters to the function.

```python
the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      rowColours=colors,
                      colLabels=columns,
                      loc='bottom')
```
