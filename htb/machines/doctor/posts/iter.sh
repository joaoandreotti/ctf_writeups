#!/bin/bash

i=0
while [ $i -lt $1 ]
do
  printf $i: 
  curl http://doctors.htb/post/$i --cookie $2 -D - -o /dev/null -s | grep HTTP
  i=$(($i+1))
done
