# 주소 이미 사용 중

서버를 시작하려고 할 때 "Address already in use" 메시지와 함께 `OSError`가 표시되면, 이는 다른 프로그램이 이미 개발 서버의 기본 포트인 포트 5000 을 사용하고 있음을 의미합니다. 다른 프로그램을 식별하고 중지하거나 다른 포트를 선택할 수 있습니다.

포트 5000 을 사용하는 프로세스를 식별하려면 `netstat` 또는 `lsof` 명령을 사용할 수 있습니다. 다음은 Linux, macOS 및 Windows 의 예입니다.

- Linux:

```bash
netstat -nlp | grep 5000
```

- macOS / Linux:

```bash
lsof -P -i :5000
```

- Windows:

```bash
-ano > netstat | findstr 5000
```

프로세스를 식별한 후에는 다른 운영 체제 도구를 사용하여 해당 프로세스를 중지할 수 있습니다. 프로세스를 중지한 후에는 문제 없이 개발 서버를 실행할 수 있습니다.
