# Image 레이어 이해

Docker 의 주요 설계 속성 중 하나는 유니온 파일 시스템 (union file system) 을 사용하는 것입니다.

이전에 생성한 `Dockerfile`을 생각해 보겠습니다.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app.py"]
COPY app.py /app.py
```

이러한 각 줄은 레이어입니다. 각 레이어에는 이전 레이어의 델타, 차이 또는 변경 사항만 포함되어 있습니다. 이러한 레이어를 단일 실행 컨테이너로 함께 넣기 위해 Docker 는 `유니온 파일 시스템`을 사용하여 레이어를 단일 보기로 투명하게 오버레이합니다.

Image 의 각 레이어는 실행 중인 컨테이너를 위해 생성된 최상위 레이어를 제외하고 `읽기 전용`입니다. 읽기/쓰기 컨테이너 레이어는 "copy-on-write"를 구현합니다. 즉, 하위 Image 레이어에 저장된 파일은 해당 파일에 대한 편집이 수행될 때만 읽기/쓰기 컨테이너 레이어로 가져옵니다. 그런 다음 해당 변경 사항은 실행 중인 컨테이너 레이어에 저장됩니다. "copy-on-write" 기능은 매우 빠르며 거의 모든 경우 성능에 눈에 띄는 영향을 미치지 않습니다. `docker diff` 명령을 사용하여 어떤 파일이 컨테이너 수준으로 가져왔는지 검사할 수 있습니다. `docker diff` 사용 방법에 대한 자세한 내용은 [여기](https://docs.docker.com/engine/reference/commandline/diff/)에서 확인할 수 있습니다.

![understanding image layers](../assets/lab2_understanding_image_layers_1.png)

Image 레이어는 `읽기 전용`이므로 Image 및 실행 중인 컨테이너에서 공유할 수 있습니다. 예를 들어, 유사한 기본 레이어를 가진 자체 Dockerfile 로 새 Python 앱을 생성하면 첫 번째 Python 앱과 공통으로 가지고 있는 모든 레이어를 공유합니다.

```bash
FROM python:3.8-alpine
RUN pip install flask
CMD ["python","app2.py"]
COPY app2.py /app2.py
```

![understanding image layers](../assets/lab2_understanding_image_layers_2.png)

동일한 Image 에서 여러 컨테이너를 시작할 때 레이어 공유를 경험할 수도 있습니다. 컨테이너가 동일한 읽기 전용 레이어를 사용하므로 컨테이너 시작이 매우 빠르고 호스트에 매우 적은 공간을 차지한다고 상상할 수 있습니다.

이 Dockerfile 과 이 랩에서 이전에 생성한 Dockerfile 에 중복된 줄이 있는 것을 알 수 있습니다. 이는 매우 사소한 예이지만, 두 Dockerfile 의 공통 줄을 "base" Dockerfile 로 가져와서 `FROM` 명령을 사용하여 각 자식 Dockerfile 로 가리킬 수 있습니다.

Image 레이어링은 빌드 및 푸시를 위한 Docker 캐싱 메커니즘을 활성화합니다. 예를 들어, 마지막 `docker push`의 출력은 Image 의 일부 레이어가 이미 Docker Hub 에 존재함을 보여줍니다.

```bash
$ docker push $DOCKERHUB_USERNAME/python-hello-world
```

레이어를 자세히 살펴보려면 생성한 Python Image 의 `docker image history` 명령을 사용할 수 있습니다.

```bash
$ docker image history python-hello-world
```

각 줄은 Image 의 레이어를 나타냅니다. 상위 줄이 생성한 Dockerfile 과 일치하고 아래 줄이 상위 Python Image 에서 가져온다는 것을 알 수 있습니다. "\<missing\>" 태그에 대해 걱정하지 마십시오. 이것들은 여전히 정상적인 레이어입니다. Docker 시스템에서 ID 가 부여되지 않았을 뿐입니다.
