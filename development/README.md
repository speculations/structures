<br>

### Notes

```shell
docker build . --file .devcontainer/Dockerfile -t points
```

```shell
 docker run --rm -i -t -p 127.0.0.1:10000:8888 -w /app --mount type=bind,src="$(pwd)",target=/app -v ~/.aws:/root/.aws points
```

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>
