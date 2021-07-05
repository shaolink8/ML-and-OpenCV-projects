# Implementation of ML algorthims for use cases like classification and clustering using various practical models.

<i>There are a lot of interesting examples below which you can tweak with a dataset of your own, with your own labels or number of classifiers and look at how the results change, and perhaps come up with a new model on your own.</i>

### Decision Tree and Random Forest

- Coin Classification - using these classifiers to classify an input image into either a "1", "2", "5" or "10" rupee coin<br>
The dataset includes a total of 118 1-rupee-coin images, 126 2-rupee-coin images and 240 5-rupee-coin images and 131 10-rupee-coin images<br>
75% data was used for training and 25% for testing<br>
In the code, we provided 2 images as an input to the model

- Scene Classification - using these classifiers to classify an input image into "coast", "forest", "street" or "highway"<br>
The dataset includes a total of 1240 images, 75% of which were used for training and 25% for testing<br>
In the code, we provided 10 images as an input to the model

- Signboard Classification - using these classifiers to classify an input image into classic road signs such as "left turn", "no parking", "right turn", "school ahead", "slow", "speedbreaker", "stop signal", "uturn", "Zebra".<br>
The dataset includes a total of 19, 18, 16, 23, 22, 19, 26, 16 and 22 images respectively, 75% of which were used for training and 25% for testing<br>
In the code, we have provided 3 images as an input to the model

### Linear SVM 

- Material Classification - using this classifier to classify an input image into either "carpet", "laminate-flooring", "tablecloth" or "wallpaper"<br>
The dataset includes a total of 16 images and the testing data includes 4 images

### Spatial Algorithms

<i>using scipy.spatial</i>

- Distance between Query Image and Input Image - 4 dino images have been provided, 1 of which is chosen as the query image and the rest are then given as input.<br>
First, the code extracts the mean and standard deviation from each channel of the BGR image, then updates the index with the feature vector<br>
At last, it computes the Euclidean distance between the query image

### KNN Classifier

- Identifying handwritten single digits in an image, tested against 5 inputs

### k-Means Clustering

- An attempt at clustering a given dataset into 2 clusters ( change the code and number of clusters in however way you want to experiment it ) <br>
The dataset in this example includes images of Antelope Canyon and Grand Canyon.

### Logistic Regression 

- Plotting of Step Function and Sigmoid
- Using Logistic Regression to predict a famous personality's name from an input image, 10 input images are provided and tested

### SVM

- Featuring comparison between Linear Kernel and Polynomial Kernel

### ABR - Vision_Basics

All the codes here are opencv projects for starters, which can better be combined and streamlined for a working application that assists lives.
