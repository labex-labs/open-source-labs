# Namespaces (Espaços de Nomes)

Um módulo é uma coleção de valores nomeados e às vezes é dito ser um _namespace_ (espaço de nomes). Os nomes são todas as variáveis globais e funções definidas no arquivo fonte. Após a importação, o nome do módulo é usado como um prefixo. Daí o _namespace_ (espaço de nomes).

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

O nome do módulo está diretamente ligado ao nome do arquivo (foo -> foo.py).
