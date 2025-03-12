# Experimentación interactiva

Python ofrece un modo interactivo que te permite ejecutar código de inmediato. Esto es muy útil para probar tu código y probar cosas nuevas. En este paso, aprenderemos cómo llamar a una función directamente desde el intérprete de Python.

## Ejecución de Python en modo interactivo

Para ejecutar un script de Python y luego entrar en el modo interactivo, puedes usar la bandera `-i`. Esta bandera le dice a Python que siga ejecutándose en un estado interactivo después de ejecutar el script. Así es como se hace:

```bash
cd /home/labex/project
python3 -i pcost.py
```

Desglosemos lo que hace este comando:

1. Primero, `cd /home/labex/project` cambia el directorio actual a `/home/labex/project`. Aquí es donde se encuentra nuestro script `pcost.py`.
2. Luego, `python3 -i pcost.py` ejecuta el script `pcost.py`. Después de que el script termine de ejecutarse, Python permanece en modo interactivo.
3. En modo interactivo, puedes escribir comandos de Python directamente en la terminal.

Después de ejecutar el comando, verás la salida del script `pcost.py`, seguida del indicador de Python (`>>>`). Este indicador indica que ahora puedes ingresar comandos de Python.

## Llamada a tu función de forma interactiva

Una vez que estés en el modo interactivo, puedes llamar a la función `portfolio_cost()` con diferentes nombres de archivo. Esto te permite ver cómo se comporta la función con diversas entradas. Aquí tienes un ejemplo:

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

Utilizando este enfoque interactivo, puedes:

- Probar tu función con diferentes entradas para ver si funciona como se espera.
- Experimentar con el comportamiento de la función en diversas condiciones.
- Depurar tu código sobre la marcha viendo los resultados inmediatos de tus llamadas a la función.

## Beneficios del modo interactivo

El modo interactivo tiene varios beneficios:

1. Puedes probar rápidamente diferentes escenarios sin tener que ejecutar todo el script cada vez.
2. Puedes inspeccionar variables y resultados de expresiones inmediatamente, lo que te ayuda a entender lo que está sucediendo en tu código.
3. Puedes probar pequeños fragmentos de código sin crear un programa completo. Esto es genial para aprender y probar nuevas ideas.
4. Es una excelente manera de aprender y experimentar con Python porque obtienes retroalimentación instantánea.

## Salida del modo interactivo

Cuando hayas terminado de experimentar, puedes salir del modo interactivo de dos maneras:

- Escribe `exit()` y presiona Enter. Esta es una forma directa de terminar la sesión interactiva.
- Presiona Ctrl+D (en Unix/Linux). Esta es una combinación de teclas que también sale del modo interactivo.

A lo largo de tu viaje de programación en Python, la técnica de definir funciones y probarlas de forma interactiva será extremadamente valiosa para el desarrollo y la depuración. Te permite iterar rápidamente en tu código y encontrar y corregir problemas.
