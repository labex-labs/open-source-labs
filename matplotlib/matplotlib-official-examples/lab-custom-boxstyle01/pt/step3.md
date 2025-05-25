# Registrar o estilo de caixa personalizado com Matplotlib

Depois de implementar um estilo de caixa personalizado como uma classe, você pode registrá-lo com Matplotlib. Isso permite que você especifique o estilo da caixa como uma string, `bbox=dict(boxstyle="registered_name,param=value,...", ...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Registrar o estilo personalizado.
```
