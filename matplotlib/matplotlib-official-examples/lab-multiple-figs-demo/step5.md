# Make changes to figure 1

Now, we will switch back to the first figure and make some changes. We will plot the second sine wave in the top subplot using square markers, and remove the x-axis tick labels from the top subplot.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s2, 's')
ax = plt.gca()
ax.set_xticklabels([])
```
