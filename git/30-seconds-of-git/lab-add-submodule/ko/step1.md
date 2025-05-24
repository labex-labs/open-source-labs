# Submodule 추가

과제는 Git repository 에 새로운 submodule 을 추가하는 것입니다. `git submodule add` 명령을 사용하여 상위 repository 에서 submodule 을 로컬 repository 의 디렉토리로 추가해야 합니다. 이 명령의 구문은 다음과 같습니다.

```shell
git submodule add <upstream-path> <local-path>
```

- `<upstream-path>`는 submodule 로 추가하려는 상위 repository 의 URL 또는 경로입니다.
- `<local-path>`는 로컬 repository 에서 submodule 을 저장하려는 경로입니다.

`my-project`라는 Git repository 가 있고, Git repository `https://github.com/labex-labs/git-playground.git`에서 submodule 을 로컬 repository 의 `git-playground`라는 디렉토리에 추가하려는 경우를 가정해 보겠습니다. 다음과 같이 할 수 있습니다.

```shell
git init my-project
cd my-project
git submodule add https://github.com/labex-labs/git-playground.git ./git-playground
```

다음은 랩을 완료한 후의 결과입니다.

![Git submodule add result](../assets/challenge-add-submodule-step1-1.png)
