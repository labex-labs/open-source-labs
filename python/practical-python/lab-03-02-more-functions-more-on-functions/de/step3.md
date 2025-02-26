# Verwenden Sie für optionale Argumente lieber Schlüsselwortargumente

Vergleichen Sie diese beiden unterschiedlichen Aufrufstile:

```python
parse_data(data, False, True) #?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

In den meisten Fällen verbessern Schlüsselwortargumente die Klarheit des Codes - insbesondere für Argumente, die als Flags dienen oder die mit optionalen Funktionen zusammenhängen.
