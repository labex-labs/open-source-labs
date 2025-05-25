# Saída do Programa (Program Exit)

A saída do programa é tratada por meio de exceções.

```python
raise SystemExit
raise SystemExit(exitcode)
raise SystemExit('Informative message')
```

Uma alternativa.

```python
import sys
sys.exit(exitcode)
```

Um código de saída diferente de zero indica um erro.
