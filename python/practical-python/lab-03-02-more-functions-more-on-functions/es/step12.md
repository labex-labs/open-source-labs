# Reasignación vs Modificación

Asegúrese de entender la sutil diferencia entre modificar un valor y reasignar un nombre de variable.

```python
def foo(items):
    items.append(42)    # Modifica el objeto de entrada

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]

# VS
def bar(items):
    items = [4,5,6]    # Cambia la variable local `items` para que apunte a un objeto diferente

b = [1, 2, 3]
bar(b)
print(b)                # [1, 2, 3]
```

_Recordatorio: La asignación de variables nunca sobrescribe la memoria. El nombre simplemente se vincula a un nuevo valor._

Este conjunto de ejercicios le pide que implemente lo que, quizás, es la parte más poderosa y difícil del curso. Hay muchos pasos y muchos conceptos de ejercicios anteriores se ponen juntos de una vez. La solución final es de solo alrededor de 25 líneas de código, pero tome su tiempo y asegúrese de entender cada parte.

Una parte central de su programa `report.py` se centra en la lectura de archivos CSV. Por ejemplo, la función `read_portfolio()` lee un archivo que contiene filas de datos de cartera y la función `read_prices()` lee un archivo que contiene filas de datos de precios. En ambas funciones, hay muchos detalles "fastidiosos" de bajo nivel y características similares. Por ejemplo, ambas abren un archivo y lo envuelven con el módulo `csv` y ambas convierten varios campos en nuevos tipos.

Si estuviera haciendo mucha análisis de archivos en serio, probablemente querría limpiar algo de esto y hacerlo más general. Ese es nuestro objetivo.

Comience este ejercicio abriendo el archivo llamado `fileparse.py`. Aquí es donde estaremos trabajando.
