# Criando um projeto

Se esta é a sua primeira vez usando o Django, você precisará cuidar de algumas configurações iniciais. Especificamente, você precisará gerar automaticamente algum código que estabelece um `project` do Django -- uma coleção de configurações para uma instância do Django, incluindo configuração de banco de dados, opções específicas do Django e configurações específicas da aplicação.

Na linha de comando, use `cd` para entrar em um diretório onde você gostaria de armazenar seu código e, em seguida, execute o seguinte comando:

```bash
cd ~/project
django-admin startproject mysite
```

Isso criará um diretório `mysite` no seu diretório atual.

Vamos dar uma olhada no que `startproject` criou:

```plaintext
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

Esses arquivos são:

- O diretório raiz externo `mysite/` é um contêiner para o seu projeto. Seu nome não importa para o Django; você pode renomeá-lo para o que quiser.
- `manage.py`: Um utilitário de linha de comando que permite interagir com este projeto Django de várias maneiras.
- O diretório interno `mysite/` é o pacote Python real para o seu projeto. Seu nome é o nome do pacote Python que você precisará usar para importar qualquer coisa dentro dele (por exemplo, `mysite.urls`).
- `mysite/__init__.py`: Um arquivo vazio que informa ao Python que este diretório deve ser considerado um pacote Python.
- `mysite/settings.py`: Configurações/configuração para este projeto Django.
- `mysite/urls.py`: As declarações de URL para este projeto Django; um "sumário" do seu site com tecnologia Django.
- `mysite/asgi.py`: Um ponto de entrada para servidores web compatíveis com ASGI para servir seu projeto.
- `mysite/wsgi.py`: Um ponto de entrada para servidores web compatíveis com WSGI para servir seu projeto.
