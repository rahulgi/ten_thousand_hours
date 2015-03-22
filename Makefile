docker-create-tth-dev:
	rm -f *.pyc
	rm -f */*.pyc
	docker build -t tth-dev -f ./Dockerfile.tth.dev ./

docker-create-tth-nginx:
	docker build -t tth-nginx -f ./Dockerfile.tth.nginx ./

docker-create-tth-gunicorn: docker-create-tth-dev
	docker build -t tth-gunicorn -f ./Dockerfile.tth.gunicorn ./
