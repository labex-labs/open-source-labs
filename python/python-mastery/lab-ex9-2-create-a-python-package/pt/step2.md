# Criando a Estrutura do Pacote

Agora, vamos criar nosso pacote Python. Mas primeiro, vamos entender o que é um pacote Python. Um pacote Python é uma maneira de organizar módulos Python relacionados em uma única hierarquia de diretórios. Ele ajuda a gerenciar e reutilizar o código de forma mais eficaz. Para criar um pacote Python, precisamos seguir estes passos:

1. Crie um diretório com o nome do pacote. Este diretório servirá como o contêiner para todos os módulos que pertencem ao pacote.
2. Crie um arquivo `__init__.py` dentro deste diretório. Este arquivo é crucial porque faz com que o Python reconheça o diretório como um pacote. Quando você importa o pacote, o código em `__init__.py` é executado, o que pode ser usado para inicializar o pacote.
3. Mova nossos arquivos de módulo Python para dentro deste diretório. Este passo garante que todo o código relacionado seja agrupado dentro do pacote.

Vamos criar a estrutura do pacote passo a passo:

1. Primeiro, crie um diretório chamado `structly`. Este será o diretório raiz do nosso pacote.

```bash
mkdir structly
```

2. Em seguida, crie um arquivo `__init__.py` vazio dentro do diretório `structly`.

```bash
touch structly/__init__.py
```

O arquivo `__init__.py` pode estar vazio, mas é necessário para fazer com que o Python trate o diretório como um pacote. Quando você importa o pacote, o código em `__init__.py` é executado, o que pode ser usado para inicializar o pacote.

3. Agora, vamos mover nossos arquivos de módulo Python para o diretório `structly`. Esses arquivos de módulo contêm as funções e classes que queremos incluir em nosso pacote.

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. Verifique se todos os arquivos foram movidos corretamente. Podemos usar o comando `ls -l` para listar o conteúdo do diretório `structly`.

```bash
ls -l structly/
```

Você deve ver os seguintes arquivos listados:

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

Agora criamos uma estrutura básica de pacote. A hierarquia de diretórios deve ser assim:

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

No próximo passo, corrigiremos as instruções de importação para fazer o pacote funcionar corretamente.
