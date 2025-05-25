# Métodos de String

Strings possuem métodos que realizam diversas operações com os dados da string.

Exemplo: remoção de espaços em branco no início/fim.

```python
s = '  Hello '
t = s.strip()     # 'Hello'
```

Exemplo: Conversão de caixa (case).

```python
s = 'Hello'
l = s.lower()     # 'hello'
u = s.upper()     # 'HELLO'
```

Exemplo: Substituição de texto.

```python
s = 'Hello world'
t = s.replace('Hello' , 'Hallo')   # 'Hallo world'
```

**Mais métodos de string:**

Strings possuem uma grande variedade de outros métodos para testar e manipular os dados de texto. Este é um pequeno exemplo de métodos:

```python
s.endswith(suffix)     # Verifica se a string termina com o sufixo
s.find(t)              # Primeira ocorrência de t em s
s.index(t)             # Primeira ocorrência de t em s
s.isalpha()            # Verifica se os caracteres são alfabéticos
s.isdigit()            # Verifica se os caracteres são numéricos
s.islower()            # Verifica se os caracteres estão em minúsculas
s.isupper()            # Verifica se os caracteres estão em maiúsculas
s.join(slist)          # Junta uma lista de strings usando s como delimitador
s.lower()              # Converte para minúsculas
s.replace(old,new)     # Substitui texto
s.rfind(t)             # Busca por t a partir do final da string
s.rindex(t)            # Busca por t a partir do final da string
s.split([delim])       # Divide a string em uma lista de substrings
s.startswith(prefix)   # Verifica se a string começa com o prefixo
s.strip()              # Remove espaços em branco no início/fim
s.upper()              # Converte para maiúsculas
```
