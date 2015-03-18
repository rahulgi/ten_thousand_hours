docker-create-tth:
	rm -f *.pyc
	rm -f */*.pyc
	docker build -t tth_django -f ./Dockerfile.tth.django ./

docker-create-tth-nginx:
	docker build -t tth_nginx -f ./Dockerfile.tth.nginx ./
