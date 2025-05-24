# Obter o Nome da _Branch_ Atual

Escreva um comando que imprima o nome da _branch_ atual em um repositório Git.

Suponha que você esteja trabalhando em um projeto armazenado no repositório `https://github.com/labex-labs/git-playground`. Você fez algumas alterações no arquivo `README.md` e deseja confirmá-las na _branch_ atual. No entanto, antes de fazer isso, você quer ter certeza de que está na _branch_ correta.

Para verificar a _branch_ atual, você pode usar o seguinte comando:

```shell
git rev-parse --abbrev-ref HEAD
```

Isso imprimirá o nome da _branch_ atual no console. Por exemplo, se você estiver atualmente na _branch_ `master`, a saída será:

```shell
master
```

Se você mudar para uma _branch_ diferente, como `feature-branch`, a saída mudará de acordo:

```shell
git checkout -b feature-branch
git rev-parse --abbrev-ref HEAD
```

Isso exibirá:

```shell
feature-branch
```
