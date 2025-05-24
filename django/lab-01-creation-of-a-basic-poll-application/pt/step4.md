# Criando o aplicativo Polls

Agora que seu ambiente -- um "projeto" -- está configurado, você está pronto para começar a trabalhar.

Cada aplicação que você escreve em Django consiste em um pacote Python que segue uma certa convenção. Django vem com um utilitário que gera automaticamente a estrutura básica de diretórios de um aplicativo, para que você possa se concentrar em escrever código em vez de criar diretórios.

> Projetos vs. aplicativos
> Qual é a diferença entre um projeto e um aplicativo? Um aplicativo é uma aplicação web que faz algo -- por exemplo, um sistema de blog, um banco de dados de registros públicos ou um pequeno aplicativo de enquetes. Um projeto é uma coleção de configurações e aplicativos para um determinado site. Um projeto pode conter vários aplicativos. Um aplicativo pode estar em vários projetos.

Seus aplicativos podem viver em qualquer lugar no seu `Python path <tut-searchpath>`. Neste tutorial, criaremos nosso aplicativo de enquetes no mesmo diretório do seu arquivo `manage.py` para que ele possa ser importado como seu próprio módulo de nível superior, em vez de um submódulo de `mysite`.

Para criar seu aplicativo, certifique-se de estar no mesmo diretório que `manage.py` e digite este comando:

```bash
cd ~/project/mysite
python manage.py startapp polls
```

Isso criará um diretório `polls`, que é organizado assim:

```plaintext
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

Esta estrutura de diretórios abrigará a aplicação de enquetes.
