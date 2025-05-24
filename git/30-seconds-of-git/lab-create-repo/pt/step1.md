# Criar um Novo Repositório (Repository)

Aprendemos como clonar um repositório Git existente. Agora, vamos criar um novo repositório Git do zero.

Abra seu terminal ou prompt de comando e siga os passos abaixo para criar um novo repositório Git:

```bash
cd ~/project
git init my_repo
```

Isso criará um novo diretório chamado `my_repo` no seu diretório de trabalho atual e inicializará um novo repositório Git dentro dele.

Vamos ver o que está dentro do diretório `my_repo`:

```bash
ls -a my_repo
```

Você deve ver os seguintes arquivos e diretórios:

```plaintext
.  ..  .git
```

Os diretórios `.` e `..` são diretórios especiais que representam o diretório atual e o diretório pai, respectivamente.

O diretório `.git` é onde o Git armazena todos os arquivos de configuração e o histórico de versões do repositório.

Tente executar o seguinte comando para ver os arquivos e diretórios dentro do diretório `.git`:

```bash
ls -a my_repo/.git
```

Você deve ver os seguintes arquivos e diretórios:

```plaintext
.  ..  branches  config  description  HEAD  hooks  info  objects  ref
```

- O diretório `branches` contém referências aos branches (ramificações) no repositório.
- O arquivo `config` contém as configurações específicas do repositório.
- O arquivo `description` contém uma breve descrição do repositório.
- O arquivo `HEAD` contém uma referência ao branch (ramificação) atualmente verificado (checked out).
- O diretório `hooks` contém scripts que podem ser acionados por eventos Git.
- O diretório `info` contém arquivos de informações globais.
- O diretório `objects` contém todos os objetos no repositório.
- O diretório `ref` contém referências aos commits no repositório.

Não precisamos nos preocupar com o conteúdo do diretório `.git` por enquanto. Apenas lembre-se de que é onde o Git armazena todas as informações sobre o repositório.
