# Controlling Text Placement and Style

We can also control the placement and style of the text in our Matplotlib plot. Try adding the following code to your script:

```python
plt.text(2, 8, "Top Left", fontsize=12, color='red')
plt.text(8, 8, "Top Right", fontsize=12, color='blue')
plt.text(2, 2, "Bottom Left", fontsize=12, color='green')
plt.text(8, 2, "Bottom Right", fontsize=12, color='purple')
```

This will add four text elements to our plot, each with a different color, font size, and position.
