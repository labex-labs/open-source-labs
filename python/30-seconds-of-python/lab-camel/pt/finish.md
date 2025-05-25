# Resumo

Neste desafio, você aprendeu como converter uma string para camelcase removendo espaços, hífens ou underscores e capitalizando a primeira letra de cada palavra, exceto a primeira. Você usou `re.sub()` para substituir qualquer `-` ou `_` por um espaço, usando a expressão regular (regexp) `r"(_|-)+"`, `str.title()` para capitalizar a primeira letra de cada palavra e converter o restante para minúsculas, e `str.replace()` para remover espaços entre as palavras.
