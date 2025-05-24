# Docker Image 생성 및 빌드

이제 로컬에 파이썬이 설치되어 있지 않다면 어떻게 해야 할까요? 걱정하지 마세요! 필요하지 않으니까요. 컨테이너를 사용하는 것의 장점 중 하나는 호스트 머신에 파이썬이 설치되어 있지 않아도 컨테이너 내에서 파이썬을 빌드할 수 있다는 것입니다.

다음 명령을 실행하여 `Dockerfile`을 생성합니다. (전체 코드 블록을 복사하여 붙여넣기)

```bash
echo 'FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py' > Dockerfile
```

Dockerfile 은 Docker Image 를 빌드하는 데 필요한 지침을 나열합니다. 위의 파일을 줄별로 살펴보겠습니다.

**FROM python:3.8-alpine**
이것은 Dockerfile 의 시작점입니다. 모든 Dockerfile 은 위에 레이어를 구축할 시작 Image 인 `FROM` 라인으로 시작해야 합니다.

이 경우, 애플리케이션을 실행하는 데 필요한 파이썬과 pip 버전이 이미 포함되어 있으므로 `python:3.8-alpine` 기본 레이어를 선택합니다 ( [Dockerfile for python3.8/alpine3.12](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile) 참조).

`alpine` 버전은 [Alpine Linux](https://en.wikipedia.org/wiki/Alpine_Linux) 배포판을 사용한다는 의미입니다. 이는 다른 많은 Linux 버전보다 훨씬 작으며, 크기가 약 8MB 이고, 디스크에 최소 설치 시 약 130MB 정도입니다. Image 가 작을수록 다운로드 (배포) 속도가 훨씬 빠르며, 공격 표면이 작기 때문에 보안 측면에서도 장점이 있습니다. [Alpine Linux](https://alpinelinux.org/downloads/)는 musl 과 BusyBox 를 기반으로 하는 Linux 배포판입니다.

여기서는 파이썬 Image 에 "3.8-alpine" 태그를 사용하고 있습니다. [Docker Hub](https://hub.docker.com/_/python/)에서 공식 파이썬 Image 에 사용 가능한 태그를 살펴보십시오. 상위 Image 의 변경 사항을 제어하기 위해 상위 Image 를 상속할 때는 특정 태그를 사용하는 것이 가장 좋습니다. 태그가 지정되지 않으면 "latest" 태그가 적용되며, 이는 Image 의 최신 버전을 가리키는 동적 포인터 역할을 합니다.

보안상의 이유로, Docker Image 를 구축하는 레이어를 이해하는 것이 매우 중요합니다. 따라서 [docker hub](https://hub.docker.com/)에서 찾을 수 있는 "공식" Image 또는 docker-store 에서 찾을 수 있는 비 커뮤니티 Image 만 사용하는 것이 좋습니다. 이러한 Image 는 특정 보안 요구 사항을 충족하도록 [검증](https://docs.docker.com/docker-hub/official_repos/)되었으며, 사용자가 따를 수 있는 매우 훌륭한 문서를 갖추고 있습니다. 이 [파이썬 기본 Image](https://hub.docker.com/_/python) 및 사용할 수 있는 다른 모든 Image 에 대한 자세한 정보는 [docker hub](https://hub.docker.com)에서 확인할 수 있습니다.

더 복잡한 애플리케이션의 경우, 체인 상위에 있는 `FROM` Image 를 사용해야 할 수 있습니다. 예를 들어, 파이썬 앱의 상위 [Dockerfile](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)은 `FROM alpine`으로 시작한 다음 Image 에 대한 일련의 `CMD` 및 `RUN` 명령을 지정합니다. 더 세밀한 제어가 필요한 경우, `FROM alpine`(또는 다른 배포판) 으로 시작하여 해당 단계를 직접 실행할 수 있습니다. 하지만 처음 시작할 때는 요구 사항에 가장 잘 맞는 공식 Image 를 사용하는 것이 좋습니다.

**RUN pip install flask**
`RUN` 명령은 패키지 설치, 파일 편집 또는 파일 권한 변경과 같이 애플리케이션에 대한 Image 를 설정하는 데 필요한 명령을 실행합니다. 이 경우 flask 를 설치하고 있습니다. `RUN` 명령은 빌드 시 실행되며 Image 의 레이어에 추가됩니다.

**CMD ["python","app.py"]**
`CMD`는 컨테이너를 시작할 때 실행되는 명령입니다. 여기서는 `CMD`를 사용하여 파이썬 앱을 실행하고 있습니다.

Dockerfile 당 하나의 `CMD`만 있을 수 있습니다. 둘 이상의 `CMD`를 지정하면 마지막 `CMD`가 적용됩니다. 상위 python:3.8-alpine 도 `CMD`(`CMD python3`) 를 지정합니다. 공식 python:alpine Image 에 대한 Dockerfile 은 [여기](https://github.com/docker-library/python/blob/9ff5f04241c7bcb224303ff8cea9434e9976f8af/3.8/alpine3.12/Dockerfile)에서 확인할 수 있습니다.

호스트에 파이썬을 설치하지 않고도 공식 파이썬 Image 를 직접 사용하여 파이썬 스크립트를 실행할 수 있습니다. 하지만 오늘은 애플리케이션을 포함하는 사용자 정의 Image 를 생성하여 애플리케이션으로 Image 를 빌드하고 다른 환경으로 배포할 수 있도록 합니다.

**COPY app.py /app.py**
이것은 로컬 디렉토리 (여기서 `docker image build`를 실행합니다) 의 app.py 를 Image 의 새 레이어로 복사합니다. 이 지침은 Dockerfile 의 마지막 줄입니다. 소스 코드를 Image 로 복사하는 등 자주 변경되는 레이어는 Docker 레이어 캐시를 최대한 활용하기 위해 파일 하단에 배치해야 합니다. 이렇게 하면 그렇지 않으면 캐시될 수 있는 레이어를 다시 빌드하지 않아도 됩니다. 예를 들어, `FROM` 지침에 변경 사항이 있으면 이 Image 의 모든 후속 레이어에 대한 캐시가 무효화됩니다. 이 랩의 뒷부분에서 이를 시연할 것입니다.

`CMD ["python","app.py"]` 라인 뒤에 배치하는 것은 직관적이지 않을 수 있습니다. `CMD` 라인은 컨테이너가 시작될 때만 실행되므로 여기서는 `file not found` 오류가 발생하지 않습니다.

자, 아주 간단한 Dockerfile 이 완성되었습니다. Dockerfile 에 넣을 수 있는 전체 명령 목록은 [여기](https://docs.docker.com/engine/reference/builder/)에서 확인할 수 있습니다. 이제 Dockerfile 을 정의했으므로 이를 사용하여 사용자 정의 Docker Image 를 빌드해 보겠습니다.

Docker Image 를 빌드합니다.

`-t`를 전달하여 Image 의 이름을 `python-hello-world`로 지정합니다.

```bash
docker image build -t python-hello-world .
```

Image 목록에 Image 가 표시되는지 확인합니다.

```bash
docker image ls
```

**참고** 기본 Image `python:3.8-alpine`도 목록에 있습니다.

history 명령을 실행하여 Image 및 해당 레이어의 기록을 표시할 수 있습니다.

```bash
docker history python-hello-world
docker history python:3.8-alpine
```
