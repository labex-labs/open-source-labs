# Autocorreção de Comandos Git

O problema é que os desenvolvedores frequentemente digitam comandos Git incorretamente, o que pode levar a erros e retardar seu fluxo de trabalho. Por exemplo, um desenvolvedor pode acidentalmente digitar `git sttaus` em vez de `git status`, o que resultará em uma mensagem de erro. Isso pode ser frustrante e demorado, especialmente ao trabalhar em projetos grandes com muitos arquivos e colaboradores.

Para demonstrar como usar o recurso de autocorreção do Git, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground` diretório.

1. Abra seu terminal e navegue até o diretório onde deseja clonar o repositório.
2. Clone o repositório usando o seguinte comando:

```
git clone https://github.com/labex-labs/git-playground.git
```

3. Navegue até o repositório clonado usando o seguinte comando:

```
cd git-playground
```

4. Habilite o recurso de autocorreção do Git usando o seguinte comando:

```
git config --global help.autocorrect 1
```

5. Tente digitar incorretamente um comando Git, como `git sttaus`. O Git corrigirá automaticamente o comando e executará `git status` em vez disso.

Este é o resultado após concluir o laboratório:

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
