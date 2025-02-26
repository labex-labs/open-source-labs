# Exécution de `unittest`

Pour exécuter les tests, convertissez le code en un script.

```python
# test_simple.py

...

if __name__ == '__main__':
    unittest.main()
```

Ensuite, exécutez Python sur le fichier de test.

```bash
$ python3 test_simple.py
F.
========================================================
ÉCHEC: test_simple (__main__.TestAdd)
--------------------------------------------------------
Traceback (most recent call last):
  File "testsimple.py", line 8, in test_simple
    self.assertEqual(r, 5)
AssertionError: 4!= 5
--------------------------------------------------------
Exécuté 2 tests en 0.000s
ÉCHEC (échecs=1)
```
