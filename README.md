## Run your docker container of mysql from offical image.
- docker run -d -p 3306:3306 --name mera_sql -e MYSQL_ROOT_PASSWORD=1234567  mysql:latest
- Now through mysql_workbench you should be able to connect to container.
## Follow offical link for good information.
- https://hub.docker.com/_/mysql

## Additional information
- https://stackoverflow.com/questions/33827342/how-to-connect-mysql-workbench-to-running-mysql-inside-docker


### Flask with mysql local/ mysql container::
- Good one :  https://www.codementor.io/@adityamalviya/python-flask-mysql-connection-rxblpje73

## If you don't have  a workbench installed just run this to set workbench in container.
- ` docker run -d \
    --name=mysql-workbench \
    -e PUID=1000 \
    -e PGID=1000 \
    -e TZ=Europe/London \
    -p 3000:3000 \
    -v /path/to/config:/config \
    --cap-add="IPC_LOCK" \
    --restart unless-stopped \
    linuxserver/mysql-workbench `
- you sql-workbench is running at localhost:3000


## I was geeting error while installing 
-  `pip install Flask-MySQLdb`
- installed this first
sudo apt-get install libmysqlclient-dev
