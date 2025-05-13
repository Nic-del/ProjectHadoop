#!/bin/bash

PYTHON=python2

#1 : Valider les donnes
$PYTHON validation.py

#Crée le dossier de sortie s’il existe 
rm -r output 2>/dev/null

#2 : Hadoop Streaming
hadoop jar /usr/hdp/3.0.1.0-187/hadoop-mapreduce/hadoop-streaming.jar \
  -input dpt2022_valid.csv \
  -output output \
  -mapper "$PYTHON mapperFiltre.py" \
  -reducer "$PYTHON reducer.py" \
  -file mapperFiltre.py \
  -file reducer.py

#3 : Post-traitement en local
hdfs dfs -cat /user/maria_dev/logs/output/part-00000 | $PYTHON post_traitement.py
