# Git 명령어 자동 수정

문제는 개발자가 Git 명령어를 자주 잘못 입력하여 오류가 발생하고 워크플로우가 느려질 수 있다는 것입니다. 예를 들어, 개발자가 실수로 `git status` 대신 `git sttaus`를 입력하면 오류 메시지가 표시됩니다. 이는 특히 많은 파일과 협업자가 있는 대규모 프로젝트에서 작업할 때 좌절감을 유발하고 시간을 낭비할 수 있습니다.

Git 의 자동 수정 기능을 사용하는 방법을 보여주기 위해, `https://github.com/labex-labs/git-playground`라는 이름의 Git 저장소 디렉토리를 사용하겠습니다.

1. 터미널을 열고 저장소를 복제하려는 디렉토리로 이동합니다.
2. 다음 명령을 사용하여 저장소를 복제합니다.

```
git clone https://github.com/labex-labs/git-playground.git
```

3. 다음 명령을 사용하여 복제된 저장소로 이동합니다.

```
cd git-playground
```

4. 다음 명령을 사용하여 Git 의 자동 수정 기능을 활성화합니다.

```
git config --global help.autocorrect 1
```

5. `git sttaus`와 같이 Git 명령어를 잘못 입력해 봅니다. Git 은 자동으로 명령어를 수정하고 대신 `git status`를 실행합니다.

다음은 랩을 완료한 후의 결과입니다.

![Git autocorrect command result](../assets/challenge-autocorrect-step1-1.jpg)
