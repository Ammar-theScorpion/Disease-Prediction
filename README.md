			                                         Heart Disease Prediction
This project is a machine learning model that is designed to predict the likelihood of an individual developing heart disease based on a variety of factors. The model is trained on a large dataset of patient information, including demographics, medical history, and various health measurements such as blood pressure and cholesterol levels. Using advanced algorithms, the model is able to analyze this data and learn patterns that are associated with an increased risk of heart disease.

Once trained, the model can be used to predict the risk of heart disease for a new individual by inputting their data into the model. This can be useful for doctors and other healthcare professionals in identifying individuals who may be at higher risk of developing heart disease and in need of preventative care. It can also be used by individuals themselves to help them understand their own risk of heart disease and take steps to reduce that risk.



Data and features:
Our data consists of around 300000 samples composed of both object and numeric data.
![Picture1](https://user-images.githubusercontent.com/79399411/207529511-424b97fe-f2e0-4adf-a1b8-1e8367a29139.png)


About the Data:
	We Have no null values in the dataset.
	Most of the data is object data.
	all the values are valid and there are no missing values.
	all numerical variables are skewed and contain outliers. We replaced them with the mean of each column
	Most of people in our data are white and have no diabetic.
	Most of them had done a physical activity during the past 30 days other than their regular job and in general they have very good health as they said.
	A little of them who have asthma, kidney disease and skin cancer.
	Most people said that they have generally very good health. A few of people who said that they have generally a poor health


Cleaning and Scaling:
	First I had to use One Hot Encoding for some of categorical columns like ‘Sex, Smoking, Stroke, DiffWalking’ and any column has the type of ‘Yes/No’ answers 	      and Ordinal encoder for the others like ’AgeCategory, Race, GenHealth’.  But the results turned out to be so poor that Precision and Recall dropped down to           zero.
	To make up the result, we used OrdinalEncoder for object columns and StanderdScaler for numeric columns and the result turned to our interest.

Train and Split:
	Split the data using Cross Validation(StratigiedKFold) to ensure that we have a small piece of all different samples.
	Used Logisitic Regression, Decision Tree Classifier, Random Forest Classifier SVM
	The best one is ‘Decision Tree Classifier, with a recall of 0.746 and precision of 0.68. With hyper parameter tuning, the recall improved by 0.164 so the 	   total recall is around 0.76.  Out of curiosity, I run the program against SVM with hyper parameter tuning I got a way better recall but was less precise. The 	  recall now is 0.82, since recall is the most important factor I stick to it.

Diabetes
 Data and features:
	Our data consists of around 700 samples composed of numeric data only.

About the Data:
	Pregnancies: Number of times the patient was pregnant.
	Glucose: Plasma glucose concentration over two hours in an oral glucose tolerance test.
	BloodPressure: Diastolic blood pressure (mm Hg).
	SkinThickness: Triceps skin fold thickness (mm).
	Insulin: Two-Hour serum insulin (mu U/ml).
	BMI: Body mass index (weight in kg/(height in m)^2).
	DiabetesPedigreeFunction/DPF: A function that scores the likelihood of diabetes based on 	family history.
	Age: In years.
	Outcome: Class variable (0 if non-diabetic, 1 if diabetic). This is the target variable.
	all numerical variables are skewed and contain outliers. We replaced them with the mean of each column


Cleaning and Scaling:
	Our data is small and simple, No Object columns, No Null values and No missing data. The data is all clean and ready to go we had only to scale it down using 		‘StanderdScaler’

Train and Split:
	Split the data between x_train, y_train, x_test, y_test. Test data has around 20% of the data and the remaining part of it for train data. Didn’t use 		CrossVaildtion because the data is small and distributed equally.
	Used Logistic Regression, SGDClassifier, and SVM
	The best one is ‘Logistic Regression’, with a recall of 0.65 and precision of 0.6297. With hyper parameter tuning, the recall improved by 0.264 so the total         recall is around 0.68.  Out of curiosity, I run the program against SVM with hyper parameter tuning I got a way better recall but was less precise. The 	             recall now is 0.629, since recall is the most important factor we stick to Logistic Regression.


,
