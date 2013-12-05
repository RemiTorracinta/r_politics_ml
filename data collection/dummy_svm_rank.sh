cd ~/r_politics_ml/data\ collection/

~/svm_rank/svm_rank_learn -c .01 fTrain.data base_rank_model
~/svm_rank/svm_rank_classify fTest.data base_rank_model base_rank_predictions
python performance.py fTest.data base_rank_predictions
