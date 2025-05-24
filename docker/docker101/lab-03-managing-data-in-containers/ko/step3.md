# [선택 사항] OverlayFS

OverlayFS 는 Linux 용 `union mount filesystem` 구현입니다. Docker 볼륨이 무엇인지 이해하려면 Docker 에서 레이어와 파일 시스템이 어떻게 작동하는지 이해하는 것이 도움이 됩니다.

컨테이너를 시작하기 위해 Docker 는 읽기 전용 이미지를 가져와 그 위에 새로운 읽기 - 쓰기 레이어를 생성합니다. 레이어를 하나로 보려면 Docker 는 Union File System 또는 OverlayFS(Overlay File System), 특히 `overlay2` 스토리지 드라이버를 사용합니다.

Docker 호스트 관리 파일을 보려면 Docker 프로세스 파일 시스템에 액세스해야 합니다. `--privileged` 및 `--pid=host` 플래그를 사용하면 `busybox`와 같은 컨테이너 내부에서 호스트의 프로세스 ID 네임스페이스에 액세스할 수 있습니다. 그런 다음 Docker 의 `/var/lib/docker/overlay2` 디렉토리로 이동하여 Docker 에서 관리하는 다운로드된 레이어를 볼 수 있습니다.

Docker 에서 현재 레이어 목록을 보려면,

```bash
$ docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh

/ # ls -l /var/lib/docker/overlay2
total 16
drwx------ 3 root root 4096 Sep 25 19:44 0e55ecaa4d17c353191e68022d9a17fde64fb5e9217b07b5c56eb4c74dad5b32
drwx------ 5 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d
drwx------ 4 root root 4096 Sep 25 19:44 187854d05ccd18980642e820b0d2be6a127ba85d8ed96315bb5ae37eb1add36d-init
drwx------ 2 root root 4096 Sep 25 19:44 l

/ # exit
```

`ubuntu` 이미지를 다운로드하고 다시 확인합니다.

```bash
docker pull ubuntu
docker run -it --privileged --pid=host busybox nsenter -t 1 -m -u -n -i sh
```

레이어 목록을 다시 보려면 명령을 입력합니다.

```
ls -l /var/lib/docker/overlay2/ & exit
```

`ubuntu` 이미지를 다운로드하면 암묵적으로 4 개의 새로운 레이어가 다운로드된 것을 볼 수 있습니다.

- a611792b4cac502995fa88a888261dfba0b5d852e72f9db9e075050991423779
- d181f1a41fc35a45c16e8bfcb8eee6f768f3b98f82210a43ea65f284a45fcd65
- dac2f37f6280a076836d39b87b0ae5ebf5c0d386b6d8b991b103aadbcebaa7c6
- f3e921b440c37c86d06cd9c9fb70df50edad553c36cc87f84d5eeba734aae709

본질적으로 `overlay2` 스토리지 드라이버는 호스트의 서로 다른 디렉토리를 계층화하고 단일 디렉토리로 표시합니다.

- base layer 또는 lowerdir,
- `diff` layer 또는 upperdir,
- overlay layer (사용자 보기), 그리고
- `work` dir.

OverlayFS 는 하위 디렉토리를 기본 이미지와 다운로드된 읽기 전용 (R/O) 레이어가 포함된 `lowerdir`로 참조합니다.

상위 디렉토리는 `upperdir`이라고 하며 읽기 - 쓰기 (R/W) 컨테이너 레이어입니다.

통합 보기 또는 `overlay` 레이어는 `merged`라고 합니다.

마지막으로, `workdir`은 오버레이에서 내부적으로 사용되는 빈 디렉토리입니다.

`overlay2` 드라이버는 최대 128 개의 하위 OverlayFS 레이어를 지원합니다. `l` 디렉토리에는 단축된 레이어 식별자가 심볼릭 링크로 포함되어 있습니다.

![Overlay2 Storage Driver](../assets/overlay2-driver.png)

정리,

```bash
docker system prune -a
clear
```
