# Instanzmethoden

Instanzmethoden sind Funktionen, die auf Instanzen eines Objekts angewendet werden.

```python
class Player:
  ...
    # `move` ist eine Methode
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

Das Objekt selbst wird immer als erstes Argument übergeben.

```python
>>> a.move(1, 2)

# passt `a` an `self`
# passt `1` an `dx`
# passt `2` an `dy`
def move(self, dx, dy):
```

Konventionell wird die Instanz `self` genannt. Der tatsächliche Name, der verwendet wird, ist jedoch unwichtig. Das Objekt wird immer als erstes Argument übergeben. Es ist lediglich der Python-Programmierstil, diesen Argument `self` zu nennen.
