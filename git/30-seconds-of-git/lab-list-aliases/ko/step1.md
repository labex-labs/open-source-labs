# 모든 Git 별칭 나열하기

개발자로서 시스템에 설정된 모든 Git 별칭을 나열하고 싶을 수 있습니다. 이는 다음과 같은 여러 가지 이유로 유용할 수 있습니다.

- 사용 가능한 별칭 확인
- 별칭이 매핑된 명령 확인
- 기존 별칭 제거 또는 수정

`https://github.com/labex-labs/git-playground`에 위치한 `git-playground`라는 Git 저장소가 있다고 가정해 보겠습니다.

1. 로컬 머신에서 이 저장소로 이동합니다.

```shell
cd git-playground
```

2. 다음 별칭을 설정합니다.

```shell
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.rb rebase
```

3. 모든 Git 별칭을 나열하는 동안 `sed` 명령을 사용합니다.

```shell
git config -l | grep alias | sed 's/^alias\.//g'
```

명령을 실행하면 다음과 같이 출력됩니다.

```shell
st=status
co=checkout
rb=rebase
```
