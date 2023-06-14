# Update the Status Bar

Finally, we will define a method to update the status bar with the cursor location whenever the mouse moves over the plot.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```

#
