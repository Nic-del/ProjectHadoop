#!/bin/bash

PYTHON=python2

#1 : Valider les donnes
$PYTHON validation.py

#Crée le dossier de sortie s’il existe 
hdfs dfs -rm -r -f output

#2 : Hadoop Streaming
hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming.jar \
  -input dpt2022_valid.csv \
  -output output \
  -mapper "$PYTHON mapperv1.py" \
  -reducer "$PYTHON reducerV1.py" \
  -file mapperv1.py \
  -file reducerV1.py

#3 : Post-traitement en local
hdfs dfs -cat /user/maria_dev/logs/output/part-00000 | $PYTHON post_traitementV1.py
