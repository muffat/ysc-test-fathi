# yousican test

### Endpoints
 
 Endpoint                                              | Method | Description
 ----------------------------------------------------- | ------ | ----------------
 `/songs` | GET    |  Returns a list of songs with some details on them         
 `/songs/avg/difficulty?level={level}`                   | GET   |  Returns the average difficulty for all songs	          
 `/songs/search`                  | GET    | Return a list of songs
 `/songs/rating`            | POST    | Adds a rating to the song. Ratings should be between 1 and 5
 `/songs/rating/{song_id}`   | GET    | Returns the average, the lowest and the highest rating of the given song id
  
 - Swagger UI: Nil 
 - Documentation: Please see `https://wiki.autodesk.com/x/GdXlIw`

### Prerequisites
   
- Docker


## How-tos

#### Run and test application locally

```
cd ysc-test-fathi
sh build.sh
```

There will be 3 docker containers running.
1. Tomcat with old ASE application (image name: adppa-old-ase)
2. Minio for s3 mock (image name: s3)
3. Localstack for kinesis firehose mock (image name: localstack) 

Application will be running at port 5000. http://localhost:5000/health/

Minio Console will be running at port 9001 and api at 9000. 
  - Console http://localhost:9001/
  - Console login: 
  --    User: minio_access_key
  --    Password minio_secret_key 

Minio is configured such that Bucket `epBucket` under `src/test/resources/s3` is mounted on start-up.
Firehose stream `adp-ingestion-device-analytics-ase` is created upon startup and destination bucket at s3://local.bucket. 

Localstack will be running at port 4566. Use AWS CLI to access to check on firehose stream. 

You may need to `aws configure`. Just key in any access key and secret (dummy). it should work.

Example commands:
```
aws --endpoint-url=http://localhost:4566 firehose list-delivery-streams
aws --endpoint-url=http://localhost:4566 s3 ls s3://local.bucket
```

#### Create docker image for CICD (Image Name: adppa-old-ase)
```
cd docker
./docker-build.sh
```
