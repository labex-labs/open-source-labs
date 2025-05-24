# 첫 번째 컨테이너 실행

Docker CLI 를 사용하여 첫 번째 컨테이너를 실행합니다.

LabEx VM 에서 터미널을 엽니다.

명령을 실행합니다.

```bash
docker container run -t ubuntu top
```

`docker container run` 명령을 사용하여 `top` 명령을 사용하는 `ubuntu` 이미지로 컨테이너를 실행합니다. `-t` 플래그는 `top`이 올바르게 작동하는 데 필요한 가상 TTY 를 할당합니다.

```bash
$ docker container run -it ubuntu top
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
aafe6b5e13de: Pull complete
0a2b43a72660: Pull complete
18bdd1e546d2: Pull complete
8198342c3e05: Pull complete
f56970a44fd4: Pull complete
Digest: sha256:f3a61450ae43896c4332bda5e78b453f4a93179045f20c8181043b26b5e79028
Status: Downloaded newer image for ubuntu:latest
```

`docker run` 명령은 먼저 `docker pull`을 실행하여 ubuntu 이미지를 호스트에 다운로드합니다. 다운로드가 완료되면 컨테이너를 시작합니다. 실행 중인 컨테이너의 출력은 다음과 같습니다.

```bash
top - 20:32:46 up 3 days, 17:40,  0 users,  load average: 0.00, 0.01, 0.00
Tasks:   1 total,   1 running,   0 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2046768 total,   173308 free,   117248 used,  1756212 buff/cache
KiB Swap:  1048572 total,  1048572 free,        0 used.  1548356 avail Mem

PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
      1 root      20   0   36636   3072   2640 R   0.3  0.2   0:00.04 top
```

`top`은 시스템의 프로세스를 출력하고 리소스 소비량별로 정렬하는 리눅스 유틸리티입니다. 이 출력에는 단일 프로세스만 있습니다. 즉, `top` 프로세스 자체입니다. PID 네임스페이스 격리 때문에 이 목록에서 호스트의 다른 프로세스는 보이지 않습니다.

컨테이너는 리눅스 네임스페이스를 사용하여 다른 컨테이너 또는 호스트로부터 시스템 리소스를 격리합니다. PID 네임스페이스는 프로세스 ID 에 대한 격리를 제공합니다. 컨테이너 내에서 `top`을 실행하면 컨테이너의 PID 네임스페이스 내의 프로세스가 표시됩니다. 이는 호스트에서 `top`을 실행할 때 볼 수 있는 것과 매우 다릅니다.

`ubuntu` 이미지를 사용하고 있지만, 컨테이너 자체에는 자체 커널이 없다는 점에 유의하는 것이 중요합니다. 호스트의 커널을 사용하며, `ubuntu` 이미지는 ubuntu 시스템에서 사용할 수 있는 파일 시스템과 도구를 제공하는 데만 사용됩니다.

`docker container exec`로 컨테이너 검사

`docker container exec` 명령은 새 프로세스로 실행 중인 컨테이너의 네임스페이스에 "진입"하는 방법입니다.

새 터미널을 엽니다. `Terminal` > `New Terminal`을 선택합니다.

새 터미널에서 `docker container ls` 명령을 사용하여 방금 생성한 실행 중인 컨테이너의 ID 를 가져옵니다.

```bash
$ docker container ls
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
b3ad2a23fab3 ubuntu "top" 29 minutes ago Up 29 minutes goofy_nobel
```

그런 다음 해당 ID 를 사용하여 `docker container exec` 명령을 사용하여 해당 컨테이너 내에서 `bash`를 실행합니다. bash 를 사용하고 터미널에서 이 컨테이너와 상호 작용하려는 경우, 대화형 모드를 사용하여 실행하는 동시에 가상 터미널을 할당하기 위해 `-it` 플래그를 사용합니다.

```bash
$ docker container exec -it ID < CONTAINER > bash
root@b3ad2a23fab3:/#
```

그리고 짜잔! 방금 `docker container exec` 명령을 사용하여 `bash` 프로세스로 컨테이너의 네임스페이스에 "진입"했습니다. `bash`와 함께 `docker container exec`를 사용하는 것은 Docker 컨테이너를 검사하는 일반적인 패턴입니다.

터미널의 접두사가 변경된 것을 확인하십시오. 예를 들어, `root@b3ad2a23fab3:/`. 이는 컨테이너 "내부"에서 bash 를 실행하고 있음을 나타냅니다.

