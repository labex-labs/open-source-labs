# Optionen abrufen und setzen

Wir können den Wert einer einzelnen Option mithilfe von `pd.get_option` bzw. `pd.set_option` abrufen oder setzen. Hier setzen wir die maximale Anzahl von angezeigten Zeilen auf 999.

```python
# Get the current setting for maximum display rows
print(pd.options.display.max_rows)

# Set the maximum display rows to 999
pd.options.display.max_rows = 999

# Verify the new setting
print(pd.options.display.max_rows)
```
