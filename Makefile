clean:
	-find -name "*.un~" -exec rm {} \;
	-find -name "*.swp" -exec rm {} \;
	-find -name "*.pyc" -exec rm {} \;

run:
	python3 src/app.py

docker_run: docker_container_remove
	docker build -t toy-web-server .
	docker run -it --rm -p 8070:8070 --name toy-server toy-web-server

docker_container_remove:
	-docker stop $$(docker ps -a -q -f name=toy-server)
	-docker rm $$(docker ps -a -q -f name=toy-server)

docker_image_remove: docker_container_remove
	-docker rmi $$(docker images -q -f dangling=true)
	-docker rmi $$(docker images -q -f reference=toy-web-server)

