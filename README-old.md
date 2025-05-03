# Belief Revision Engine


## Requirements

This project is setup to require a minimal number of utilities installed
locally. To do this, most of the task done during local development is performed
in [Docker](https://www.docker.com/). The requirements are thus:

- [🐳 Docker](https://www.docker.com/)
- [🤖 Just](https://github.com/casey/just)

---

## Build instructions

Follow these steps to build the project:

1. Clone this repository:
    ```bash
    cd ~/
    git clone https://github.com/busterbn/02180-Introduction-to-Artificial-Intelligence.git
    cd 02180-Introduction-to-Artificial-Intelligence
    git switch belief_revision
    ```

2. Build the Docker image:
    ```bash
    just build
    ```
