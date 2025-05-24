# 커밋 요약 보기

개발자로서, 여러 기여자가 있는 프로젝트를 작업하고 있습니다. 변경 사항을 이해하고 잠재적인 문제를 식별하기 위해 프로젝트에 이루어진 모든 커밋의 요약을 볼 필요가 있습니다. 하지만 필요한 정보를 찾기 위해 모든 커밋 메시지를 일일이 살펴보는 데 많은 시간을 쓰고 싶지는 않습니다.

Git 저장소에 이루어진 모든 커밋의 짧은 요약을 보려면 `git log --oneline` 명령을 사용할 수 있습니다. 예를 들어, GitHub 에서 호스팅되는 `git-playground`라는 프로젝트를 작업하고 있다고 가정해 보겠습니다.

1. 다음 명령을 사용하여 저장소를 로컬 머신 (local machine) 에 복제할 수 있습니다.

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. 저장소를 복제한 후, 프로젝트 디렉토리로 이동하여 다음 명령을 실행하여 모든 커밋의 짧은 요약을 봅니다.

```shell
cd git-playground
git log --oneline
```

이렇게 하면 저장소에 이루어진 모든 커밋 목록과 각 커밋 메시지의 짧은 요약이 출력됩니다. 예를 들어 다음과 같습니다.

```shell
d22f46b (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
cf80005 Added file1.txt
b00b937 Initial commit
```
