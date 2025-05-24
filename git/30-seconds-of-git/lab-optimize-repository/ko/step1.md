# 로컬 레포지토리 최적화

시간이 지남에 따라 Git 레포지토리는 파일의 이전 버전 및 기타 불필요한 데이터로 인해 복잡해질 수 있습니다. 이는 Git 의 속도를 늦추고 레포지토리 작업을 더 어렵게 만들 수 있습니다. 로컬 레포지토리를 최적화하려면 이러한 불필요한 데이터를 제거해야 합니다. 이는 `git gc` 명령을 사용하여 수행할 수 있습니다.

`git gc` 명령은 "Git garbage collector"의 약자입니다. 레포지토리에서 불필요한 데이터를 정리하는 데 사용됩니다. `git gc`를 실행하면 Git 은 느슨한 객체 (어떤 브랜치나 태그에서도 참조되지 않는 객체) 를 제거하고 나머지 객체를 새로운 팩 파일 세트로 묶습니다. 이렇게 하면 레포지토리의 크기를 크게 줄이고 Git 의 성능을 향상시킬 수 있습니다.

로컬 레포지토리를 최적화하려면 `--prune=now` 및 `--aggressive` 옵션과 함께 `git gc` 명령을 사용할 수 있습니다. 예를 들어, 홈 디렉토리에 위치한 `git-playground`라는 Git 레포지토리가 있다고 가정해 보겠습니다. 이 레포지토리를 최적화하려면 다음 명령을 실행합니다.

```shell
cd git-playground
git gc --prune=now --aggressive
```

이는 모든 느슨한 객체를 제거하고 나머지 객체를 새로운 팩 파일 세트로 묶어 `git-playground` 레포지토리를 최적화한 결과입니다.

![Git repository optimization result](../assets/challenge-optimize-repository-step1-1.png)
