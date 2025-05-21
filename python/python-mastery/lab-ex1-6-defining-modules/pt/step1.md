# Compreendendo os Módulos Python

Em Python, um módulo é como um contêiner que armazena definições e declarações Python. É essencialmente um arquivo, e o nome desse arquivo é o nome do módulo com a extensão `.py` adicionada no final. Pense nos módulos como caixas de ferramentas. Eles ajudam você a organizar seu código Python de forma lógica, tornando-o mais fácil de reutilizar e manter. Assim como você guardaria diferentes ferramentas em caixas separadas para melhor organização, você pode agrupar código Python relacionado em diferentes módulos.

Vamos dar uma olhada nos arquivos que foram configurados para este laboratório:

1. Primeiro, abriremos o arquivo `stock.py` no editor para ver o que há dentro. Para fazer isso, usaremos os seguintes comandos. O comando `cd` altera o diretório para a pasta `project` onde nosso arquivo está localizado, e o comando `cat` exibe o conteúdo do arquivo.

```bash
cd ~/project
cat stock.py
```

Este arquivo `stock.py` define uma classe `Stock`. Uma classe é como um modelo para criar objetos. Neste caso, a classe `Stock` representa uma ação. Ela tem atributos (que são como características) para o nome da ação, o número de ações e o preço. Também tem um método (que é como uma função associada à classe) para calcular o custo da ação.

2. Em seguida, vamos examinar o arquivo `pcost.py`. Usaremos o comando `cat` novamente para visualizar seu conteúdo.

```bash
cat pcost.py
```

Este arquivo define uma função chamada `portfolio_cost()`. Uma função é um bloco de código que executa uma tarefa específica. A função `portfolio_cost()` lê um arquivo de portfólio e calcula o custo total de todas as ações nesse portfólio.

3. Agora, vamos olhar para os dados de exemplo do portfólio. Usaremos o comando `cat` para visualizar o conteúdo do arquivo `portfolio.dat`.

```bash
cat portfolio.dat
```

Este arquivo contém dados de ações em um formato simples. Cada linha tem o símbolo da ação, o número de ações e o preço por ação.

## Usando a Declaração `import`

A declaração `import` do Python é uma ferramenta poderosa que permite que você use código de outros módulos em seu programa atual. É como pegar emprestado ferramentas de outras caixas de ferramentas. Vamos praticar o uso de diferentes maneiras de importar código:

1. Primeiro, precisamos iniciar o interpretador Python. O interpretador Python é um programa que executa código Python. Usaremos o seguinte comando para iniciá-lo.

```bash
python3
```

2. Agora, vamos importar o módulo `pcost` e ver o que acontece. Quando usamos a declaração `import`, o Python procura o arquivo `pcost.py` e disponibiliza o código dentro dele para que possamos usar.

```python
import pcost
```

Você deve ver a saída `44671.15`. Este é o custo calculado do portfólio do arquivo `portfolio.dat`. Quando o módulo `pcost` é importado, o código na parte inferior do arquivo `pcost.py` é executado automaticamente.

3. Vamos tentar chamar a função `portfolio_cost()` com um arquivo de portfólio diferente. Usaremos a sintaxe `pcost.portfolio_cost()` para chamar a função do módulo `pcost`.

```python
pcost.portfolio_cost('portfolio2.dat')
```

A saída deve ser `19908.75`, que representa o custo total das ações no segundo arquivo de portfólio.

4. Agora, vamos importar uma classe específica do módulo `stock`. Em vez de importar o módulo inteiro, podemos importar apenas a classe `Stock` usando a declaração `from...import`.

```python
from stock import Stock
```

5. Depois de importar a classe `Stock`, podemos criar um objeto `Stock`. Um objeto é uma instância de uma classe. Criaremos um objeto `Stock` com o nome `GOOG`, 100 ações e um preço de `490.10`. Em seguida, imprimiremos o nome da ação e calcularemos seu custo usando o método `cost()`.

```python
s = Stock('GOOG', 100, 490.10)
print(s.name)
print(s.cost())
```

A saída deve ser:

```
GOOG
49010.0
```

6. Finalmente, quando terminarmos de usar o interpretador Python, podemos sair dele usando a função `exit()`.

```python
exit()
```

Este laboratório demonstrou duas maneiras diferentes de importar código Python:

- `import module_name` - Isso importa o módulo inteiro, tornando todas as funções, classes e variáveis ​​nesse módulo disponíveis para uso.
- `from module_name import specific_item` - Isso importa apenas um item específico (como uma classe ou uma função) do módulo, o que pode ser útil se você precisar apenas de uma parte da funcionalidade do módulo.
