# Ejecución del módulo

Cuando se importa un módulo, _todas las declaraciones del módulo se ejecutan_ una después de la otra hasta que se alcanza el final del archivo. El contenido del espacio de nombres del módulo son todos los nombres _globales_ que todavía se definen al final del proceso de ejecución. Si hay declaraciones de scripting que realizan tareas en el ámbito global (impresión, creación de archivos, etc.), las verás ejecutarse al importar.
