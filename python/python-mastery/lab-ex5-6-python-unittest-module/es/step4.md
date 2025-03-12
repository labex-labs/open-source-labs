# Ejecución de pruebas seleccionadas y uso de la detección de pruebas

El módulo `unittest` en Python es una herramienta poderosa que te permite probar tu código de manera efectiva. Proporciona varias formas de ejecutar pruebas específicas o descubrir y ejecutar automáticamente todas las pruebas en tu proyecto. Esto es muy útil porque te ayuda a centrarte en partes específicas de tu código durante las pruebas o a comprobar rápidamente el conjunto de pruebas de todo el proyecto.

## Ejecución de pruebas específicas

A veces, es posible que desees ejecutar solo métodos de prueba o clases de prueba específicas en lugar de todo el conjunto de pruebas. Puedes lograr esto utilizando la opción de patrón con el módulo `unittest`. Esto te da más control sobre qué pruebas se ejecutan, lo cual puede ser útil cuando estás depurando una parte particular de tu código.

1. Para ejecutar solo las pruebas relacionadas con la creación de un objeto Stock:

```bash
python3 -m unittest teststock.TestStock.test_create
```

En este comando, `python3 -m unittest` le dice a Python que ejecute el módulo `unittest`. `teststock` es el nombre del archivo de prueba, `TestStock` es el nombre de la clase de prueba y `test_create` es el método de prueba específico que queremos ejecutar. Al ejecutar este comando, puedes comprobar rápidamente si el código relacionado con la creación de un objeto `Stock` está funcionando como se espera.

2. Para ejecutar todas las pruebas en la clase `TestStock`:

```bash
python3 -m unittest teststock.TestStock
```

Aquí, omitimos el nombre del método de prueba específico. Por lo tanto, este comando ejecutará todos los métodos de prueba dentro de la clase `TestStock` en el archivo `teststock`. Esto es útil cuando quieres comprobar la funcionalidad general de los casos de prueba del objeto `Stock`.

## Uso de la detección de pruebas

El módulo `unittest` puede descubrir y ejecutar automáticamente todos los archivos de prueba en tu proyecto. Esto te ahorra el problema de especificar manualmente cada archivo de prueba para ejecutarlo, especialmente en proyectos más grandes con muchos archivos de prueba.

1. Renombra el archivo actual para que siga el patrón de nomenclatura de detección de pruebas:

```bash
mv teststock.py test_stock.py
```

El mecanismo de detección de pruebas en `unittest` busca archivos que sigan el patrón de nomenclatura `test_*.py`. Al renombrar el archivo a `test_stock.py`, facilitamos que el módulo `unittest` encuentre y ejecute las pruebas en este archivo.

2. Ejecuta la detección de pruebas:

```bash
python3 -m unittest discover
```

Este comando le dice al módulo `unittest` que descubra y ejecute automáticamente todos los archivos de prueba que coincidan con el patrón `test_*.py` en el directorio actual. Buscará en el directorio y ejecutará todos los casos de prueba encontrados en los archivos que coincidan.

3. También puedes especificar un directorio para buscar pruebas:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Donde:

- `-s .` especifica el directorio donde comenzar la detección (en este caso, el directorio actual). El punto (`.`) representa el directorio actual. Puedes cambiar esto a otra ruta de directorio si quieres buscar pruebas en una ubicación diferente.
- `-p "test_*.py"` es el patrón para coincidir con los archivos de prueba. Esto asegura que solo se consideren como archivos de prueba los archivos cuyo nombre comience con `test_` y tenga la extensión `.py`.

Deberías ver que se ejecutan y pasan las 12 pruebas, al igual que antes.

4. Renombra el archivo de vuelta al nombre original para mantener la coherencia con el laboratorio:

```bash
mv test_stock.py teststock.py
```

Después de ejecutar la detección de pruebas, renombramos el archivo a su nombre original para mantener el entorno del laboratorio consistente.

Al utilizar la detección de pruebas, puedes ejecutar fácilmente todas las pruebas en un proyecto sin tener que especificar cada archivo de prueba individualmente. Esto hace que el proceso de prueba sea más eficiente y menos propenso a errores.
