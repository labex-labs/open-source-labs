# Creating Custom Index Formatter

To plot the data against an index that goes from 0, 1, ... len(data), we will create a custom index formatter. This formatter will format the tick marks as times instead of integers.

```python
# Create custom index formatter
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# Format x-axis as times
def format_date(x, _):
    try:
        # convert datetime64 to datetime, and use datetime's strftime:
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creating Custom Index Formatter")
ax2.xaxis.set_major_formatter(format_date)  # internally creates FuncFormatter
```
