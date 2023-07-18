```shell
git submodule update --init --recursive
# Clones missing submodules and checks out commits
```

```shell
cd git
git submodule update --init --recursive
git submodule foreach git checkout master
```
