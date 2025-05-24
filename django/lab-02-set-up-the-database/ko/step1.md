# 데이터베이스 설정

이제 `mysite/settings.py`를 열어보세요. Django 설정을 나타내는 모듈 수준 변수를 가진 일반적인 Python 모듈입니다.

기본적으로, 설정은 SQLite 를 사용합니다. 데이터베이스를 처음 접하거나 Django 를 사용해보고 싶다면, 이것이 가장 쉬운 선택입니다. SQLite 는 Python 에 포함되어 있으므로, 데이터베이스를 지원하기 위해 다른 것을 설치할 필요가 없습니다. 하지만 첫 번째 실제 프로젝트를 시작할 때는, 나중에 데이터베이스 전환으로 인한 문제를 피하기 위해 PostgreSQL 과 같은 더 확장 가능한 데이터베이스를 사용하는 것이 좋습니다.

다른 데이터베이스를 사용하려면, 적절한 `데이터베이스 바인딩 (database bindings)`을 설치하고 `DATABASES`의 `'default'` 항목에서 다음 키를 데이터베이스 연결 설정에 맞게 변경하십시오.

- `ENGINE <DATABASE-ENGINE>` -- `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'`, 또는 `'django.db.backends.oracle'` 중 하나입니다. 다른 백엔드도 `사용 가능합니다 <third-party-notes>`.
- `NAME` -- 데이터베이스의 이름입니다. SQLite 를 사용하는 경우, 데이터베이스는 컴퓨터의 파일이 됩니다. 이 경우, `NAME`은 해당 파일의 전체 절대 경로 (파일 이름 포함) 여야 합니다. 기본값인 `BASE_DIR / 'db.sqlite3'`은 프로젝트 디렉토리에 파일을 저장합니다.

SQLite 를 데이터베이스로 사용하지 않는 경우, `USER`, `PASSWORD`, `HOST`와 같은 추가 설정을 추가해야 합니다. 자세한 내용은 `DATABASES`에 대한 참조 문서를 참조하십시오.

> SQLite 이외의 데이터베이스의 경우

SQLite 이외의 데이터베이스를 사용하는 경우, 이 시점에서 데이터베이스를 생성했는지 확인하십시오. 데이터베이스의 대화형 프롬프트 내에서 "`CREATE DATABASE database_name;`"을 사용하여 수행하십시오.

또한 `mysite/settings.py`에 제공된 데이터베이스 사용자가 "create database" 권한을 가지고 있는지 확인하십시오. 이렇게 하면 나중에 튜토리얼에서 필요하게 될 `테스트 데이터베이스 <the-test-database>`를 자동으로 생성할 수 있습니다.

SQLite 를 사용하는 경우, 미리 아무것도 생성할 필요가 없습니다. 데이터베이스 파일은 필요할 때 자동으로 생성됩니다.

`mysite/settings.py`를 편집하는 동안, `TIME_ZONE`을 사용자의 시간대로 설정하십시오.

또한 파일 상단의 `INSTALLED_APPS` 설정을 확인하십시오. 이 설정은 이 Django 인스턴스에서 활성화된 모든 Django 애플리케이션의 이름을 포함합니다. 앱은 여러 프로젝트에서 사용될 수 있으며, 다른 사용자가 자신의 프로젝트에서 사용할 수 있도록 패키징하고 배포할 수 있습니다.

기본적으로, `INSTALLED_APPS`에는 Django 와 함께 제공되는 다음 앱이 포함되어 있습니다.

- `django.contrib.admin` -- 관리자 사이트입니다. 곧 사용하게 됩니다.
- `django.contrib.auth` -- 인증 시스템입니다.
- `django.contrib.contenttypes` -- 콘텐츠 유형을 위한 프레임워크입니다.
- `django.contrib.sessions` -- 세션 프레임워크입니다.
- `django.contrib.messages` -- 메시징 프레임워크입니다.
- `django.contrib.staticfiles` -- 정적 파일을 관리하기 위한 프레임워크입니다.

이러한 애플리케이션은 일반적인 경우를 위해 기본적으로 포함되어 있습니다.

이러한 애플리케이션 중 일부는 적어도 하나의 데이터베이스 테이블을 사용하므로, 사용하기 전에 데이터베이스에 테이블을 생성해야 합니다. 이를 위해 다음 명령을 실행하십시오.

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

`migrate` 명령은 `INSTALLED_APPS` 설정을 확인하고, `mysite/settings.py` 파일의 데이터베이스 설정 및 앱과 함께 제공되는 데이터베이스 마이그레이션에 따라 필요한 데이터베이스 테이블을 생성합니다 (나중에 다룰 것입니다). 적용되는 각 마이그레이션에 대한 메시지가 표시됩니다. 관심이 있다면, 데이터베이스의 명령줄 클라이언트를 실행하고 `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite), 또는 `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle) 을 입력하여 Django 가 생성한 테이블을 표시하십시오.

> 미니멀리스트를 위한 팁

위에서 언급했듯이, 기본 애플리케이션은 일반적인 경우를 위해 포함되어 있지만, 모든 사람이 필요로 하는 것은 아닙니다. 필요하지 않은 앱이 있거나 모두 필요하지 않은 경우, `migrate`를 실행하기 전에 `INSTALLED_APPS`에서 해당 줄을 주석 처리하거나 삭제하십시오. `migrate` 명령은 `INSTALLED_APPS`에 있는 앱에 대해서만 마이그레이션을 실행합니다.
