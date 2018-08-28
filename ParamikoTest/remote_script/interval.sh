#!/usr/bin/env bash

let i=30
echo '' > /tmp/interval.txt

while [ $i -ne 0 ]
do
   echo `date` >> /tmp/interval.txt
   sleep 1
   let i=i-1
done


