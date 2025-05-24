# Apresentando o Django Admin

Gerar sites de administração para sua equipe ou clientes adicionarem, alterarem e excluírem conteúdo é um trabalho tedioso que não requer muita criatividade. Por essa razão, o Django automatiza totalmente a criação de interfaces de administração para modelos.

O Django foi escrito em um ambiente de redação, com uma separação muito clara entre "editores de conteúdo" e o site "público". Os gerentes de site usam o sistema para adicionar notícias, eventos, placares esportivos, etc., e esse conteúdo é exibido no site público. O Django resolve o problema de criar uma interface unificada para os administradores do site editarem o conteúdo.

O admin não se destina a ser usado pelos visitantes do site. É para gerentes de site.

## Criando um usuário administrador

Primeiro, precisaremos criar um usuário que possa fazer login no site de administração. Execute o seguinte comando:

```bash
python manage.py createsuperuser
```

Digite o nome de usuário desejado e pressione Enter.

```plaintext
Username: admin
```

Você será solicitado a inserir o endereço de e-mail desejado:

```plaintext
Email address: admin@example.com
```

A etapa final é inserir sua senha. Você será solicitado a inserir sua senha duas vezes, a segunda vez como uma confirmação da primeira.

```plaintext
Password: 12345678
Password (again): 12345678

This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## Inicie o servidor de desenvolvimento

O site de administração do Django é ativado por padrão. Vamos iniciar o servidor de desenvolvimento e explorá-lo.

Se o servidor não estiver em execução, inicie-o assim:

```bash
python manage.py runserver
```

Agora, abra um navegador da web na guia **VNC** e vá para "/admin/" em seu domínio local -- por exemplo, `http://127.0.0.1:8000/admin/`. Você deve ver a tela de login do admin:

![Django admin login screen](../assets/20230907-14-31-50-SvkJF8K8.png)

Como a `tradução </topics/i18n/translation>` está ativada por padrão, se você definir `LANGUAGE_CODE`, a tela de login será exibida no idioma fornecido (se o Django tiver as traduções apropriadas).

## Entre no site de administração

Agora, tente fazer login com a conta de superusuário que você criou na etapa anterior. Você deve ver a página de índice do Django admin:

![Django admin index page](../assets/admin02.png)

Você deve ver alguns tipos de conteúdo editável: grupos e usuários. Eles são fornecidos por `django.contrib.auth`, a estrutura de autenticação fornecida pelo Django.

## Torne o aplicativo de pesquisa modificável no admin

Mas onde está nosso aplicativo de pesquisa? Ele não é exibido na página de índice do admin.

Só falta mais uma coisa: precisamos dizer ao admin que os objetos `Question` têm uma interface de administração. Para fazer isso, abra o arquivo `polls/admin.py` e edite-o para que fique assim:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

## Explore a funcionalidade de administração gratuita

Agora que registramos `Question`, o Django sabe que ele deve ser exibido na página de índice do admin:

![Django admin index page, now with polls displayed](../assets/admin03t.png)

Clique em "Questions". Agora você está na página "change list" (lista de alterações) para perguntas. Esta página exibe todas as perguntas no banco de dados e permite que você escolha uma para alterá-la. Existe a pergunta "What's up?" que criamos anteriormente:

![Polls change list page](../assets/admin04t.png)

Clique na pergunta "What's up?" para editá-la:

![Editing a poll question](../assets/20230907-14-33-49-XWeEgAXl.png)

Coisas a serem observadas aqui:

- O formulário é gerado automaticamente a partir do modelo `Question`.
- Os diferentes tipos de campo do modelo (`~django.db.models.DateTimeField`, `~django.db.models.CharField`) correspondem ao widget de entrada HTML apropriado. Cada tipo de campo sabe como se exibir no Django admin.
- Cada `~django.db.models.DateTimeField` recebe atalhos JavaScript gratuitos. As datas recebem um atalho "Today" (Hoje) e um popup de calendário, e os horários recebem um atalho "Now" (Agora) e um popup conveniente que lista os horários comumente inseridos.

A parte inferior da página oferece algumas opções:

- Save (Salvar) -- Salva as alterações e retorna à página de lista de alterações para este tipo de objeto.
- Save and continue editing (Salvar e continuar editando) -- Salva as alterações e recarrega a página de administração para este objeto.
- Save and add another (Salvar e adicionar outro) -- Salva as alterações e carrega um novo formulário em branco para este tipo de objeto.
- Delete (Excluir) -- Exibe uma página de confirmação de exclusão.

Se o valor de "Date published" (Data de publicação) não corresponder ao horário em que você criou a pergunta em **Criação de um aplicativo de pesquisa básico**, provavelmente significa que você esqueceu de definir o valor correto para a configuração `TIME_ZONE`. Altere-o, recarregue a página e verifique se o valor correto aparece.

Altere a "Date published" (Data de publicação) clicando nos atalhos "Today" (Hoje) e "Now" (Agora). Em seguida, clique em "Save and continue editing" (Salvar e continuar editando). Em seguida, clique em "History" (Histórico) no canto superior direito. Você verá uma página listando todas as alterações feitas neste objeto via Django admin, com o carimbo de data/hora e o nome de usuário da pessoa que fez a alteração:

![History page for question object](../assets/admin06t.png)

Quando você estiver confortável com a API de modelos e se familiarizou com o site de administração, leia **Criando as visualizações da interface pública** para aprender como adicionar mais visualizações ao nosso aplicativo de pesquisa.
