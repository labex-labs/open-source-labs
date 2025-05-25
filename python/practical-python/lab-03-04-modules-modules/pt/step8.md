# Comentários sobre importação

Variações na importação _não_ alteram a forma como os módulos funcionam.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Especificamente, `import` sempre executa o arquivo _inteiro_ e os módulos ainda são ambientes isolados.

A declaração `import module as` está apenas alterando o nome localmente. A declaração `from math import cos, sin` ainda carrega o módulo math inteiro nos bastidores. Ela simplesmente copia os nomes `cos` e `sin` do módulo para o espaço local depois de concluído.
