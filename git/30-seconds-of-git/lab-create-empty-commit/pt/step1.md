# Criar um Commit Vazio

Você precisa criar um _commit_ vazio em seu repositório Git. Isso pode ser útil em vários cenários, como:

- Acionar um processo de _build_
- Criar um _commit_ _placeholder_
- Marcar um ponto específico no histórico do repositório

Para este laboratório, vamos usar o repositório de `https://github.com/labex-labs/git-playground`:

1. Clone o repositório para sua máquina local usando o comando `git clone https://github.com/labex-labs/git-playground`.
2. Navegue até o diretório do repositório usando o comando `cd git-playground` e configure sua conta do GitHub no ambiente usando os comandos `git config --global user.name "your-uername"` e `git config --global user.email "your-email"`.
3. Use o comando `git commit --allow-empty -m "Empty commit"` para criar um _commit_ vazio com a mensagem "Empty commit".
4. Verifique se o _commit_ vazio foi criado usando o comando `git log --name-status HEAD^..HEAD`.

Aqui é onde você executa `git log --name-status HEAD^..HEAD` e o resultado:

![git log empty commit result](../assets/challenge-create-empty-commit-step1-1.png)
