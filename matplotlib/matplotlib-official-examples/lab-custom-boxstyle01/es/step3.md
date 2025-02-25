# Registrar el estilo de caja personalizado con Matplotlib

Una vez que haya implementado un estilo de caja personalizado como una clase, puede registrarlo con Matplotlib. Esto le permite especificar el estilo de caja como una cadena, `bbox=dict(boxstyle="nombre_registrado,param=valor,...",...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Registra el estilo personalizado.
```
