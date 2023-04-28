```shell
git submodule deinit -f -- <submodule>
rm -rf .git/modules/<submodule>
git rm -f <submodule>
```

```shell
git submodule deinit -f -- 30code
rm -rf .git/modules/30code
git rm -f 30code
# Removes the `30code` submodule
```
