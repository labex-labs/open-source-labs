# Configuração do Banco de Dados

Agora, abra `mysite/settings.py`. É um módulo Python normal com variáveis de nível de módulo que representam as configurações do Django.

Por padrão, a configuração usa SQLite. Se você é novo em bancos de dados, ou se está apenas interessado em experimentar o Django, esta é a escolha mais fácil. SQLite está incluído no Python, então você não precisará instalar mais nada para suportar seu banco de dados. Ao iniciar seu primeiro projeto real, no entanto, você pode querer usar um banco de dados mais escalável como PostgreSQL, para evitar dores de cabeça com a troca de banco de dados no futuro.

Se você deseja usar outro banco de dados, instale os `database bindings <database-installation>` apropriados e altere as seguintes chaves no item `'default'` de `DATABASES` para corresponder às configurações de conexão do seu banco de dados:

- `ENGINE <DATABASE-ENGINE>` -- Seja `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'`, ou `'django.db.backends.oracle'`. Outros backends também estão `disponíveis <third-party-notes>`.
- `NAME` -- O nome do seu banco de dados. Se você estiver usando SQLite, o banco de dados será um arquivo no seu computador; nesse caso, `NAME` deve ser o caminho absoluto completo, incluindo o nome do arquivo, desse arquivo. O valor padrão, `BASE_DIR / 'db.sqlite3'`, armazenará o arquivo no diretório do seu projeto.

Se você não estiver usando SQLite como seu banco de dados, configurações adicionais como `USER`, `PASSWORD` e `HOST` devem ser adicionadas. Para mais detalhes, consulte a documentação de referência para `DATABASES`.

> Para bancos de dados diferentes de SQLite

Se você estiver usando um banco de dados além do SQLite, certifique-se de ter criado um banco de dados neste ponto. Faça isso com "`CREATE DATABASE database_name;`" dentro do prompt interativo do seu banco de dados.

Certifique-se também de que o usuário do banco de dados fornecido em `mysite/settings.py` tenha privilégios de "criar banco de dados". Isso permite a criação automática de um `test database <the-test-database>` que será necessário em um tutorial posterior.

Se você estiver usando SQLite, não precisa criar nada antes - o arquivo do banco de dados será criado automaticamente quando for necessário.

Enquanto você estiver editando `mysite/settings.py`, defina `TIME_ZONE` para seu fuso horário.

Além disso, observe a configuração `INSTALLED_APPS` no topo do arquivo. Ela contém os nomes de todos os aplicativos Django que estão ativados nesta instância do Django. Os aplicativos podem ser usados em vários projetos, e você pode empacotá-los e distribuí-los para uso por outros em seus projetos.

Por padrão, `INSTALLED_APPS` contém os seguintes aplicativos, todos os quais vêm com o Django:

- `django.contrib.admin` -- O site de administração. Você o usará em breve.
- `django.contrib.auth` -- Um sistema de autenticação.
- `django.contrib.contenttypes` -- Uma estrutura para tipos de conteúdo.
- `django.contrib.sessions` -- Uma estrutura de sessão.
- `django.contrib.messages` -- Uma estrutura de mensagens.
- `django.contrib.staticfiles` -- Uma estrutura para gerenciar arquivos estáticos.

Esses aplicativos são incluídos por padrão como uma conveniência para o caso comum.

Alguns desses aplicativos usam pelo menos uma tabela de banco de dados, no entanto, então precisamos criar as tabelas no banco de dados antes de podermos usá-los. Para fazer isso, execute o seguinte comando:

```bash
cd ~/project/mysite
python manage.py migrate
```

```plaintext
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

O comando `migrate` olha para a configuração `INSTALLED_APPS` e cria quaisquer tabelas de banco de dados necessárias de acordo com as configurações do banco de dados em seu arquivo `mysite/settings.py` e as migrações do banco de dados fornecidas com o aplicativo (abordaremos isso mais tarde). Você verá uma mensagem para cada migração que ele aplicar. Se você estiver interessado, execute o cliente de linha de comando para seu banco de dados e digite `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite), ou `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle) para exibir as tabelas que o Django criou.

> Para os minimalistas

Como dissemos acima, os aplicativos padrão são incluídos para o caso comum, mas nem todo mundo precisa deles. Se você não precisar de nenhum ou de todos eles, sinta-se à vontade para comentar ou excluir a(s) linha(s) apropriada(s) de `INSTALLED_APPS` antes de executar `migrate`. O comando `migrate` só executará migrações para aplicativos em `INSTALLED_APPS`.
