# Lung Cancer Diagnosis and Survival Risk Prediction Models


## Purpose

This is an application that I created for my Bachelor's degree Thesis. The purpose is to make a web application which will workas a decision support system for either professionals or 
non-experienced people to use, which will be able to detect the existence of lung cancer based on simple information like symptoms and habits. If lung cancer is 
detected, the application proceeds to ask for more information in order to make a decision for the chance of survival of the patient for more than a year after surgery removal. In this file we are going to discuss the 
process to create our application step to step, so thanks in advance for reading this!


## Data

To find the data required for training our models, we used a popular web platform called [Kaggle](kaggle.com) which hosts datasets of every kind possible, which users can upload or download without restrictions, in order
to use them for their own projects. Because of the nature of our application, we needed two different datasets, one for each model that we are going to create. 


#### Diagnosis Dataset

This dataset is made of two hundred and eighty four (284) instances, each consisting of sixteen (16) attributes filled with boolean data and is available [here](https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer).
Some of the attributes are: _Gender, Age, Alcohol Consuming, Peer Pressure, Wheezing etc._.


#### Survival Prediction Dataset

This set consists of four hundred and seventy (470) instances with sixteen (16) attributes of integer and real type and can be found [here](https://www.kaggle.com/datasets/sid321axn/thoraric-surgery). It requires more 
complex information, as it asks for: _Forced Vital Capacity, Perfirmance Status (in Zubrod Scale), Size of the original tumor, Dyspnoea before surgery etc._


## Data Preprocessing

In this section of the development we used the same techniques for both datasets so it is only natural to explain them together. After the usage of each of the following techniques, we created a different version of our
dataset in order to compare them in the end and find out which provides the best results.

- First things first, we had to make sure that there were no missing or duplicate data, because that would influence our metrics in the wrong way.
After finding them, we erased them completely from the dataset,because they were an insignificant ammount that wouldn't change our end result.

* The next technique was the spread subsample, which was used in order to make our classed more equal in both our datasets. That was necessary, because both our datasets are greatly imbalanced and by equalizing their classes 
we can handle them better and get better results.

+ Our last effort to make our data better and greatly improve our metrics was the Attribute Selection technique, which removes any unnecessary attributes from the dataset that don't really provide anything in the decision.


## Metrics

After gathering and "cleaning" our data, the next step is to acess the performance of the different versions of the datasets that we made with the different machine learning algorithms that are available,
in order to choose the one with the best metrics to use on our application. After some experimenting with algorithms such as Decision Tree, Random Forest, Naive Bayes etc., we found the best results using the 
Extreme Gradient Boosting (or XGBoost) machine learning algorithm, which proved that it can handle our data's imbalance greatly. Our deciding factor was the balanced accuracy and after choosing the right version for us,
we decided to document the other metrics of the model too, which are important too. To do this, we used 10 - Fold Cross Validation, a popular technique among Machine Learning Engineering used in performance acessment. 
Although the metrics of the survival prediction model were quite average, they were still enough to proceed with the next step which is the creation of the models. The metric results of each model are shown in the 
following table:

| Diagnosis Model | Metric            | Survival Prediction Dataset |
| :-------------: | :---------------: | :-------------------------: |
|    80.5%        | Accuracy          | 65.4%                       |
|    88.8%        | Recall            | 65.4%                       |
|    90.8%        | Precision         | 67.6%                       |
|    88.7%        | F1 - Score        | 64.5%                       |
|    87.7%        | Balanced Accuracy | 66%                         |


## Application Development

The last and largest step is to create the web application itself. This consists of three main pilars, as we can see in the repository folders. First, we have the models that we created using the [Pickle](https://docs.python.org/3/library/pickle.html)
library in Python. Next, we had to make some templates for the different pages that our application will have. The total of them is six (6) and they were made using simple **HTML**, **CSS** and **JavaScript** and are available in
this repository. For the last part, the back-end development, we used Flask which is ideal for small applications with simple functions like this one. 








