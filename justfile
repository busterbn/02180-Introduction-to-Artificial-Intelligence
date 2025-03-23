IMAGE := "minmax_game:latest"

build:
	docker build -f dockerfile -t {{IMAGE}} .

run:
	docker run -it --rm -v $(pwd):/app -w /app/src {{IMAGE}}
