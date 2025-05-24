# Docker Image 실행

이제 Image 를 빌드했으므로 실행하여 작동하는지 확인할 수 있습니다.

Docker Image 실행

```bash
docker run -p 5001:5000 -d python-hello-world
```

`-p` 플래그는 컨테이너 내에서 실행되는 포트를 호스트에 매핑합니다. 이 경우, 컨테이너 내부의 포트 5000 에서 실행되는 파이썬 앱을 호스트의 포트 5001 에 매핑하고 있습니다. 호스트의 다른 애플리케이션에서 포트 5001 을 이미 사용하고 있는 경우 5001 을 5002 와 같은 다른 값으로 바꿔야 할 수 있습니다.

터미널 창에서 **PORTS** 탭으로 이동하여 링크를 클릭하여 새 브라우저 탭에서 앱을 엽니다.

![Terminal ports tab link](../assets/20230829-13-59-19-e8dZe3aN.png)

터미널에서 `curl localhost:5001`을 실행하면 `hello world!`가 반환됩니다.

컨테이너의 로그 출력을 확인합니다.

애플리케이션의 로그를 보려면 `docker container logs` 명령을 사용할 수 있습니다. 기본적으로 `docker container logs`는 애플리케이션에서 표준 출력으로 전송된 내용을 출력합니다. 실행 중인 컨테이너의 ID 를 찾으려면 `docker container ls`를 사용하십시오.

```bash
labex:project/ $ docker container ls
CONTAINER ID   IMAGE                COMMAND           CREATED         STATUS         PORTS                                       NAMES
52df977e5541   python-hello-world   "python app.py"   2 minutes ago   Up 2 minutes   0.0.0.0:5001->5000/tcp, :::5001->5000/tcp   heuristic_lamport
labex:project/ $ docker container logs 52df977e5541
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET / HTTP/1.1" 200 -
172.17.0.1 - - [23/Jan/2024 02:43:10] "GET /favicon.ico HTTP/1.1" 404 -
```

Dockerfile 은 애플리케이션에 대한 재현 가능한 빌드를 생성하는 방법입니다. 일반적인 워크플로우는 CI/CD 자동화가 빌드 프로세스의 일부로 `docker image build`를 실행하도록 하는 것입니다. Image 가 빌드되면 중앙 레지스트리로 전송되어 해당 애플리케이션의 인스턴스를 실행해야 하는 모든 환경 (예: 테스트 환경) 에서 액세스할 수 있습니다. 다음 단계에서는 사용자 정의 Image 를 공개 Docker 레지스트리인 Docker Hub 에 푸시하여 다른 개발자 및 운영자가 사용할 수 있도록 합니다.
