# yousican test

### Endpoints
 
 Endpoint                                              | Method | Description
 ----------------------------------------------------- | ------ | ----------------
 `/songs` | GET    |  Returns a list of songs with some details on them         
 `/songs/avg/difficulty?level={level}`                   | GET   |  Returns the average difficulty for all songs	          
 `/songs/search`                  | GET    | Return a list of songs
 `/songs/rating`            | POST    | Adds a rating to the song. Ratings should be between 1 and 5
 `/songs/rating/{song_id}`   | GET    | Returns the average, the lowest and the highest rating of the given song id

### Prerequisites
   
- Docker


## How-tos

#### Run and test application locally

```
cd ysc-test-fathi/
sh init.sh
```

There will be a docker container running.
1. uWSGI server will be running and run the application
2. config file located in /app/config/uwsgi.ini

Application will be running at port 5000. http://localhost:5000/health/