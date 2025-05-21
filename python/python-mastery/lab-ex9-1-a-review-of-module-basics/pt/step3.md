# Compreendendo o Comportamento de Carregamento de Módulos

Em Python, a maneira como os módulos são carregados tem algumas características interessantes. Nesta etapa, exploraremos esses comportamentos para entender como o Python gerencia o carregamento de módulos.

1. Primeiro, vamos ver o que acontece quando tentamos importar um módulo novamente dentro da mesma sessão do interpretador Python. Quando você inicia um interpretador Python, é como abrir um espaço de trabalho onde você pode executar código Python. Depois de importar um módulo, importá-lo novamente pode parecer que recarregaria o módulo, mas esse não é o caso.

```python
>>> import simplemod
```

Observe que desta vez você não vê a saída "Loaded simplemod". Isso ocorre porque **o Python carrega um módulo apenas uma vez** por sessão do interpretador. Instruções `import` subsequentes não recarregam o módulo. O Python lembra que já carregou o módulo, então não passa pelo processo de carregá-lo novamente.

2. Depois de importar um módulo, você pode modificar as variáveis dentro dele. Um módulo em Python é como um contêiner que contém variáveis, funções e classes. Depois de importar um módulo, você pode acessar e alterar suas variáveis como faria com qualquer outro objeto Python.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Aqui, primeiro verificamos o valor da variável `x` no módulo `simplemod`, que é inicialmente `42`. Em seguida, alteramos seu valor para `13` e verificamos se a alteração foi feita. Quando chamamos a função `foo` no módulo, ela reflete o novo valor de `x`.

3. Importar o módulo novamente não redefine as alterações que fizemos em suas variáveis. Mesmo que tentemos importar o módulo mais uma vez, o Python não o recarrega, então as alterações que fizemos em suas variáveis permanecem.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. Se você quiser recarregar um módulo à força, precisará usar a função `importlib.reload()`. Às vezes, você pode ter feito alterações no código do módulo e deseja ver essas alterações entrarem em vigor imediatamente. A função `importlib.reload()` permite que você faça exatamente isso.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

O módulo foi recarregado e o valor de `x` foi redefinido para `42`. Isso mostra que o módulo foi carregado novamente a partir de seu código-fonte e todas as variáveis foram inicializadas como eram originalmente.

5. O Python acompanha todos os módulos carregados no dicionário `sys.modules`. Este dicionário atua como um registro onde o Python armazena informações sobre todos os módulos que foram carregados durante a sessão atual do interpretador.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

Verificando se o nome de um módulo está no dicionário `sys.modules`, você pode ver se o módulo foi carregado. E acessando o dicionário com o nome do módulo como chave, você pode obter informações sobre o módulo.

6. Você pode remover um módulo deste dicionário para forçar o Python a recarregá-lo na próxima importação. Se você remover um módulo do dicionário `sys.modules`, o Python esquece que já carregou o módulo. Portanto, da próxima vez que você tentar importá-lo, o Python o carregará novamente a partir de seu código-fonte.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

O módulo foi carregado novamente porque foi removido de `sys.modules`. Esta é outra maneira de garantir que você está trabalhando com a versão mais recente do código de um módulo.
