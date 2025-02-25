# Добавляем легенду к графику

Теперь мы добавим легенду к графику. В Matplotlib есть два способа добавить легенду. Мы будем использовать оба метода в этом примере.

```python
# Method 1: Place a legend above the subplot
ax.legend(bbox_to_anchor=(0., 1.02, 1.,.102), loc='lower left',
           ncols=2, mode="expand", borderaxespad=0.)

# Method 2: Place a legend to the right of the subplot
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
```
