# Comprender los paquetes de Python

Antes de comenzar a crear un paquete de Python, entendamos qué es un paquete de Python. Un paquete de Python es esencialmente un directorio. Dentro de este directorio, hay múltiples archivos de módulos de Python, que son simplemente archivos `.py` que contienen código de Python. Además, hay un archivo especial llamado `__init__.py`. Este archivo puede estar vacío, pero su presencia indica que el directorio es un paquete de Python. El propósito de esta estructura es ayudarte a organizar el código relacionado en una única jerarquía de directorios.

Los paquetes ofrecen varios beneficios. En primer lugar, te permiten estructurar tu código de manera lógica. En lugar de tener todos tus archivos de Python dispersos, puedes agrupar la funcionalidad relacionada en un paquete. En segundo lugar, ayudan a evitar conflictos de nombres entre módulos. Dado que los paquetes crean un espacio de nombres (namespace), puedes tener módulos con el mismo nombre en diferentes paquetes sin ningún problema. En tercer lugar, facilitan la importación y el uso de tu código. Puedes importar un paquete completo o módulos específicos de él con facilidad.

Ahora, echemos un vistazo a los archivos que actualmente tenemos en nuestro directorio de proyecto. Para listar los archivos, usaremos el siguiente comando en la terminal:

```bash
ls -l
```

Cuando ejecutes este comando, deberías ver los siguientes archivos:

```
portfolio.csv
reader.py
stock.py
structure.py
tableformat.py
validate.py
```

Estos archivos de Python están todos relacionados y trabajan juntos, pero actualmente son solo módulos separados. En este laboratorio, nuestro objetivo es organizarlos en un paquete coherente llamado `structly`.

Comprendamos brevemente qué hace cada archivo:

- `structure.py`: Este archivo define una clase base `Structure` y varios descriptores. Estos descriptores se utilizan para la validación de tipos, lo que significa que ayudan a garantizar que los datos utilizados en tu programa tengan el tipo correcto.
- `validate.py`: Contiene la funcionalidad de validación que utiliza el módulo `structure`. Esto ayuda a validar los datos de acuerdo con ciertas reglas.
- `reader.py`: Este archivo proporciona funciones que se utilizan para leer datos CSV. CSV (Comma-Separated Values, Valores Separados por Comas) es un formato de archivo común para almacenar datos tabulares.
- `tableformat.py`: Contiene clases y funciones que se utilizan para formatear datos en tablas. Esto es útil cuando quieres mostrar los datos de manera más organizada.
- `stock.py`: Este archivo utiliza los otros módulos para definir una clase `Stock` y procesar datos de acciones. Combina la funcionalidad de los otros módulos para realizar tareas específicas relacionadas con los datos de acciones.

En el siguiente paso, crearemos nuestra estructura de paquete.
