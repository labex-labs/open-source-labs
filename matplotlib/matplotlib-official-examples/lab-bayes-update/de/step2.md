# Definieren der Beta-Verteilungs-PDF

Die Beta-Verteilung ist eine kontinuierliche Wahrscheinlichkeitsverteilung, die häufig verwendet wird, um die Verteilung von Wahrscheinlichkeiten darzustellen. Beim Bayes'schen Updating verwenden wir die Beta-Verteilung als Vorverteilung, um unsere Überzeugungen über die Wahrscheinlichkeit einer Hypothese darzustellen, bevor wir irgendwelche Daten beobachten. Anschließend aktualisieren wir die Beta-Verteilung, wenn wir neue Daten beobachten.

Um das Bayes'sche Updating zu simulieren, müssen wir eine Funktion definieren, die die Wahrscheinlichkeitsdichtefunktion (PDF) der Beta-Verteilung berechnet. Wir können die `math.gamma`-Funktion verwenden, um die Gamma-Funktion zu berechnen, die in der Beta-Verteilungs-PDF verwendet wird.

```python
def beta_pdf(x, a, b):
    return (x**(a-1) * (1-x)**(b-1) * math.gamma(a + b)
            / (math.gamma(a) * math.gamma(b)))
```
