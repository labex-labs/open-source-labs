# 마지막 커밋 작성자 변경

Git 저장소에 커밋을 방금 수행했지만, 작성자 이름과 이메일 주소가 잘못되었음을 깨달았습니다. 커밋의 내용을 변경하지 않고 작성자 정보를 업데이트하고 싶습니다. Git 을 사용하여 어떻게 이를 달성할 수 있을까요?

마지막 커밋의 작성자를 변경하려면 `git commit --amend` 명령을 사용할 수 있습니다. 이 명령을 사용하면 Git 저장소의 마지막 커밋을 수정할 수 있습니다. 다음은 작성자 이름과 이메일 주소를 변경하는 방법의 예입니다.

1. `https://github.com/labex-labs/git-playground`라는 Git 저장소를 로컬 머신에 복제합니다.

```shell
git clone https://github.com/labex-labs/git-playground.git
```

2. GitHub 계정을 사용하여 Git 의 ID 정보를 구성합니다.

```shell
cd git-playground
git config user.email "your email"
git config user.name "your username"
```

3. `git commit --amend` 명령을 사용하여 마지막 커밋의 작성자를 수정하고 내용을 저장합니다.

```shell
git commit --amend --author="Duck Quackers <cool.duck@qua.ck>"
```

4. 작성자 정보가 업데이트되었는지 확인합니다.

```shell
git log
```

마지막 커밋의 작성자가 이제 `Duck Quackers`임을 확인할 수 있습니다.

```shell
commit d5a385cc354f3528472a215b66cbb7c628ba47d5
Author: Duck Quackers <cool.duck@qua.ck>
Date:   Wed Apr 26 14:16:25 2023 +0800

    Added file2.txt
```
