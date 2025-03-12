# Comprendiendo el problema

En este paso, primero entenderemos cuál es el problema que necesitamos resolver y luego echaremos un vistazo a los datos con los que trabajaremos. Este es un primer paso importante en cualquier tarea de programación, ya que nos ayuda a saber exactamente hacia dónde nos dirigimos y qué recursos tenemos a nuestra disposición.

En el directorio de tu proyecto, hay un archivo llamado `portfolio.dat`. Este archivo almacena información sobre una cartera de acciones. Una cartera es como una colección de diferentes acciones que un inversor posee. Cada línea de este archivo representa una compra individual de acciones. El formato de cada línea es el siguiente:

```
[Stock Symbol] [Number of Shares] [Price per Share]
```

El símbolo de la acción es un código corto que representa las acciones de una empresa en particular. El número de acciones nos dice cuántas unidades de esa acción se compraron, y el precio por acción es el costo de una unidad de esa acción.

Veamos un ejemplo. Consideremos la primera línea del archivo:

```
AA 100 32.20
```

Esta línea indica que se compraron 100 acciones de la acción con el símbolo "AA". Cada acción costó $32.20.

Si quieres ver lo que hay dentro del archivo `portfolio.dat`, puedes ejecutar el siguiente comando en la terminal. El comando `cat` es una herramienta útil en la terminal que te permite ver el contenido de un archivo.

```bash
cat ~/project/portfolio.dat
```

Ahora, tu tarea es crear un programa de Python llamado `pcost.py`. Este programa realizará tres tareas principales:

1. Primero, debe abrir y leer el archivo `portfolio.dat`. Abrir un archivo en Python permite que nuestro programa acceda a los datos almacenados dentro de él.
2. Luego, debe calcular el costo total de todas las compras de acciones en la cartera. Para hacer esto, para cada línea del archivo, necesitamos multiplicar el número de acciones por el precio por acción. Después de obtener estos valores para cada línea, los sumamos todos. Esto nos da la cantidad total de dinero gastado en todas las acciones de la cartera.
3. Finalmente, el programa debe mostrar el costo total. De esta manera, podemos ver el resultado de nuestros cálculos.

Comencemos creando el archivo `pcost.py`. Puedes usar el editor para abrir y editar este archivo. Ya se creó para ti durante el paso de configuración. Este archivo será el lugar donde escribirás el código de Python para resolver el problema que acabamos de discutir.
