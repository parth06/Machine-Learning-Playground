import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

data = pd.read_csv('indians-diabetes.data', header = None, delimiter=' *, *', engine='python')
data.columns = ['num_pregent', 'glucose', 'bp', 'triceps', 'serum', 'bmi', 'dpf', 'age', 'class']

#extract features and targets from the data
features = data.values[:,:8]
target = data.values[:,8]

#Split arrays or matrices into random train and test subsets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size = 0.33, random_state = 10)

#Create a SVM Classifier
clf = SVC(kernel='rbf', C=10000)

#Fit SVM according to features_train, target_train
clf.fit(features_train, target_train)

#Perform classification on an array of test vectors 
target_pred = clf.predict([1,89,66,23,94,28.1,0.167,21])

if target_pred == [1]:
    print("Diabetes positive")
else:
    print("Diabetes negative")

#Returns the mean accuracy on the given test data and labels.
print (clf.score(features_test, target_test)*100)