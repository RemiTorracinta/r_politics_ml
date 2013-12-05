#!/bin/sh

#  model_selection.sh
#  
#
#  Created by Zia Rahaman
#

cd ~/r_politics_ml/SVM_rank

python ../cross_validation/cross_validation.py ../predecap\ data/fTrain.data


for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
do
for digit in 0 1 2 3 4 5 6 7 8 9
do
~/svm_rank/svm_rank_learn -c $c train$digit.data ./linear/model-$digit-$c
done
done
done



for digit in 0 1 2 3 4 5 6 7 8 9
do
for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
do
~/svm_rank/svm_classify val$digit.data ./linear/model-$digit-$c ./linear/predict-$digit-$c
done
done
done

