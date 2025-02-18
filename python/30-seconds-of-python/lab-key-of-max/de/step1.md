# Erstellen der Basisfunktion

Beginnen wir mit der Erstellung des Kernteils unserer Funktion. Wir werden sie Schritt für Schritt aufbauen. Zunächst erstellen Sie eine Datei mit dem Namen `key_of_max.py`. Sie können den integrierten LabEx-Code-Editor oder einen terminalbasierten Editor wie `nano` oder `vim` verwenden. Fügen Sie in der Datei `key_of_max.py` den folgenden Code hinzu:

![Code-Editor mit der key_of_max-Funktion](../assets/20250214-14-44-53-838b9T58.png)

```python
def key_of_max(d):
  """
  Gibt den Schlüssel zurück, der dem maximalen Wert im Wörterbuch 'd' zugeordnet ist.

  Wenn mehrere Schlüssel denselben maximalen Wert haben, kann einer beliebiger von ihnen zurückgegeben werden.
  """
  return max(d, key=d.get)
```

Hier ist eine Schritt-für-Schritt-Analyse:

- **`def key_of_max(d):`**: Dies definiert eine Funktion mit dem Namen `key_of_max`. Sie nimmt ein Argument `d` entgegen, das das Wörterbuch darstellt, mit dem wir arbeiten werden.
- **`return max(d, key=d.get)`**: Dies ist der Kern der Funktion. Analysieren wir ihn Schritt für Schritt:
  - **`max(d,...)`**: Die integrierte `max()`-Funktion sucht das größte Element. Standardmäßig sucht `max()`, wenn Sie ihm ein Wörterbuch übergeben, nach dem größten _Schlüssel_ (alphabetisch). Das möchten wir nicht; wir möchten den Schlüssel, der dem _größten Wert_ _zugeordnet ist_.
  - **`key=d.get`**: Dies ist der entscheidende Teil. Das `key`-Argument sagt der `max()`-Funktion, wie sie die Elemente vergleichen soll. `d.get` ist eine Methode von Wörterbüchern. Wenn Sie `d.get(ein_schluessel)` aufrufen, gibt es den _Wert_ zurück, der mit `ein_schluessel` verknüpft ist. Indem wir `key=d.get` setzen, sagen wir der `max()`-Funktion: "Vergleiche die Elemente im Wörterbuch `d` anhand ihrer _Werte_, nicht ihrer Schlüssel." Die `max()`-Funktion gibt dann den _Schlüssel_ zurück, der diesem maximalen Wert entspricht.
