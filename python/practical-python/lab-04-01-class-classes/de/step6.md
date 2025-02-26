# Klassenscopierung

Klassen definieren keinen Namensbereich.

```python
class Player:
 ...
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def left(self, amt):
        move(-amt, 0)       # NEIN. Ruft eine globale `move`-Funktion auf
        self.move(-amt, 0)  # JA. Ruft die Methode `move` aus oben auf.
```

Wenn Sie auf einer Instanz operieren möchten, verweisen Sie immer explizit darauf (z.B. `self`).

Ab diesem Satz von Übungen beginnen wir eine Reihe von Änderungen am vorhandenen Code aus vorherigen Abschnitten vorzunehmen. Es ist von entscheidender Bedeutung, dass Sie eine funktionierende Version von Übung 3.18 haben, um zu beginnen. Wenn Sie das nicht haben, arbeiten Sie bitte anhand des Lösungscodes, der sich im Verzeichnis `Lösungen/3_18` befindet. Es ist in Ordnung, ihn zu kopieren.
