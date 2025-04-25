# 部署更改

“你好，世界！”这个应用程序有点过时了，让我们更新一下应用程序，使其显示“你好，美丽的世界！”。

## 更新 `app.py`

在 `app.py` 中，将字符串“Hello World”替换为“Hello Beautiful World！”。你可以使用以下命令更新文件。（复制粘贴整个代码块）

```bash
echo 'from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello beautiful world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")' > app.py
```

## 重新构建并推送你的镜像

现在你的应用程序已更新，你需要重复上述步骤来重新构建你的应用程序并将其推送到 Docker Hub 注册表。

首先重新构建，这次在构建命令中使用你的 Docker Hub 用户名：

```bash
docker image build -t $DOCKERHUB_USERNAME/python-hello-world.
```

注意步骤 1 - 3 显示“使用缓存”。Docker 镜像的这些层已经构建过，`docker image build` 将使用缓存中的这些层，而不是重新构建它们。

```bash
docker push $DOCKERHUB_USERNAME/python-hello-world
```

推送层时也有一个缓存机制。Docker Hub 已经拥有早期推送中除一层之外的所有层，所以它只推送已更改的那一层。

当你更改一层时，基于该层构建的每一层都必须重新构建。Dockerfile 中的每一行都会构建一个新层，该层是基于它之前的行创建的层构建的。这就是为什么我们 Dockerfile 中行的顺序很重要。我们优化了 Dockerfile，以便最有可能更改的层（`COPY app.py /app.py`）是 Dockerfile 的最后一行。一般来说，对于一个应用程序，你的代码变化频率最高。这种优化对于 CI/CD 流程尤为重要，在该流程中你希望自动化尽可能快地运行。
