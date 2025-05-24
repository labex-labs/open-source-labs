# 변경 배포

"hello world!" 애플리케이션은 과대평가되었으므로, 대신 "Hello Beautiful World!"라고 표시되도록 앱을 업데이트해 보겠습니다.

## `app.py` 업데이트

`app.py`에서 문자열 "Hello World"를 "Hello Beautiful World!"로 바꿉니다. 다음 명령으로 파일을 업데이트할 수 있습니다. (전체 코드 블록을 복사하여 붙여넣기)

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## Image 다시 빌드 및 푸시

이제 앱이 업데이트되었으므로, 앱을 다시 빌드하고 Docker Hub 레지스트리에 푸시하기 위해 위의 단계를 반복해야 합니다.

먼저 다시 빌드합니다. 이번에는 빌드 명령에 Docker Hub 사용자 이름을 사용합니다.

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world .
```

1-3 단계에 "Using cache"가 표시되는 것을 확인합니다. Docker Image 의 이러한 레이어는 이미 빌드되었으며 `docker image build`는 이러한 레이어를 다시 빌드하는 대신 캐시에서 사용합니다.

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

레이어를 푸시하기 위한 캐싱 메커니즘도 있습니다. Docker Hub 에는 이전 푸시에서 모든 레이어가 이미 존재하므로 변경된 레이어 하나만 푸시합니다.

레이어를 변경하면 그 위에 빌드된 모든 레이어를 다시 빌드해야 합니다. Dockerfile 의 각 줄은 이전 줄에서 생성된 레이어 위에 빌드되는 새 레이어를 빌드합니다. 이것이 Dockerfile 의 줄 순서가 중요한 이유입니다. 가장 자주 변경될 가능성이 있는 레이어 (`COPY app.py /app.py`) 가 Dockerfile 의 마지막 줄이 되도록 Dockerfile 을 최적화했습니다. 일반적으로 애플리케이션의 경우 코드가 가장 빈번하게 변경됩니다. 이러한 최적화는 자동화가 가능한 한 빨리 실행되기를 원하는 CI/CD 프로세스에 특히 중요합니다.
