# Aliases

To reduce keystrokes in interactive mode, a number of properties have short aliases, e.g., 'lw' for 'linewidth' and 'mec' for 'markeredgecolor'. When calling set or get in introspection mode, these properties will be listed as 'fullname' or 'aliasname'.

```python
l1, l2 = plt.plot([1, 2, 3], [2, 3, 4], [1, 2, 3], [3, 4, 5])
plt.setp(l1, linewidth=2, color='r')
plt.setp(l2, linewidth=1, color='g')
```
