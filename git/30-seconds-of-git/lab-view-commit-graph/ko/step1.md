# 저장소의 시각적 그래프 보기

개발자로서 코드가 시간에 따라 어떻게 변경되었는지 이해하기 위해 저장소의 기록을 확인해야 할 수 있습니다. 그러나 단순히 커밋 목록을 보는 것은 압도적이고 이해하기 어려울 수 있습니다. 여기서 Git 그래프가 등장합니다. 저장소의 기록을 시각화함으로써 코드가 어떻게 발전했는지 빠르게 확인하고 도입되었을 수 있는 문제 또는 버그를 식별할 수 있습니다.

Git 저장소의 시각적 그래프를 보려면 `--graph` 옵션과 함께 `git log` 명령을 사용할 수 있습니다. 예를 들어, GitHub 에서 `git-playground` 저장소의 기록을 보려고 한다고 가정해 보겠습니다.

저장소를 복제한 후 디렉토리로 이동하여 `git log` 명령을 사용하여 그래프를 볼 수 있습니다.

```shell
cd git-playground
git log --pretty=oneline --graph --decorate --all
```

이렇게 하면 저장소의 모든 커밋과 브랜치의 시각적 그래프가 표시되어 코드가 시간에 따라 어떻게 발전했는지 확인할 수 있습니다.

최종 결과는 다음과 같습니다.

```
* d22f46ba8c2d4e07d773c5126e9c803933eb5898 (HEAD -> master, origin/master, origin/feature-branch, origin/HEAD) Added file2.txt
* cf80005e40a3c661eb212fcea5fad06f8283f08f Added file1.txt
* b00b9374a7c549d1af111aa777fdcc868d8a2a01 Initial commit
```
