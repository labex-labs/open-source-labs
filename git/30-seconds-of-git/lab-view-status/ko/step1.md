# 현재 상태 보기

개발자로서 Git 저장소의 현재 상태를 아는 것은 중요합니다. 여기에는 수정된 파일, 커밋을 위해 스테이징된 파일, 그리고 추적되지 않은 파일에 대한 정보가 포함됩니다. `git status` 명령은 이 정보를 읽기 쉬운 형식으로 제공합니다.

귀하의 과제는 `git status` 명령을 사용하여 `https://github.com/labex-labs/git-playground`에 위치한 Git 저장소의 현재 상태를 확인하는 것입니다. 명령의 출력을 주의 깊게 살펴보고 그 의미를 이해하려고 노력해야 합니다.

이 랩을 완료하려면 `https://github.com/labex-labs/git-playground`에 위치한 Git 저장소를 클론 (clone) 해야 합니다.

1. 저장소를 클론한 후, 저장소의 루트 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. Git 저장소의 현재 상태를 확인합니다.

```shell
git status
```

이렇게 하면 작업 트리 (working tree) 의 현재 상태가 출력됩니다. 현재 사용 중인 브랜치 (branch) 가 무엇인지, 브랜치가 원격 저장소 (remote repository) 와 최신 상태인지, 그리고 추적되지 않거나 수정된 파일이 있는지에 대한 정보를 확인할 수 있습니다.

출력은 다음과 같습니다.

```shell
[object Object]
```
