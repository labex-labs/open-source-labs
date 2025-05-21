# Usando o Módulo inspect

Em Python, a biblioteca padrão vem com um módulo `inspect` muito útil. Este módulo é como uma ferramenta de detetive que nos ajuda a reunir informações sobre objetos ativos (live objects) em Python. Objetos ativos podem ser coisas como módulos, classes e funções. Em vez de cavar manualmente nos atributos de um objeto para encontrar informações, o módulo `inspect` fornece maneiras mais organizadas e de alto nível de entender as propriedades das funções.

Vamos continuar usando o mesmo shell interativo Python para explorar como este módulo funciona.

## Assinaturas de Funções (Function Signatures)

A função `inspect.signature()` é uma ferramenta útil. Quando você passa uma função para ela, ela retorna um objeto `Signature`. Este objeto contém detalhes importantes sobre os parâmetros da função.

Aqui está um exemplo. Suponha que temos uma função chamada `add`. Podemos usar a função `inspect.signature()` para obter sua assinatura:

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

Quando você executar este código, a saída será:

```
(x, y)
```

Esta saída nos mostra a assinatura da função, que nos diz quais parâmetros a função pode aceitar.

## Examinando Detalhes dos Parâmetros

Podemos ir um passo além e obter informações mais detalhadas sobre cada parâmetro da função.

```python
print(sig.parameters)
```

A saída deste código será:

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

Os parâmetros da função são armazenados em um dicionário ordenado. Às vezes, podemos estar interessados apenas nos nomes dos parâmetros. Podemos converter este dicionário ordenado em uma tupla para extrair apenas os nomes dos parâmetros.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

A saída será:

```
('x', 'y')
```

## Examinando Parâmetros Individuais

Também podemos dar uma olhada mais de perto em cada parâmetro individual. O código a seguir percorre cada parâmetro na função e imprime alguns detalhes importantes sobre ele.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

Este código mostrará detalhes sobre cada parâmetro. Ele nos diz o tipo do parâmetro (se é um parâmetro posicional, um parâmetro de palavra-chave, etc.) e seu valor padrão, se tiver um.

O módulo `inspect` tem muitas outras funções úteis para introspecção de funções. Aqui estão alguns exemplos:

- `inspect.getdoc(obj)`: Esta função recupera a string de documentação para um objeto. Strings de documentação são como notas que os programadores escrevem para explicar o que um objeto faz.
- `inspect.getfile(obj)`: Ela nos ajuda a descobrir o arquivo onde um objeto é definido. Isso pode ser muito útil quando queremos localizar o código-fonte de um objeto.
- `inspect.getsource(obj)`: Esta função busca o código-fonte de um objeto. Ela nos permite ver exatamente como o objeto é implementado.
