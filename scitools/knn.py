
#KNN crossval and test.
test = open('test.results', 'w')
knn9 = open('knn9.results', 'w')
knn12 = open('knn12.results', 'w')
knn15 = open('knn15.results', 'w')
knn18 = open('knn18.results', 'w')
from sklearn.datasets import load_svmlight_file
X_train, y_train = load_svmlight_file(
	"train.data")
X_val, y_val = load_svmlight_file(
	"test.data")

from sklearn.neighbors import KNeighborsRegressor
ntest = KNeighborsRegressor(n_neighbors=14, weight = 'distance')
print("neigh14")
neigh9 = KNeighborsRegressor(n_neighbors=9, weight = 'distance')
print("neigh9")
neigh12 = KNeighborsRegressor(n_neighbors=12, weight = 'distance')
print("neigh12")
neigh15 = KNeighborsRegressor(n_neighbors=15, weight = 'distance')
print("neigh15")
neigh18 = KNeighborsRegressor(n_neighbors=18, weight = 'distance')
print("neigh18")

ntest.fit(X_train, y_train)
for i in ntest.predict(X_val):
	test.write(str(i) + "\n")
test.close()

neigh9.fit(X_train, y_train)
for i in neigh9.predict(X_val):
	knn9.write(str(i) + "\n")
knn9.close()

neigh12.fit(X_train, y_train)
for i in neigh12.predict(X_val):
	knn12.write(str(i) + "\n")
knn12.close()

neigh15.fit(X_train, y_train)
for i in neigh15.predict(X_val):
	knn15.write(str(i) + "\n")
knn15.close()

neigh18.fit(X_train, y_train)
for i in neigh18.predict(X_val):
	knn18.write(str(i) + "\n")
knn18.close()




