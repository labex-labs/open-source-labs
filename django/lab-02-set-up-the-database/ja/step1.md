# データベースのセットアップ

次に、`mysite/settings.py` を開きます。これは通常の Python モジュールで、Django の設定を表すモジュールレベルの変数があります。

デフォルトでは、設定では SQLite が使用されます。データベースに慣れていない場合、または単に Django を試してみたい場合、これは最も簡単な選択肢です。SQLite は Python に含まれているため、データベースをサポートするために他に何もインストールする必要はありません。ただし、最初の本格的なプロジェクトを始める際には、後々のトラブルを避けるために、PostgreSQL のようなより拡張性の高いデータベースを使用することが望ましい場合があります。

別のデータベースを使用する場合は、適切な「データベースバインディング <database-installation>」をインストールし、`DATABASES` の `'default'` 項目の次のキーを変更して、データベース接続設定に合わせます。

- `ENGINE <DATABASE-ENGINE>` -- `'django.db.backends.sqlite3'`、`'django.db.backends.postgresql'`、`'django.db.backends.mysql'`、または `'django.db.backends.oracle'` のいずれか。他のバックエンドも `利用可能です<third-party-notes>`。
- `NAME` -- データベースの名前。SQLite を使用する場合、データベースはコンピュータ上のファイルになります。その場合、`NAME` はそのファイルの完全な絶対パス（ファイル名を含む）にする必要があります。デフォルト値である `BASE_DIR / 'db.sqlite3'` は、ファイルをプロジェクトディレクトリに保存します。

SQLite 以外のデータベースを使用する場合は、`USER`、`PASSWORD`、`HOST` などの追加設定が必要です。詳細については、`DATABASES` のリファレンスドキュメントを参照してください。

> SQLite 以外のデータベースの場合

SQLite 以外のデータベースを使用する場合は、この時点でデータベースを作成していることを確認してください。データベースの対話型プロンプト内で「`CREATE DATABASE database_name;`」を使用して行います。

また、`mysite/settings.py` に記載されているデータベースユーザーが「データベース作成」権限を持っていることも確認してください。これにより、後のチュートリアルで必要になる「テストデータベース <the-test-database>」を自動的に作成できます。

SQLite を使用する場合は、事前に何も作成する必要はありません。データベースファイルは必要になったときに自動的に作成されます。

`mysite/settings.py` を編集している間、`TIME_ZONE` を自分のタイムゾーンに設定してください。

また、ファイルの上部にある `INSTALLED_APPS` 設定にも注目してください。これは、この Django インスタンスでアクティブになっているすべての Django アプリケーションの名前を保持しています。アプリケーションは複数のプロジェクトで使用でき、他の人が彼らのプロジェクトで使用できるようにパッケージ化して配布することができます。

デフォルトでは、`INSTALLED_APPS` には次のアプリケーションが含まれており、すべて Django に付属しています。

- `django.contrib.admin` -- 管理サイト。すぐに使用します。
- `django.contrib.auth` -- 認証システム。
- `django.contrib.contenttypes` -- コンテンツタイプのフレームワーク。
- `django.contrib.sessions` -- セッションフレームワーク。
- `django.contrib.messages` -- メッセージングフレームワーク。
- `django.contrib.staticfiles` -- 静的ファイルを管理するフレームワーク。

これらのアプリケーションは、一般的なケースの利便性のためにデフォルトで含まれています。

ただし、これらのアプリケーションの一部は少なくとも 1 つのデータベーステーブルを使用しているため、使用する前にデータベースにテーブルを作成する必要があります。そのためには、次のコマンドを実行します。

```bash
cd ~/project/mysite
python manage.py migrate
```

```plaintext
実行する操作:
  すべてのマイグレーションを適用する: admin, auth, contenttypes, sessions
マイグレーションの実行:
  contenttypes.0001_initialを適用中... OK
  auth.0001_initialを適用中... OK
  admin.0001_initialを適用中... OK
  admin.0002_logentry_remove_auto_addを適用中... OK
  admin.0003_logentry_add_action_flag_choicesを適用中... OK
  contenttypes.0002_remove_content_type_nameを適用中... OK
  auth.0002_alter_permission_name_max_lengthを適用中... OK
  auth.0003_alter_user_email_max_lengthを適用中... OK
  auth.0004_alter_user_username_optsを適用中... OK
  auth.0005_alter_user_last_login_nullを適用中... OK
  auth.0006_require_contenttypes_0002を適用中... OK
  auth.0007_alter_validators_add_error_messagesを適用中... OK
  auth.0008_alter_user_username_max_lengthを適用中... OK
  auth.0009_alter_user_last_name_max_lengthを適用中... OK
  auth.0010_alter_group_name_max_lengthを適用中... OK
  auth.0011_update_proxy_permissionsを適用中... OK
  auth.0012_alter_user_first_name_max_lengthを適用中... OK
  sessions.0001_initialを適用中... OK
```

`migrate` コマンドは、`INSTALLED_APPS` 設定を見て、`mysite/settings.py` ファイルのデータベース設定とアプリケーションに付属しているデータベースマイグレーション（後で説明します）に基づいて、必要なデータベーステーブルを作成します。適用する各マイグレーションについてメッセージが表示されます。興味がある場合は、データベースのコマンドラインクライアントを実行して、`\dt`（PostgreSQL）、`SHOW TABLES;`（MariaDB、MySQL）、`.tables`（SQLite）、または `SELECT TABLE_NAME FROM USER_TABLES;`（Oracle）を入力して、Django が作成したテーブルを表示してください。

> 最小構成を好む方へ

前述の通り、デフォルトのアプリケーションは一般的なケースのために含まれていますが、必ずしもすべての人が必要とするわけではありません。必要がない場合は、`migrate` を実行する前に、`INSTALLED_APPS` から適切な行をコメントアウトまたは削除しても構いません。`migrate` コマンドは、`INSTALLED_APPS` に含まれるアプリケーションのみにマイグレーションを実行します。
