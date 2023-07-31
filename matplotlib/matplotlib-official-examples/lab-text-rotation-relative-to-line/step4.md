# Plot text without correct rotation

We will now plot text at the specified locations without taking the rotation of the line into account. This will result in the text being rotated at a 45-degree angle, which is not what we want.

```python
# Plot text
th1 = ax.text(*l1, 'text not rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor')
```
