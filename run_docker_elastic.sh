#!/usr/bin/env bash

docker run -p 0.0.0.0:9201:9200 -v "$PWD/esdata":/usr/share/elasticsearch/data elasticsearch