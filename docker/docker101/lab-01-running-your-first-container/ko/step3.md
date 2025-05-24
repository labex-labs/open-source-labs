# 여러 컨테이너 실행

## Docker Hub 탐색

[Docker Hub](https://hub.docker.com/explore/)는 커뮤니티 및 공식 이미지를 포함하는 Docker 이미지의 공개 중앙 레지스트리입니다.

이미지를 검색할 때 "Docker Certified", "Verified Publisher" 및 "Official Images" 이미지에 대한 필터를 찾을 수 있습니다. "Docker Certified" 필터를 선택하여 엔터프라이즈 준비가 되었으며 Docker Enterprise Edition 제품으로 테스트된 이미지를 찾습니다. 프로덕션 환경에 배포하려는 자체 이미지를 개발할 때는 Docker Store 에서 검증되지 않은 콘텐츠를 사용하지 않는 것이 중요합니다. 이러한 검증되지 않은 이미지는 보안 취약점이나 악성 소프트웨어를 포함할 수 있습니다.

이 랩의 2 단계에서는 Docker Hub 에서 몇 가지 검증된 이미지를 사용하여 nginx 웹 서버와 mongo 데이터베이스의 컨테이너를 몇 개 시작합니다.

## Nginx 서버 실행

Docker Hub 에서 [공식 Nginx 이미지](https://hub.docker.com/_/nginx)를 사용하여 컨테이너를 실행해 보겠습니다.

```bash
docker container run --detach --publish 8080:80 --name nginx nginx
```

여기서는 몇 가지 새로운 플래그를 사용하고 있습니다. `--detach` 플래그는 이 컨테이너를 백그라운드에서 실행합니다. `publish` 플래그는 컨테이너의 포트 80(nginx 의 기본 포트) 을 호스트의 포트 8080 을 통해 게시합니다. NET 네임스페이스는 컨테이너의 프로세스에 자체 네트워크 스택을 제공한다는 점을 기억하십시오. `--publish` 플래그는 컨테이너를 통해 네트워킹을 호스트에 노출할 수 있는 기능입니다.

포트 80 이 nginx 의 기본 포트라는 것을 어떻게 알 수 있습니까? Docker Hub 의 [설명서](https://hub.docker.com/_/nginx)에 나열되어 있기 때문입니다. 일반적으로 검증된 이미지에 대한 설명서는 매우 훌륭하며, 해당 이미지를 사용하여 컨테이너를 실행할 때 참조해야 합니다.

또한 컨테이너의 이름을 지정하는 `--name` 플래그도 지정하고 있습니다. 모든 컨테이너에는 이름이 있으며, 이름을 지정하지 않으면 Docker 가 임의로 이름을 할당합니다. 자체 이름을 지정하면 컨테이너 ID 대신 이름을 참조할 수 있으므로 컨테이너에서 후속 명령을 더 쉽게 실행할 수 있습니다. 예를 들어, `docker container inspect nginx` 대신 `docker container inspect 5e1`입니다.

이것이 nginx 컨테이너를 처음 실행하는 것이므로 Docker Store 에서 nginx 이미지를 다운로드합니다. Nginx 이미지에서 생성된 후속 컨테이너는 호스트에 있는 기존 이미지를 사용합니다.

Nginx 는 경량 웹 서버입니다. LabEx VM 의 **Web 8080** 탭에서 nginx 서버에 액세스할 수 있습니다. 전환하고 페이지를 새로 고쳐 nginx 의 출력을 확인하십시오.

![step 2 nginx](../assets/20230829-11-16-04-BazUogDa.png)

## `mongo` DB 서버 실행

이제 mongoDB 서버를 실행합니다. Docker Hub 에서 [공식 mongoDB 이미지](https://hub.docker.com/_/mongo)를 사용합니다. `latest` 태그 (태그가 지정되지 않은 경우 기본값) 를 사용하는 대신, mongo 이미지의 특정 버전인 4.4 를 사용합니다.

```bash
docker container run --detach --publish 8081:27017 --name mongo mongo:4.4
```

다시 말하지만, 이것이 mongo 컨테이너를 처음 실행하는 것이므로 Docker Store 에서 mongo 이미지를 다운로드합니다. `--publish` 플래그를 사용하여 호스트에서 27017 mongo 포트를 노출합니다. 호스트 매핑에 대해 8080 이 아닌 다른 포트를 사용해야 합니다. 해당 포트는 이미 호스트에서 노출되어 있기 때문입니다. mongo 이미지를 사용하는 방법에 대한 자세한 내용은 Docker Hub 의 [공식 문서](https://hub.docker.com/_/mongo)를 참조하십시오.

웹 브라우저에서 `0.0.0.0:8081`을 사용하여 mongoDB 의 출력을 확인하십시오. MongoDB 에서 경고를 반환하는 메시지가 표시됩니다.

![MongoDB server output warning](../assets/20230829-11-19-23-PkodKK48.png)

`docker container ls`로 실행 중인 컨테이너를 확인합니다.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon ..." Less than a second ago Up 2 seconds 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 17 seconds ago Up 19 seconds 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 5 minutes ago Up 5 minutes priceless_kepler
```

호스트에서 Nginx 웹 서버 컨테이너와 MongoDB 컨테이너가 실행 중인 것을 볼 수 있습니다. 이러한 컨테이너가 서로 통신하도록 구성하지 않았다는 점에 유의하십시오.

컨테이너에 지정한 "nginx" 및 "mongo" 이름과 ubuntu 컨테이너에 대해 생성된 임의 이름 (제 경우에는 "priceless_kepler") 을 볼 수 있습니다. `--publish` 플래그로 지정한 포트 매핑도 볼 수 있습니다. 이러한 실행 중인 컨테이너에 대한 자세한 정보는 `docker container inspect [container id` 명령을 사용할 수 있습니다.

한 가지 눈에 띄는 점은 mongo 컨테이너가 `docker-entrypoint` 명령을 실행하고 있다는 것입니다. 이것은 컨테이너가 시작될 때 실행되는 실행 파일의 이름입니다. mongo 이미지는 DB 프로세스를 시작하기 전에 몇 가지 사전 구성이 필요합니다. [github](https://github.com/docker-library/mongo)에서 스크립트가 정확히 무엇을 하는지 확인할 수 있습니다. 일반적으로 Docker Store 웹사이트의 이미지 설명 페이지에서 github 소스에 대한 링크를 찾을 수 있습니다.

컨테이너는 자체 포함 및 격리되어 있으므로 서로 다른 시스템 또는 런타임 종속성이 있는 컨테이너 간의 잠재적인 충돌을 방지할 수 있습니다. 예를 들어, Java 7 을 사용하는 앱과 Java 8 을 사용하는 다른 앱을 동일한 호스트에 배포합니다. 또는 포트 80 을 기본 수신 포트로 사용하는 여러 nginx 컨테이너를 실행합니다 (호스트에서 `--publish` 플래그를 사용하여 노출하는 경우 호스트에 대해 선택된 포트는 고유해야 합니다). 격리 이점은 Linux 네임스페이스 때문에 가능합니다.

**참고**: 이러한 프로세스를 실행하기 위해 호스트에 (Docker 외에) 아무것도 설치할 필요가 없었습니다! 각 컨테이너에는 컨테이너 내에 필요한 종속성이 포함되어 있으므로 호스트에 직접 아무것도 설치할 필요가 없습니다.

동일한 호스트에서 여러 컨테이너를 실행하면 단일 호스트에서 사용할 수 있는 리소스 (CPU, 메모리 등) 를 최대한 활용할 수 있습니다. 이는 기업에 막대한 비용 절감 효과를 가져올 수 있습니다.

Docker Hub 에서 직접 이미지를 실행하는 것이 때로는 유용할 수 있지만, 사용자 지정 이미지를 만들고 이러한 이미지의 시작점으로 공식 이미지를 참조하는 것이 더 유용합니다. 랩 2 에서 자체 사용자 지정 이미지를 빌드하는 방법을 자세히 살펴보겠습니다.
