# Sigue adelante

Oh, puedes hacerlo mejor que eso. Vamos a integrarlo en tu código de generación de tablas. Cambia el programa al siguiente:

```python
# ticker.py
...

if __name__ == '__main__':
    from follow import follow
    import csv
    from tableformat import create_formatter, print_table

    formatter = create_formatter('text')

    lines = follow('stocklog.csv')
    rows = csv.reader(lines)
    records = (Ticker.from_row(row) for row in rows)
    negative = (rec for rec in records if rec.change < 0)
    print_table(negative, ['name','price','change'], formatter)
```

Esto debería producir una salida que se vea así:

          name      price     change
    ---------- ---------- ----------
             C      53.12      -0.21
           UTX      70.04      -0.19
           AXP      62.86      -0.18
           MMM      85.72      -0.22
           MCD      51.38      -0.03
           WMT      49.85      -0.23
            KO       51.6      -0.07
           AIG      71.39      -0.14
            PG      63.05      -0.02
            HD      37.76      -0.19

Ahora, ¡eso es loco! Y bastante impresionante.

**Discusión**

Algunas lecciones aprendidas: Puedes crear varias funciones generadoras y enlazarlas para realizar un procesamiento que involucre tuberías de flujo de datos.

Un buen modelo mental para las funciones generadoras podría ser bloques de Lego. Puedes crear una colección de pequeños patrones de iterador y comenzar a apilarlos de diferentes maneras. Puede ser una forma extremadamente poderosa de programar.
