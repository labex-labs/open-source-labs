# Melhorando a Experiência no Shell

Para melhorar a experiência no shell, crie um módulo (`shelltools.py`) com métodos auxiliares que podem ser importados para a sessão interativa. Este módulo pode conter métodos auxiliares adicionais para tarefas como inicializar o banco de dados ou remover tabelas.

```python
# File: shelltools.py

def initialize_database():
    # Code to initialize the database
    pass

def drop_tables():
    # Code to drop tables
    pass
```

No shell interativo, importe os métodos desejados do módulo `shelltools`.

```python
# File: shell.py
# Execution: python shell.py

from shelltools import initialize_database, drop_tables

# Import desired methods from shelltools module
from shelltools import *

# Use imported methods
initialize_database()
drop_tables()
```
