# Selectively remove syscalls

In this step you will see how applying changes to the `default.json` profile can be a good way to fine-tune which syscalls are available to containers.

The `default-no-chmod.json` profile is a modification of the `default.json` profile with the `chmod()`, `fchmod()`, and `chmodat()` syscalls removed from its whitelist.

1. Start a new container with the `default-no-chmod.json` profile and attempt to run the `chmod 777 / -v` command.

   ```bash
   docker run --rm -it --security-opt seccomp=./seccomp-profiles/default-no-chmod.json alpine sh
   ```

   and then from inside the container:

   ```bash
   chmod 777 / -v
   ```

   ```
   chmod: /: Operation not permitted
   ```

The command fails because the `chmod 777 / -v` command uses some of the `chmod()`, `fchmod()`, and `chmodat()` syscalls that have been removed from the whitelist of the `default-no-chmod.json` profile.

2. Exit the container.

```bash
exit
```

3. Start another new container with the `default.json` profile and run the same `chmod 777 / -v`.

   ```bash
   docker run --rm -it --security-opt seccomp=./seccomp-profiles/default.json alpine sh
   ```

   and then from inside the container:

   ```bash
   chmod 777 / -v
   ```

   ```
   mode of '/' changed to 0777 (rwxrwxrwx)
   ```

The command succeeds this time because the `default.json` profile has the `chmod()`, `fchmod()`, and `chmodat` syscalls included in its whitelist.

4. Exit the container.

```bash
exit
```

5. Check both profiles for the presence of the `chmod()`, `fchmod()`, and `chmodat()` syscalls.

   Be sure to perform these commands from the command line of your Docker Host and not from inside of the container created in the previous step.

   ```bash
   cat ./seccomp-profiles/default.json | grep chmod
   ```

   ```
   "name": "chmod",
   "name": "fchmod",
   "name": "fchmodat",
   ```

   ```bash
   cat ./seccomp-profiles/default-no-chmod.json | grep chmod
   ```

   The output above shows that the `default-no-chmod.json` profile contains no **chmod** related syscalls in the whitelist.

In this step you saw how removing particular syscalls from the `default.json` profile can be a powerful way to start fine tuning the security of your containers.
