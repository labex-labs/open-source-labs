# 정리

이 랩을 완료하면 호스트에서 많은 컨테이너가 실행됩니다. 이를 정리해 보겠습니다.

먼저 `docker container ls`를 사용하여 실행 중인 컨테이너 목록을 가져옵니다.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
d6777df89fea nginx "nginx -g 'daemon ..." 3 minutes ago Up 3 minutes 0.0.0.0:8080- nginx > 80/tcp
ead80a0db505 mongo "docker-entrypoint..." 3 minutes ago Up 3 minutes 0.0.0.0:8081- mongo > 27017/tcp
af549dccd5cf ubuntu "top" 8 minutes ago Up 8 minutes priceless_kepler
```

다음으로, 목록의 각 컨테이너에 대해 `docker container stop [container id]`를 실행합니다. 이전에 지정한 컨테이너 이름을 사용할 수도 있습니다.

```bash
$ docker container stop d67 ead af5
d67
ead
af5
```

**참고**: ID 의 고유성을 위해 충분한 자릿수만 참조하면 됩니다. 세 자릿수면 거의 항상 충분합니다.

중지된 컨테이너 제거

`docker system prune`은 시스템을 정리하는 데 매우 유용한 명령입니다. 중지된 모든 컨테이너, 사용하지 않는 볼륨 및 네트워크, 그리고 댕글링 이미지를 제거합니다.

```bash
$ docker system prune
WARNING! This will remove:
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
7872fd96ea4695795c41150a06067d605f69702dbcb9ce49492c9029f0e1b44b
60abd5ee65b1e2732ddc02b971a86e22de1c1c446dab165462a08b037ef7835c
31617fdd8e5f584c51ce182757e24a1c9620257027665c20be75aa3ab6591740

Total reclaimed space: 12B
```
