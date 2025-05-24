# Git 설정 파일 편집

개발자로서 Git 의 동작을 사용자 정의하기 위해 Git 설정 파일을 수정해야 할 수 있습니다. Git 설정 파일은 키 - 값 쌍 형식으로 설정을 포함하는 일반 텍스트 파일입니다. 이 파일은 모든 텍스트 편집기를 사용하여 편집할 수 있지만, Git 은 설정 파일을 수정하는 데 사용할 수 있는 내장 텍스트 편집기를 제공합니다.

이 예제에서는 Git 설정 파일을 편집하는 방법을 보여주기 위해 `https://github.com/labex-labs/git-playground` 디렉토리라는 Git 저장소를 사용합니다.

1. 터미널을 열고 Git 저장소 디렉토리로 이동합니다.

```shell
cd git-playground
```

2. 다음 명령을 사용하여 Git 텍스트 편집기에서 Git 설정 파일을 엽니다.

```shell
git config --global -e
```

3. 위 명령은 기본 Git 텍스트 편집기에서 Git 설정 파일을 엽니다. 사용자 이름을 `labex_git`로, 사용자 이메일을 `labex_git@example.com`으로 변경할 수 있습니다.
4. 필요한 변경을 완료했으면 <kbd>Esc</kbd> 키를 누르고 <kbd>:wq</kbd> 명령을 입력한 다음 <kbd>Enter</kbd> 키를 눌러 변경 사항을 저장하고 편집기를 종료합니다.

완료 후 결과는 다음과 같습니다.

```shell
# This is Git's per-user configuration file.
[user]
name = labex_git
email = labex_git@example.com
# Please adapt and uncomment the following lines:
#   name =
#   email = labex@64b8c76af840a200973e9d16.(none)
```
