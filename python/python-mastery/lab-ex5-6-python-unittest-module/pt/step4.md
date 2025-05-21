# Executando Testes Selecionados e Usando Descoberta de Testes

O módulo `unittest` em Python é uma ferramenta poderosa que permite testar seu código de forma eficaz. Ele fornece várias maneiras de executar testes específicos ou descobrir e executar automaticamente todos os testes em seu projeto. Isso é muito útil porque ajuda você a se concentrar em partes específicas do seu código durante os testes ou verificar rapidamente o conjunto de testes de todo o projeto.

## Executando Testes Específicos

Às vezes, você pode querer executar apenas métodos de teste ou classes de teste específicos em vez de todo o conjunto de testes. Você pode conseguir isso usando a opção de padrão com o módulo `unittest`. Isso oferece mais controle sobre quais testes são executados, o que pode ser útil ao depurar uma parte específica do seu código.

1.  Para executar apenas os testes relacionados à criação de um objeto `Stock`:

```bash
python3 -m unittest teststock.TestStock.test_create
```

Neste comando, `python3 -m unittest` diz ao Python para executar o módulo `unittest`. `teststock` é o nome do arquivo de teste, `TestStock` é o nome da classe de teste e `test_create` é o método de teste específico que queremos executar. Ao executar este comando, você pode verificar rapidamente se o código relacionado à criação de um objeto `Stock` está funcionando como esperado.

2.  Para executar todos os testes na classe `TestStock`:

```bash
python3 -m unittest teststock.TestStock
```

Aqui, omitimos o nome específico do método de teste. Portanto, este comando executará todos os métodos de teste dentro da classe `TestStock` no arquivo `teststock`. Isso é útil quando você deseja verificar a funcionalidade geral dos casos de teste do objeto `Stock`.

## Usando Descoberta de Testes

O módulo `unittest` pode descobrir e executar automaticamente todos os arquivos de teste em seu projeto. Isso evita o trabalho de especificar manualmente cada arquivo de teste a ser executado, especialmente em projetos maiores com muitos arquivos de teste.

1.  Renomeie o arquivo atual para seguir o padrão de nomenclatura de descoberta de testes:

```bash
mv teststock.py test_stock.py
```

O mecanismo de descoberta de testes em `unittest` procura arquivos que seguem o padrão de nomenclatura `test_*.py`. Ao renomear o arquivo para `test_stock.py`, facilitamos para o módulo `unittest` encontrar e executar os testes neste arquivo.

2.  Execute a descoberta de testes:

```bash
python3 -m unittest discover
```

Este comando diz ao módulo `unittest` para descobrir e executar automaticamente todos os arquivos de teste que correspondem ao padrão `test_*.py` no diretório atual. Ele pesquisará no diretório e executará todos os casos de teste encontrados nos arquivos correspondentes.

3.  Você também pode especificar um diretório para pesquisar testes:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Onde:

- `-s .` especifica o diretório para iniciar a descoberta (diretório atual neste caso). O ponto (`.`) representa o diretório atual. Você pode alterar isso para outro caminho de diretório se quiser pesquisar testes em um local diferente.
- `-p "test_*.py"` é o padrão para corresponder aos arquivos de teste. Isso garante que apenas arquivos com nomes começando com `test_` e tendo a extensão `.py` sejam considerados como arquivos de teste.

Você deve ver todos os 12 testes serem executados e passarem, como antes.

4.  Renomeie o arquivo de volta para o nome original para consistência com o laboratório:

```bash
mv test_stock.py teststock.py
```

Após executar a descoberta de testes, renomeamos o arquivo de volta para seu nome original para manter o ambiente do laboratório consistente.

Ao usar a descoberta de testes, você pode facilmente executar todos os testes em um projeto sem ter que especificar cada arquivo de teste individualmente. Isso torna o processo de teste mais eficiente e menos propenso a erros.
