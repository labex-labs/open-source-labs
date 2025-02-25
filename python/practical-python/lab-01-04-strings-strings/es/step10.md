# Cadenas sin procesar

Las cadenas sin procesar son literales de cadena con una barra invertida no interpretada. Se especifican prefijando la comilla inicial con una "r" minúscula.

```python
>>> rs = r'c:\newdata\test' # Sin procesar (barra invertida no interpretada)
>>> rs
'c:\\newdata\\test'
```

La cadena es el texto literal encerrado dentro, exactamente como se escribió. Esto es útil en situaciones donde la barra invertida tiene un significado especial. Ejemplo: nombre de archivo, expresiones regulares, etc.
