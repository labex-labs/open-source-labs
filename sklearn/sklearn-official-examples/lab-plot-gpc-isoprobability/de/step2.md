# Daten vorbereiten

Wir werden einige synthetische Daten für die Klassifizierung generieren. Die zu klassifizierende Funktion wird wie folgt definiert:

```python
def g(x):
    """Die Funktion, die vorhergesagt werden soll (die Klassifizierung besteht dann darin, vorherzusagen,
    ob g(x) <= 0 oder nicht)"""
    return 5.0 - x[:, 1] - 0.5 * x[:, 0] ** 2.0
```

Anschließend müssen wir das Experimentdesign und die Beobachtungen erstellen.

```python
# Einige Konstanten
lim = 8

# Experimentdesign
X = np.array(
    [
        [-4.61611719, -6.00099547],
        [4.10469096, 5.32782448],
        [0.00000000, -0.50000000],
        [-6.17289014, -4.6984743],
        [1.3109306, -6.93271427],
        [-5.03823144, 3.10584743],
        [-2.87600388, 6.74310541],
        [5.21301203, 4.26386883],
    ]
)

# Beobachtungen
y = np.array(g(X) > 0, dtype=int)
```