**참고**: 이는 별도의 호스트 또는 VM 에 ssh 로 접속하는 것과 동일하지 않습니다. bash 프로세스와 연결하기 위해 ssh 서버가 필요하지 않습니다. 컨테이너는 커널 수준 기능을 사용하여 격리를 달성하고 컨테이너는 커널 위에서 실행된다는 점을 기억하십시오. 컨테이너는 동일한 호스트에서 격리되어 실행되는 프로세스 그룹일 뿐이며, `docker container exec`를 사용하여 `bash` 프로세스로 해당 격리에 진입할 수 있습니다. `docker container exec`를 실행한 후 격리되어 실행되는 프로세스 그룹 (즉, 컨테이너) 에는 `top` 및 `bash`가 포함됩니다.

동일한 터미널에서 `ps -ef`를 실행하여 실행 중인 프로세스를 검사합니다.

```bash
root@b3ad2a23fab3:/# ps -ef
UID PID PPID C STIME TTY TIME CMD
root 1 0 0 20:34 ? 00:00:00 top
root 17 0 0 21:06 ? 00:00:00 bash
root 27 17 0 21:14 ? 00:00:00 ps -ef
```

`top` 프로세스, `bash` 프로세스 및 `ps` 프로세스만 표시됩니다.

비교를 위해 컨테이너를 종료하고 호스트에서 `ps -ef` 또는 `top`을 실행합니다. 이러한 명령은 리눅스 또는 Mac 에서 작동합니다. Windows 의 경우 `tasklist`를 사용하여 실행 중인 프로세스를 검사할 수 있습니다.

```bash
root@b3ad2a23fab3:/# exit
exit
$ ps -ef
# Lots of processes!
```

_기술 심층 분석_
PID 는 컨테이너에 시스템 리소스에 대한 격리를 제공하는 리눅스 네임스페이스 중 하나일 뿐입니다. 다른 리눅스 네임스페이스는 다음과 같습니다.

- MNT - 다른 네임스페이스에 영향을 주지 않고 디렉토리를 마운트 및 마운트 해제
- NET - 컨테이너에는 자체 네트워크 스택이 있습니다.
- IPC - 메시지 큐와 같은 격리된 프로세스 간 통신 메커니즘.
- User - 시스템의 사용자 격리된 보기
- UTC - 컨테이너별로 호스트 이름 및 도메인 이름 설정

이러한 네임스페이스는 함께 컨테이너가 동일한 시스템에서 실행되는 다른 컨테이너와 안전하게 충돌 없이 함께 실행될 수 있도록 컨테이너에 대한 격리를 제공합니다. 다음으로, 컨테이너의 다양한 용도를 보여주고 동일한 호스트에서 여러 컨테이너를 실행할 때 격리의 이점을 보여줍니다.

**참고**: 네임스페이스는 **리눅스** 커널의 기능입니다. 그러나 Docker 를 사용하면 Windows 및 Mac 에서 컨테이너를 실행할 수 있습니다... 어떻게 작동합니까? 비결은 Docker 제품 또는 Docker 엔진에 내장된 리눅스 서브시스템입니다. Docker 는 이 리눅스 서브시스템을 새로운 프로젝트인 [LinuxKit](https://github.com/linuxkit/linuxkit)에 오픈 소스로 제공했습니다. 여러 다른 플랫폼에서 컨테이너를 실행할 수 있다는 것은 컨테이너와 함께 Docker 도구를 사용하는 것의 장점 중 하나입니다.

리눅스 서브시스템을 사용하여 Windows 에서 리눅스 컨테이너를 실행하는 것 외에도, Windows OS 에서 컨테이너 기본 요소가 생성되어 네이티브 Windows 컨테이너가 이제 가능합니다. 네이티브 Windows 컨테이너는 Windows 10 또는 Windows Server 2016 이상에서 실행할 수 있습니다.

**참고**: 컨테이너화된 터미널에서 이 연습을 실행하고 터미널에서 `ps -ef` 명령을 실행하면 `exec` 명령을 종료한 후에도 제한된 프로세스 집합이 표시됩니다. 로컬 머신의 터미널에서 `ps -ef` 명령을 실행하여 모든 프로세스를 볼 수 있습니다.

`<ctrl>-c`를 입력하여 `top` 프로세스를 실행하는 컨테이너를 정리하고, 모든 컨테이너를 나열하고 ID 별로 컨테이너를 제거합니다.

```bash
docker ps -a

docker rm <CONTAINER ID>
```
