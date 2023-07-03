# Create figure 1

We will begin by creating the first figure, which will contain two subplots. We will plot the first sine wave in the top subplot and twice the amplitude of the first sine wave in the bottom subplot.

```python
plt.figure(1)

# Top subplot
plt.subplot(211)
plt.plot(t, s1)

# Bottom subplot
plt.subplot(212)
plt.plot(t, 2*s1)
```
