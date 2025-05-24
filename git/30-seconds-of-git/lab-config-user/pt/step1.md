# Configurar Informações do Usuário do Git

Você acabou de começar a trabalhar em um novo projeto e deseja configurar suas informações de usuário para o Git. Você quer ter certeza de que seu nome e endereço de e-mail estão associados a quaisquer alterações que você fizer no repositório.

Para este laboratório, usaremos o repositório Git chamado `https://github.com/labex-labs/git-playground`. Siga estas etapas para configurar suas informações de usuário para este repositório:

1. Clone o repositório usando o seguinte comando:

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Navegue até o repositório clonado usando o seguinte comando:

```
cd git-playground
```

3. Use o comando `git config` para definir suas informações de usuário para o repositório. Por exemplo, se seu endereço de e-mail for `jane.doe@example.com` e seu nome for `Jane Doe`, você usaria os seguintes comandos:

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. Verifique se suas informações de usuário foram definidas corretamente usando o seguinte comando: `git config --list`. Você deve ver seu endereço de e-mail e nome listados sob as chaves `user.email` e `user.name`, respectivamente.

Este é o resultado após a conclusão do laboratório:

![Resultado da configuração do usuário do Git](../assets/challenge-config-user-step1-1.png)
