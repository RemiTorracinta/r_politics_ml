#!/bin/sh

#  test.sh
#  
#
#  Created by Zia Rahaman on 12/5/13.
#


cd ~/r_politics_ml/SVM_rank



#for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
#do
#~/svm_rank/svm_rank_learn -c $c ../predecap\ data/fTrain.data ./test/model-$c
#done






#for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
#do
#~/svm_rank/svm_rank_classify ../predecap\ data/fTest.data ./test/model-$c ./test/predict-$c
#done



for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
do
echo "c is " $c
python ./performance.py ../predecap\ data/fTest.data ./test/predict-$c
done
