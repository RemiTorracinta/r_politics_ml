cd ~/r_politics_ml/data\ collection/


~/svm_light/svm_learn -z p fTrain.data base_model
~/svm_light/svm_classify fTest.data base_model base_predictions
python performance.py fTest.data base_predictions