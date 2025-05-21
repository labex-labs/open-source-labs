# Criando a Função Básica

Vamos começar criando o núcleo da nossa função. Vamos construí-la passo a passo. Primeiro, crie um arquivo chamado `key_of_max.py`. Você pode usar o editor de código LabEx integrado ou um editor baseado em terminal como `nano` ou `vim`. Dentro de `key_of_max.py`, adicione o seguinte código:

![Editor de código com a função key_of_max](../assets/20250214-14-44-53-838b9T58.png)

```python
def key_of_max(d):
  """
  Retorna a chave associada ao valor máximo no dicionário 'd'.

  Se várias chaves compartilharem o valor máximo, qualquer uma delas pode ser retornada.
  """
  return max(d, key=d.get)
```

Aqui está uma análise:

- **`def key_of_max(d):`**: Isso define uma função chamada `key_of_max`. Ela recebe um argumento, `d`, que representa o dicionário com o qual trabalharemos.
- **`return max(d, key=d.get)`**: Este é o coração da função. Vamos analisá-lo parte por parte:
  - **`max(d, ...)`**: A função `max()` integrada encontra o maior item. Por padrão, se você fornecer um dicionário para `max()`, ele encontrará a maior _chave_ (alfabeticamente). Não queremos isso; queremos a chave _associada ao_ maior _valor_.
  - **`key=d.get`**: Esta é a parte crucial. O argumento `key` diz a `max()` como comparar os itens. `d.get` é um método de dicionários. Quando você chama `d.get(some_key)`, ele retorna o _valor_ associado a `some_key`. Ao definir `key=d.get`, estamos dizendo a `max()`: "Compare os itens no dicionário `d` usando seus _valores_, não suas chaves." A função `max()` então retorna a _chave_ correspondente a esse valor máximo.
