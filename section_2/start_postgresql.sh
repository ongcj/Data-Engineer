#!/bin/bash

docker build . -t gt_postgresql 
docker run -d -p 5432:5432 --name car_dealership -v $(pwd)/data:/var/lib/postgresql/data gt_postgresql
