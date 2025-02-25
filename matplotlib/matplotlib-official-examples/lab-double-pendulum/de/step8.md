# Die Animation erstellen

Wir erstellen nun die Animation mit der `FuncAnimation`-Funktion aus Matplotlib.

```python
ani = animation.FuncAnimation(
    fig, animate, len(y), interval=dt*1000, blit=True)
plt.show()
```
