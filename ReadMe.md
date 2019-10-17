##### Prerequisites
- Install docker; https://docs.docker.com/docker-for-mac/install/
- Install docker-compose; pip install docker-compose


##### Start server

    make up
- server runs in port 5000, es at 9200, refer `docker-compose.yml`


##### Stop server

    make down

##### Logs
`docker ps`; lists all the running containers

`docker logs -f flask_es_web_1`; prints logs of flask server

`docker logs -f flask_es_es_1`; prints logs of elasticsearch server

##### Notes
- Elastic search data is stored inside `volumes` folder
- Although the code is written in such a way to initialise data at the start,
      data might not be loaded because es might not have started by the time flask app starts
       run `make up` again after es is up to mitigate this
- Configure env vars in `src/config/config.env`
