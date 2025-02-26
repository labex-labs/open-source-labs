# Facilitando la selección

Un problema al usar la herencia es la complejidad adicional de elegir diferentes clases para usar (por ejemplo, recordar los nombres, usar las declaraciones `import` correctas, etc.). Una función de fábrica puede simplificar esto. Agrega una función `create_formatter()` al archivo `tableformat.py` que permita a un usuario crear más fácilmente un formateador especificando un formato como `'text'`, `'csv'` o `'html'`. Por ejemplo:

```python
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('html')
>>> print_table(portfolio, ['name','shares','price'], formatter)
<tr> <th>name</th> <th>shares</th> <th>price</th> </tr>
<tr> <td>AA</td> <td>100</td> <td>32.2</td> </tr>
<tr> <td>IBM</td> <td>50</td> <td>91.1</td> </tr>
<tr> <td>CAT</td> <td>150</td> <td>83.44</td> </tr>
<tr> <td>MSFT</td> <td>200</td> <td>51.23</td> </tr>
<tr> <td>GE</td> <td>95</td> <td>40.37</td> </tr>
<tr> <td>MSFT</td> <td>50</td> <td>65.1</td> </tr>
<tr> <td>IBM</td> <td>100</td> <td>70.44</td> </tr>
>>>
```

**Discusión**

La clase `TableFormatter` en este ejercicio es un ejemplo de lo que se conoce como una "Clase Base Abstracta". No es algo que se pretende usar directamente. En cambio, está sirviendo como una especie de especificación de interfaz para un componente del programa - en este caso, los diversos formatos de salida. Esencialmente, el código que produce la tabla se programará en función de la clase base abstracta con la expectativa de que un usuario proporcione una implementación adecuada. Siempre que se hayan implementado todos los métodos requeridos, todo debería simplemente "funcionar" (ojo con los crossed fingers).
