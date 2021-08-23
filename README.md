# Game Rating Predictor

<b> Greek Board Game Review Predictor </b>

The goal of this project is to predict a rating for a given Comment in between 1 to 10 . The model Used here is Multinomial Naive Bayes, Ridge Classifier  and Logistic Regression.

The dataset is availabe at https://www.kaggle.com/jvanelteren/boardgamegeek-reviews/metadata. This dataset contains more than 15M reviews about the game.

<b> Requirements </b><br>
-Pandas<br>
-Numpy<br>
-Scikit<br>
-sklearn<br>
-nltk<br>
-matplotlib<br>
-joblib<br>
-Collection<br>
Note: I have used python 3.7.9

Deploy:
I have created a flask application and deploy it on ibm cloud. I have already uploaded the app.py and requirement.txt as well procfile and pip file.<br>
DM-Project contains all related files.<br>
For deployment on ibmcloud:
First you have create account on ibm cloud<br>
open command prompt and type cf login -a https://api.ng.bluemix.net/ and it ask your credentials for ibm cloud<br>
the command is cf push appname -m 128M. It generates a link appname.mybluemis.net .<br>
<b>Note: ibm cloud allowed only 2 apps at a time on the free basis.<b>
<b> Note: You have to give an unique name for your app </b>
