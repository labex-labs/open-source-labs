# Vergleiche die Scores mit und ohne Early Stopping

Wir werden nun die Scores der beiden Modelle vergleichen.

```python
plt.figure(figsize=(9, 5))

bar1 = plt.bar(
    index, score_gb, bar_width, label="Ohne Early Stopping", color="crimson"
)
bar2 = plt.bar(
    index + bar_width, score_gbes, bar_width, label="Mit Early Stopping", color="coral"
)

plt.xticks(index + bar_width, names)
plt.yticks(np.arange(0, 1.3, 0.1))

autolabel(bar1, n_gb)
autolabel(bar2, n_gbes)

plt.ylim([0, 1.3])
plt.legend(loc="best")
plt.grid(True)

plt.xlabel("Datensätze")
plt.ylabel("Testscore")

plt.show()
```
