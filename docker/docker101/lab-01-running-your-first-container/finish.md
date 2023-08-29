# Summary

In this lab, you created your first Ubuntu, Nginx and MongoDB containers.

Key Takeaways

- Containers are composed of linux namespaces and control groups that provide isolation from other containers and the host.
- Because of the isolation properties of containers, you can schedule many containers on a single host without worrying about conflicting dependencies. This makes it easier to run multiple containers on a single host: fully utilizing resources allocated to that host, and ultimately saving some money on server costs.
- Avoid using unverified content from the Docker Store when developing your own images because these images may contain security vulnerabilities or possibly even malicious software.
- Containers include everything they need to run the processes within them, so there is no need to install additional dependencies directly on your host.
