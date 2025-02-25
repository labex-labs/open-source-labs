# Erstellen eines Balkendiagramms

Wir werden ein Balkendiagramm erstellen, bei dem die X-Achsenwerte von 0 bis 5 und die entsprechenden Y-Achsenwerte variieren. Wir werden die `bar`-Funktion des `pyplot`-Moduls verwenden, um das Balkendiagramm zu erstellen.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a bar plot
plt.bar(x, y)

# Adding title and labels to the plot
plt.title('Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
