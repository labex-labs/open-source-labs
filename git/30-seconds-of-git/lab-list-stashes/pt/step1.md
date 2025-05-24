# Listar Todos os Stashes

Você está trabalhando em um projeto em um repositório Git e fez algumas alterações que ainda não estão prontas para serem _commitadas_ (confirmadas). Você decide fazer o _stash_ (armazenamento temporário) dessas alterações para poder trabalhar em uma tarefa diferente. Mais tarde, você quer ver uma lista de todos os _stashes_ que criou para poder decidir qual aplicar. Como você lista todos os _stashes_ em um repositório Git?

1. Navegue até o diretório `git-playground`:

```
cd git-playground
```

2. Crie um novo arquivo chamado `test.txt` e adicione algum conteúdo a ele:

```
echo "hello,world" > test.txt
git add .
```

3. Use o seguinte comando para fazer o _stash_ (armazenamento temporário) de suas alterações:

```
git stash save "Added test.txt"
```

4. Crie outro novo arquivo chamado `test2.txt` e adicione algum conteúdo a ele:

```
echo "hello,labex" > test2.txt
git add .
```

5. Use o seguinte comando para fazer o _stash_ (armazenamento temporário) de suas alterações:

```
git stash save "Added test2.txt"
```

6. Use o seguinte comando para listar todos os _stashes_:

```
git stash list
```

Você deve ver uma saída semelhante à seguinte:

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
