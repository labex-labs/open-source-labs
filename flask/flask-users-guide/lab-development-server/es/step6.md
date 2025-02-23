# Ejecutar el servidor de desarrollo desde Python

Además de usar el comando de la CLI de Flask, también puede iniciar el servidor de desarrollo a partir de código Python. Agregue el siguiente código al final de su archivo `app.py`:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Ahora, puede ejecutar el servidor de desarrollo ejecutando el archivo `app.py` con Python:

```bash
python app.py
```

Esto iniciará el servidor de desarrollo y puede acceder a su aplicación Flask de la misma manera que antes.
