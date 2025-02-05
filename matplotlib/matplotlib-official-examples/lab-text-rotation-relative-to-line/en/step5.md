# Plot text with correct rotation

Finally, we will plot text at the specified locations while taking the rotation of the line into account. This will result in the text being rotated at the correct angle relative to the line.

```python
# Plot text
th2 = ax.text(*l2, 'text rotated correctly', fontsize=16,
              rotation=angle, rotation_mode='anchor',
              transform_rotates_text=True)
```
