# Clone the lab GitHub repo

In this step you will clone the lab's GitHub repo so that you have the seccomp profiles that you will use for the remainder of this lab.

1. Clone the lab GitHub repo.

   ```bash
   git clone https://github.com/docker/labs
   ```

2. Change into the `labs/security/seccomp` directory.

   ```bash
   cd labs/security/seccomp
   ```

The remaining steps in this lab will assume that you are running commands from this `labs/security/seccomp` directory. This will be important when referencing the seccomp profiles on the various `docker run` commands throughout the lab.
