# カスタムインデックスフォーマッターの作成

データを 0、1、... len(data) までのインデックスに対してプロットするために、カスタムインデックスフォーマッターを作成します。このフォーマッターは、目盛りを整数ではなく日付にフォーマットします。

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
