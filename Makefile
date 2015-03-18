docker-create-tth:
	rm *.pyc
	rm */*.pyc
	docker build -t tth_django ./
