# **Detecting Credit Card Fraud**

## **Overview**

Using a dataset comprised of nearly 300,000 anonymized credit card transactions, the aim of this project was to build a classification model capable of recognizing fraudulent credit card transactions.

## **Dataset Description**

The dataset used for the project originally came from Kaggle (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). The dataset contains 31 fields (28 of which were the result of a PCA transformation). The remaining columns contain information about the time a purchase happened, the amount spent, and whether or not a transaction was fraudulent.

## **Required Packages**

The notebook associated with this project uses Python 3.9.12 as well as the following packages:

* imblearn 0.10.1
* matplotlib 3.5.1
* numpy 1.24.3
* pandas 1.4.2
* seaborn 0.11.2
* sklearn 1.1.2
* xgboost 1.7.6

## **Findings**

Since there were only a total of 492 fraudulent transactions, little attention was given to any of the
classifiers' accuracy scores during the model evaluation process. Instead, only the models with the highest f1, recall, and precision scores were considered for additional hyperparameter tuning. Both oversampling (SMOTE) and undersampling (Random Undersampling) techniques were also utilized to address the imbalanced nature of the dataset. Ultimately, a tuned XG Boost Classifier was selected as it was the model that performed best on the original test set.
