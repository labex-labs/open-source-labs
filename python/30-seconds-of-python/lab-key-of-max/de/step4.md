# Testen des leeren Wörterbuchs (Randfall)

Fügen wir einen speziellen Test für den Fall eines leeren Wörterbuchs hinzu. Fügen Sie diese Methode zur `TestKeyOfMax`-Klasse in der Datei `test_key_of_max.py` hinzu:

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: Diese Behauptung (assertion) prüft, ob der Wert genau `None` ist. Dies ist wichtig, da `self.assertEqual(..., None)` für Dinge, die _zu_ `None` _ausgewertet_ werden, aber nicht tatsächlich `None` sind, bestanden werden könnte. `assertIsNone` ist strenger.

Führen Sie die Tests erneut aus (`python3 test_key_of_max.py`). Alle drei Tests (die beiden grundlegenden Tests und der Test für das leere Wörterbuch) sollten jetzt bestanden werden.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
