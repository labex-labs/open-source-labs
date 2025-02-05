# Create the Plot and Connect the Keypress Event Listener

We create a simple plot using `np.random.rand()` to generate random data. Then, we set up the keypress event listener using `fig.canvas.mpl_connect()` and passing in the name of the event we want to listen for (`'key_press_event'`) and the function we want to call when the event occurs (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Press a key')
plt.show()
```
