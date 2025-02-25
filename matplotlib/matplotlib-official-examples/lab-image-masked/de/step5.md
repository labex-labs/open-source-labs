# Erstellen eines Balkendiagramms

Ein weiterer häufiger Plot-Typ ist das Balkendiagramm. Balkendiagramme eignen sich zur Vergleichung von Werten unterschiedlicher Kategorien.

```python
# Create the data
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 1, 9, 4]

# Create the bar chart
plt.bar(x, y)

# Add title and axis labels
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()
```
