# Registrieren des benutzerdefinierten Box-Stils bei Matplotlib

Sobald Sie einen benutzerdefinierten Box-Stil als Klasse implementiert haben, können Sie ihn bei Matplotlib registrieren. Dies ermöglicht es Ihnen, den Box-Stil als Zeichenfolge anzugeben, `bbox=dict(boxstyle="registrierter_name,param=value,...",...)`.

```python
BoxStyle._style_list["angled"] = MyStyle  # Registriere den benutzerdefinierten Stil.
```
