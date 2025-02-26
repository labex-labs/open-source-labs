# Préférez les arguments nommés pour les arguments facultatifs

Comparez et contrastez ces deux styles d'appel différents :

```python
parse_data(data, False, True) #?????

parse_data(data, ignore_errors=True)
parse_data(data, debug=True)
parse_data(data, debug=True, ignore_errors=True)
```

Dans la plupart des cas, les arguments nommés améliorent la clarté du code - en particulier pour les arguments qui servent de drapeaux ou qui sont liés à des fonctionnalités facultatives.
