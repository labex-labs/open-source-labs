# Ejercicio 3.12: Usando tu módulo de biblioteca

En la sección 2, escribiste un programa `report.py` que producía un informe de acciones como este:

          Nombre     Acciones      Precio     Cambio
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Toma ese programa y modifícalo de modo que todo el procesamiento de archivos de entrada se realice utilizando funciones en tu módulo `fileparse`. Para hacer eso, importa `fileparse` como un módulo y cambia las funciones `read_portfolio()` y `read_prices()` para que usen la función `parse_csv()`.

Utiliza el ejemplo interactivo al principio de este ejercicio como guía. Después, deberías obtener exactamente la misma salida que antes.
