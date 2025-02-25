# Definieren der UpdateDist-Klasse

Als nächstes definieren wir eine Klasse namens `UpdateDist`, die verwendet werden soll, um die Beta-Verteilung bei Beobachtung neuer Daten zu aktualisieren. Die `UpdateDist`-Klasse nimmt zwei Argumente entgegen: das Matplotlib-Achsenobjekt und die anfängliche Erfolgswahrscheinlichkeit.

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')
```

Die `__init__`-Methode initialisiert die Klasseninstanz, indem sie die anfängliche Anzahl der Erfolge auf Null setzt (`self.success = 0`) und die anfängliche Erfolgswahrscheinlichkeit auf den als Argument übergebenen Wert (`self.prob = prob`). Wir erstellen auch ein Linienobjekt, um die Beta-Verteilung darzustellen, und legen die Diagrammeinstellungen fest.

Die `__call__`-Methode wird jedes Mal aufgerufen, wenn die Animation aktualisiert wird. Sie simuliert ein Münzwurfexperiment und aktualisiert die Beta-Verteilung entsprechend.

```python
def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

Wenn dies der erste Frame der Animation ist (`if i == 0`), setzen wir die Anzahl der Erfolge auf Null zurück und löschen das Linienobjekt. Andernfalls simulieren wir ein Münzwurfexperiment, indem wir eine Zufallszahl zwischen 0 und 1 generieren (`np.random.rand()`) und sie mit der Erfolgswahrscheinlichkeit (`self.prob`) vergleichen. Wenn die Zufallszahl kleiner als die Erfolgswahrscheinlichkeit ist, zählen wir es als Erfolg und aktualisieren die Beta-Verteilung mit der `beta_pdf`-Funktion. Schließlich aktualisieren wir das Linienobjekt mit den neuen Daten und geben es zurück.
