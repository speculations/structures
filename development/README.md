<br>

## Remote Development Environment

The environment's image is built via:

```shell
docker build . --file .devcontainer/Dockerfile -t points
```

Naming the new image `points`.  Subsequently, use a container/instance of the image `points` as a
development environment via the command:

```bash
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app 
  --mount type=bind,src="$(pwd)",target=/app points
```

or

```bash
docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app 
  --mount type=bind,src="$(pwd)",target=/app -v ~/.aws:/root/.aws points
```

Whereby:

* [--rm](https://docs.docker.com/engine/reference/commandline/run/#:~:text=a%20container%20exits-,%2D%2Drm,-Automatically%20remove%20the): Automatically remove container on exit.
* [-i](https://docs.docker.com/engine/reference/commandline/run/#:~:text=and%20reaps%20processes-,%2D%2Dinteractive,-%2C%20%2Di): Interact.
* [-t](https://docs.docker.com/get-started/02_our_app/#:~:text=Finally%2C%20the-,%2Dt,-flag%20tags%20your): Tag.
* [-p](https://docs.docker.com/engine/reference/commandline/run/#:~:text=%2D%2Dpublish%20%2C-,%2Dp,-Publish%20a%20container%E2%80%99s): Publish a container's set of port to the host.


Additionally, `-p 10000:8888` maps the host port `10000` to container port `8888`.  Note, the container's working environment,
i.e., -w, must be inline with this project's top directory.  The latter, second, option is important for interactions
with Amazon Web Services; **never deploy a root container, study the production** [Dockerfile](/Dockerfile); never deploy a development container with root settings.  Get the name of the running instance of `points` via:

```shell
docker ps --all
```

A developer may attach an IDE (independent development environment) application to a running container.  Considering
IntelliJ IDEA:

> Connect to the Docker [daemon](https://www.jetbrains.com/help/idea/docker.html#connect_to_docker)
> * **Settings** $\rightarrow$ **Build, Execution, Deployment** $\rightarrow$ **Docker** $\rightarrow$ **WSL:** `operating system`
> * **View** $\rightarrow$ **Tool Window** $\rightarrow$ **Services** <br>Within the **Containers** section connect to the running instance of interest, or ascertain connection to the running instance of interest.

Similarly, Visual Studio Code as its container attachment instructions; study [Attach Container](https://code.visualstudio.com/docs/devcontainers/attach-container).


<br>
<br>


## Code Analysis

The GitHub Actions script [main.yml](../.github/workflows/main.yml) conducts code analysis within a Cloud GitHub Workspace.  Depending on the script, code analysis may occur `on push` to any repository branch, or `on push` to a specific branch.

The sections herein outline remote code analysis.

### pylint

The directive

```shell
pylint --generate-rcfile > .pylintrc
```

generates the dotfile `.pylintrc` of the static code analyser [pylint](https://pylint.pycqa.org/en/latest/user_guide/checkers/features.html).  Subsequently, analyse a directory via the command

```shell
python -m pylint --rcfile .pylintrc {directory}
```

The `.pylintrc` file of this template project has been **amended to adhere to team norms**, including

* Maximum number of characters on a single line.
  > max-line-length=127

* Maximum number of lines in a module.
  > max-module-lines=135


<br>


### pytest & pytest coverage

> [!IMPORTANT]
> Within main.yml, enable pytest & pytest coverage via patterns akin to
>
> * pytest -o python_files=test_*
> * pytest --cov-report term-missing  --cov src/data/... tests/data/...
>

Within a remote environment conduct apply/conduct a pytest via

```shell
python -m pytest ...
```

Replace the ellipses with, e.g., a file name.

<br>
<br>

### flake8

For code & complexity analysis.  A directive of the form

```bash
python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics src/data
```

inspects issues in relation to logic (F7), syntax (Python E9, Flake F7), mathematical formulae symbols (F63), undefined variable names (F82).  Additionally

```shell
python -m flake8 --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics src/data
```

inspects complexity.

<br>
<br>

## Delivering Assets

We may deliver assets to GitHub Container Registry (GCR) and/or Amazon ECR (Elastic Container Registry).  **If you do not have an Amazon account and/or** you have not set up the GitHub Secrets

* AWS_ENTRY
* AWS_ARN_ECR_ACTIONS: Amazon ECR & GitHub Actions interaction role.  Ensure the trust policy of the role refers to this repository's GitHub Organization.
* AWS_REGION: region code
* ECR_REPOSITORY: The name of the Amazon ECR repository that assets will be delivered to.

that enable delivery to Amazon ECR via the directive

```yaml
  with:
    role-to-assume: arn:aws:iam::${{ secrets.AWS_ENTRY }}:role/${{ secrets.AWS_ARN_ECR_ACTIONS }}
    aws-region: ${{ secrets.AWS_REGION }}
```

then set the `ecr` section of [main.yml](../.github/workflows/main.yml) to *false*, i.e.,

```yaml
  ecr:
    name: Amazon Elastic Container Registry
    needs: build
    if: ${{ false }}
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
