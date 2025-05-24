# Copiar um Arquivo de Outra Branch

Você está trabalhando em um projeto em um repositório Git chamado `https://github.com/labex-labs/git-playground.git`. Você tem duas branches chamadas `feature-1` e `feature-2`. Você precisa copiar o arquivo `hello.txt` da branch `feature-1` para a branch `feature-2`.

1. Clone o repositório:

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o diretório e configure a identidade:

```shell
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

3. Crie e mude para a branch `feature-1` e crie um arquivo de texto chamado `hello.txt` e escreva a string "hello,world" nele e faça o commit do arquivo com a mensagem "add hello.txt":

```shell
git checkout -b feature-1
echo "hello,world" > hello.txt
git add .
git commit -m "add hello.txt"
```

4. Crie e mude para a branch `feature-2` após mudar para a branch `master`:

```shell
git checkout master
git checkout -b feature-2
```

5. Copie o arquivo `hello.txt` da branch `feature-1` para a branch `feature-2` e faça o commit com a mensagem de commit "copy hello.txt":

```shell
git checkout feature-1 hello.txt
git commit -am "copy hello.txt"
```

6. Verifique se o arquivo `hello.txt` foi copiado para a branch `feature-2`:

```shell
ll
```

Você deve ver o arquivo `hello.txt` na lista de arquivos na branch `feature-2`:

```
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file1.txt
-rw-r--r-- 1 labex labex 15 Jul 12 22:43 file2.txt
-rw-r--r-- 1 labex labex 12 Jul 12 22:50 hello.txt
-rw-r--r-- 1 labex labex 32 Jul 12 22:43 README.md
```
