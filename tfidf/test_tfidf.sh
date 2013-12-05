#!/bin/sh

#  test_tfidf.sh
#  
#
#  Created by Zia Rahaman on 12/5/13.
#

cd ~/r_politics_ml/tfidf



#for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
#do
#~/svm_rank/svm_rank_learn -c $c ./fTrain.data-tf_idf ./test/model-$c
#done






#for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
#do
#~/svm_rank/svm_rank_classify ./fTest.data-tf_idf ./test/model-$c ./test/predict-$c
#done



for c in 0.0001 0.0005 0.001 0.005 0.01 0.05 0.1
do
echo "c is " $c
python ../SVM_rank/performance.py ./fTest.data-tf_idf ./test/predict-$c
done
