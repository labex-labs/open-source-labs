# Git Stash 생성하기

개발자로서 다른 브랜치로 전환하거나 다른 기능을 작업해야 하지만 아직 변경 사항을 커밋할 준비가 되지 않은 상황에 직면할 수 있습니다. 진행 상황을 잃고 싶지 않지만, 불완전하거나 버그가 있는 코드를 커밋하고 싶지도 않을 것입니다. 이럴 때 stash 가 유용합니다.

Stash 를 사용하면 변경 사항을 커밋하지 않고 저장할 수 있으므로 다른 브랜치로 전환하거나 다른 기능을 작업할 수 있습니다. 그런 다음 변경 사항 작업을 계속할 준비가 되면 나중에 stash 를 적용할 수 있습니다.

Stash 를 생성하려면 `git stash save` 명령을 사용할 수 있습니다. `git-playground` 저장소의 `feature`라는 브랜치에서 작업 중이고 다른 브랜치로 전환하기 전에 변경 사항을 저장하려는 경우를 예로 들어 보겠습니다.

1. 먼저, `git-playground` 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. `feature`라는 브랜치로 전환합니다.

```shell
git checkout -b feature
```

3. 디렉토리의 파일에 몇 가지 변경 사항을 적용합니다.

```shell
echo "Some changes" >> README.md
```

4. 변경 사항을 stash 에 저장합니다.

```shell
git stash save "My changes"
```

5. 다른 브랜치로 전환합니다.

```shell
git checkout master
```

6. 다른 브랜치에서 변경 작업을 완료한 후, 다시 `feature` 브랜치로 전환하고 stash 를 적용합니다.

```shell
git stash apply
```

이것이 최종 결과입니다.

```shell
stash@{0}: On feature: My changes
```
