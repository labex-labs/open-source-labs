# 다른 작성자가 커밋 생성하기

팀 개발자와 함께 프로젝트를 진행하는 상황을 가정해 보겠습니다. 팀원 중 한 명이 코드에 몇 가지 변경 사항을 적용했지만, 본인이 변경 사항을 커밋할 수 없는 상황입니다. 이 경우, 해당 팀원을 대신하여 커밋을 생성해야 합니다. 이러한 시나리오에서는 `--author` 옵션을 사용하여 커밋 작성자의 이름과 이메일을 변경할 수 있습니다. 이 옵션은 휴가 또는 병가 중인 동료를 대신하여 코드를 커밋하는 경우와 같이, 다른 사람에게 커밋을 귀속시켜야 할 때 유용합니다.

다른 작성자가 커밋을 생성하려면 다음 명령을 사용할 수 있습니다.

```shell
git commit -m < message > --author="<name> <email>"
```

`https://github.com/labex-labs/git-playground` 저장소에서 호스팅되는 프로젝트를 진행하고 있다고 가정해 보겠습니다. 코드에 몇 가지 변경 사항을 적용했으며, 변경 사항을 직접 커밋할 수 없는 동료 John Doe 를 대신하여 커밋을 생성해야 합니다. 이를 위해 다음 명령을 사용할 수 있습니다.

```shell
git clone https://github.com/labex-labs/git-playground
cd git-playground
git config --global user.email "your email"
git config --global user.name "your username"
echo "Fix the network bug" > README.md
git add .
git commit -m "Fix the bug" --author="John Doe <john.doe@example.com>"
```

이 명령은 "Fix the bug" 메시지와 함께 새로운 커밋을 생성하고 John Doe 에게 귀속시킵니다.

다음은 최종 결과입니다.

![Git commit author change result](../assets/challenge-commit-set-author-step1-1.png)
