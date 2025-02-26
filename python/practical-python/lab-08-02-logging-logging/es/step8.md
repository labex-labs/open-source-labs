# Ejercicio 8.3: Agregar registro a un programa

Para agregar registro a una aplicación, necesitas tener algún mecanismo para inicializar el módulo de registro en el módulo principal. Una forma de hacer esto es incluir un código de configuración que se ve como esto:

    # Este archivo configura la configuración básica del módulo de registro.
    # Cambia las configuraciones aquí para ajustar la salida del registro según sea necesario.
    import logging
    logging.basicConfig(
        filename = 'app.log',            # Nombre del archivo de registro (omite para usar stderr)
        filemode = 'w',                  # Modo de archivo (usa 'a' para adjuntar)
        level    = logging.WARNING,      # Nivel de registro (DEBUG, INFO, WARNING, ERROR o CRITICAL)
    )

Nuevamente, necesitarías poner esto en algún lugar de los pasos de inicio de tu programa. Por ejemplo, ¿dónde pondrías esto en tu programa `report.py`?
