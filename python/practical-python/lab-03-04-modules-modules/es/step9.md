# Carga del módulo

Cada módulo se carga y ejecuta solo _una vez_. _Nota: Las importaciones repetidas solo devuelven una referencia al módulo cargado previamente._

`sys.modules` es un diccionario de todos los módulos cargados.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath',...]
>>>
```

**Precaución:** Si repites una declaración `import` después de cambiar el código fuente de un módulo, puede surgir una confusión común. Debido a la memoria caché de los módulos `sys.modules`, las importaciones repetidas siempre devuelven el módulo cargado previamente, incluso si se ha realizado un cambio. La forma más segura de cargar código modificado en Python es cerrar y reiniciar el intérprete.
