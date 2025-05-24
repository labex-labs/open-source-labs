# 애플리케이션 실행

애플리케이션이 설정 및 구성되었으므로 `flask` 명령을 사용하여 실행할 수 있습니다. 이 명령은 `flaskr` 패키지가 아닌 최상위 디렉토리에서 실행해야 합니다.

```bash
flask --app flaskr run --debug --host=0.0.0.0
```

다음과 유사한 출력을 볼 수 있습니다.

```bash
 * Serving Flask app "flaskr"
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: nnn-nnn-nnn
```

그런 다음 **Web 5000** 탭을 열면 다음을 볼 수 있습니다.

![Flask app hello world page](../assets/hello-world.png)
