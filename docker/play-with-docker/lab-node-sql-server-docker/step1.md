# This lab walks through the evolution of a simple Node.js bulletin board application, running on Docker. You'll start with a simple app that uses hard-coded data, then add SQL Server for persistent storage, and a proxy to improve web performance.

You'll learn about packaging applications in Docker images, running distributed applications across multiple containers, and adding instrumentation to your containers so you can see the health of your application. You'll use the Docker command line, Docker Compose and Docker swarm for running the app.

> **Difficulty**: Beginner (assumes no familiarity with Docker)

> **Time**: Approximately 60 minutes

> **Tasks**:

> - [Task 0: Prerequisites](#Task_0)
> - [Task 1: Run v1 of the app in a container](#Task_1)
> - [Task 2: Add a SQL Server database container for storage](#Task_2)
> - [Task 3: Switch to high availability in swarm mode](#Task_3)
> - [Task 4: Add a reverse proxy to improve performance](#Task_4)
> - [Task 5: Add monitoring and an application dashboard](#Task_5)
