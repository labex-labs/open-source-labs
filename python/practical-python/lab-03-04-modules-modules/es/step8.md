# Comentarios sobre la importación

Las variaciones en la importación _no_ cambian la forma en que funcionan los módulos.

```python
import math
# vs
import math as m
# vs
from math import cos, sin
...
```

Especificamente, `import` siempre ejecuta todo el archivo y los módulos siguen siendo entornos aislados.

La declaración `import módulo as` solo está cambiando el nombre localmente. La declaración `from math import cos, sin` todavía carga todo el módulo math en segundo plano. Simplemente está copiando los nombres `cos` y `sin` del módulo al espacio local una vez que ha terminado.
