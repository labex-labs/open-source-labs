# Figure Size in Centimeters

We can also specify the figure size in centimeters. To do this, we need to convert the centimeter-based numbers to inches. We can do this by multiplying the centimeter value with the conversion factor from cm to inches, which is 1/2.54. We can then use this value as the figsize parameter in the subplots function. The code below shows how to create a figure with a size of 15 cm x 5 cm.

```python
cm = 1/2.54  # centimeters in inches
plt.subplots(figsize=(15*cm, 5*cm))
plt.show()
```
