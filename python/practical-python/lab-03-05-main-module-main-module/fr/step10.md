# Sortie du programme

La sortie du programme est gérée à travers des exceptions.

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

Une alternative.

```python
import sys
sys.exit(exitcode)
```

Un code de sortie non nul indique une erreur.
