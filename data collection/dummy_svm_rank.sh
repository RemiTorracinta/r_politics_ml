cd ~/r_politics_ml/data\ collection/

python partition.py
python partition_tfidf.py

~/svm_rank/svm_rank_learn -c .01 fTrain.data base_rank_model
~/svm_rank/svm_rank_classify fTest.data base_rank_model base_rank_predictions



~/svm_rank/svm_rank_learn -c .01 fTrain.data-tf_idf base_rank_model_tf
~/svm_rank/svm_rank_classify fTest.data-tf_idf base_rank_model_tf base_rank_predictions_tf
python performance.py fTest.data base_rank_predictions
python performance.py fTest.data-tf_idf base_rank_predictions_tf