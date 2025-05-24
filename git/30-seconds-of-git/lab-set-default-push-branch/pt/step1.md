# Definir o Nome da Branch de Envio (Push) Padrão

Ao enviar (push) alterações para um repositório remoto, o Git usará o nome da branch local atual como o nome padrão para a branch remota. No entanto, às vezes você pode querer enviar suas alterações para uma branch diferente. Nesse caso, você precisaria especificar o nome da branch remota explicitamente toda vez que enviar suas alterações. Isso pode ser tedioso e propenso a erros, especialmente se você estiver trabalhando com várias branches.

Para completar este laboratório, você usará o repositório Git `git-playground` da sua conta do GitHub, que vem de um fork de `https://github.com/labex-labs/git-playground.git`. Siga os passos abaixo para definir o nome da branch de envio (push) padrão:

1. Clone o repositório usando o seguinte comando:
   ```
   git clone https://github.com/your-username/git-playground.git
   ```
2. Mude para o diretório do repositório:
   ```
   cd git-playground
   ```
3. Defina o nome da branch de envio (push) padrão para o nome da branch local atual:
   ```
   git config push.default current
   ```
4. Crie uma nova branch e mude para ela:
   ```
   git checkout -b my-branch
   ```
5. Faça algumas alterações no repositório e faça o commit:
   ```
   echo "Hello, World" > hello.txt
   git add hello.txt
   git commit -m "Add hello.txt"
   ```
6. Envie (push) suas alterações para o repositório remoto:
   ```
   git push -u
   ```
   O Git enviará suas alterações para uma branch chamada `my-branch` no repositório remoto.

Este é o resultado da execução de `git log`:

```shell
ADD hello.txt
```
