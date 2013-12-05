#!/bin/sh

#  model_selection.sh
#  
#
#  Created by Zia Rahaman
#

cd ~/r_politics_ml/data\ collection/

python ./cross_validation/cross_validation fTrain.data

for d in 2 3 4 5
do
for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
do
for digit in 0 1 2 3 4 5 6 7 8 9
do
~/svm_light/svm_learn -c $c -t 1 -d $d$ digits$digit.train kernel-$digit-c-$c-d-$d
done
done
done