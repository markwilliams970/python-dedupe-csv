#!/bin/bash

cat samples.csv | awk 'BEGIN{FS=","}{if($7>5){for(i=1;i<=4;i++){printf("%s\n",$0)}}else{print $0}}' > sample_with_duplicates.csv
