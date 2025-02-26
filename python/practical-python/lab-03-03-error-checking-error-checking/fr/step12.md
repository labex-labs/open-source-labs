# Instruction `finally`

Elle spécifie le code qui doit s'exécuter que l'exception se produise ou non.

```python
lock = Lock()
...
lock.acquire()
try:
  ...
finally:
    lock.release()  # ceci sera TOUJOURS exécuté. Avec ou sans exception.
```

Utilisé couramment pour gérer de manière sûre les ressources (en particulier les verrous, les fichiers, etc.).
