# 정리

이 랩을 완료하면 호스트에 많은 수의 실행 중인 컨테이너가 생성됩니다. 이를 정리해 보겠습니다.

실행 중인 각 컨테이너에 대해 `docker container stop [container id]`를 실행합니다.

먼저 `docker container ls`를 사용하여 실행 중인 컨테이너 목록을 가져옵니다.

```bash
$ docker container ls
```

그런 다음 목록의 각 컨테이너에 대해 명령을 실행합니다.

```bash
$ docker container stop <container_id>
```

중지된 컨테이너 제거

`docker system prune`은 시스템을 정리하는 데 매우 유용한 명령입니다. 중지된 모든 컨테이너, 사용하지 않는 볼륨 및 네트워크, 그리고 댕글링 (dangling) Image 를 제거합니다.

```bash
$ docker system prune
WARNING! This will remove:
- all stopped containers
- all volumes not used by at least one container
- all networks not used by at least one container
- all dangling images
Are you sure you want to continue? [y/N] y
Deleted Containers:
0b2ba61df37fb4038d9ae5d145740c63c2c211ae2729fc27dc01b82b5aaafa26

Total reclaimed space: 300.3kB
```
