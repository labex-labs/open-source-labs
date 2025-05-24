# 병합된 브랜치 보기

귀하의 과제는 `https://github.com/labex-labs/git-playground`라는 Git 저장소에서 병합된 모든 로컬 브랜치의 목록을 출력하는 것입니다. 병합된 브랜치 목록을 표시하려면 `git branch -a --merged` 명령을 사용해야 합니다. 목록을 얻은 후에는 화살표 키를 사용하여 탐색하고 <kbd>Q</kbd>를 눌러 종료할 수 있습니다.

1. 저장소 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. 병합된 브랜치 목록을 봅니다.

```shell
git branch -a --merged
```

최종 결과는 다음과 같습니다.

```
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/feature-branch
  remotes/origin/master
```
