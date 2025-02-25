# Erstellen eines einfachen Linienplots

Wir werden einen einfachen Linienplot erstellen, bei dem die X-Achsenwerte von 0 bis 5 und die entsprechenden Y-Achsenwerte variieren. Wir werden die `plot`-Funktion des `pyplot`-Moduls verwenden, um den Linienplot zu erstellen.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
