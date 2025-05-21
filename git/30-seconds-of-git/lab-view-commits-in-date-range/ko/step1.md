# Git 리포지토리 복제 (Cloning the Git Repository)

Git 의 날짜 범위 필터링 기능을 탐색하기 위해 먼저 작업할 Git 리포지토리가 필요합니다. LabEx 에서 제공하는 `git-playground` 리포지토리를 사용하겠습니다.

리포지토리를 복제하는 것부터 시작해 보겠습니다.

1. LabEx VM 에서 터미널을 엽니다.

![terminal](../assets/screenshot-20250306-shbu3WrQ@2x.png)

2. 다음 명령을 실행하여 리포지토리를 복제합니다.

```bash
git clone https://github.com/labex-labs/git-playground
```

다음과 유사한 출력을 볼 수 있습니다.

```
Cloning into 'git-playground'...
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 8 (delta 0), reused 8 (delta 0), pack-reused 0
Receiving objects: 100% (8/8), done.
```

3. 리포지토리 디렉토리로 이동합니다.

```bash
cd git-playground
```

이제 로컬 머신에 리포지토리가 있으므로 커밋 히스토리를 탐색할 수 있습니다.
