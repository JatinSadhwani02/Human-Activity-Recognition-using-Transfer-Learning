# Human-Activity-Recognition-using-Transfer-Learning

<h2>Unpreprocess kinetic 400 Dataset link:- https://deepmind.com/research/open-source/kinetics </h2>


<h2> Preprocess Dataset Link : https://drive.google.com/file/d/1Es0IpYDY3k71kz9FpW2p5AGbCIk5I_qu/view?usp=sharing </h2>

<h2> Download pretrained model : https://drive.google.com/file/d/11tqGeByuntORoOJe7KLtouUD-kGpLzLN/view?usp=sharing</h2>

Click on the preprocess dataset link. You will get Train_Test_video_classifier.zip file. After extract the datatset. You will get two folders training and validation. Both folders contain 45-45 category folders.

<h1>Training and Validation </h1>
<img src="images/one.png" alt="one" width="800" height="450">
<h1>Training folder contains 45 categories </h1>
<img src="images/two.png" alt="one" width="800" height="450">
<h1>Validation folder contains 45 categories </h1>
<img src="images/three.png" alt="one" width="800" height="450">

<h1> Introduction </h1>
Now in human activity recognition files's folder, You will get 5 files. Firstly we extract 15-15 videos's id, label, start time and end time of 45 category from thousands of videos's data, then we'll check that which video is private or which video is public. So we'll remove the private video's data and keep the public videos's data. And in preprocessing, we download videos of each category one by one then trim the video for 10 sec according to the start time and end time which is given in the training.csv file. Then we convert the videos into frames (images). Then move the images to a particular category folder and do for all the categories and make a training folder and move all category folders into it. And do same for the validation. The ratio of training and validation is 80:20. That means 80% data in the training and 20% data in the validation. After preparing the dataset, now we start the training of our model. After train the model for 70 epochs, you will get 90% accuracy on the training data and 91% accuracy on the validation data. Now it’s time for testing the model. We test a model on video to recognize the human activity. So for testing, we convert the video into frames then classify all the frames, then make a video with the help of all the frames. You will get all the process in the folder of human activity recognition files.

<h4>The steps for train the model and sequence for use the files are:-</h4>

1. Extract 15-15 Videos from training and validation.ipynb
2. Remove Private keep public.ipynb
3. Prepoccess_training_videos.ipynb
4. Prepoccess_validation_videos.ipynb
5. HUMAN_ACTIVITY_RECOGNIZTION_TRAINING.ipynb


<h3> Process to run file: </h3>

1. Extract 15-15 Videos from training and validation.ipynb : Change the name of the class when appending into the new dataframe. And simply save the training dataframe. You will get 675 data rows of 45 category. and do for same validation, You will get 675 data rows of 45 category. Then save the validation dataframe. 

2. Remove Private keep public.ipnyb : For remove the private and keep public video data, Just execute the loop from 0 to len(data). Then you will get all private videos's list. Then remove private videos and save the training dataframe and do for same as validation.

3. Prepoccess_training_videos.ipnyb: download one by one category videos which means download 15 videos in one time. Then trim all the videos. Then you will get the list of untrimmed video. Then again try to trim the remainig videos. Then convert the videos into the frames. For example- if you have 15 or less than 15 trimmed video of celebrating class then make a celebrating folder then convert all the trimmed videos into frames(images) then move all the frames into the celebrating folder and do all for same.

4. Prepoccess_training_videos.ipnyb: download one by one category videos which means download 15 videos in one time. Then trim all the videos. Then you will get the list of untrimmed video. Then again try to trim the remainig videos. Then convert the videos into the frames. For example- if you have 15 or less than 15 trimmed video of celebrating class then make a celebrating folder then convert all the trimmed videos into frames(images) then move all the frames into the celebrating folder and do all for same.


After doing 3rd and 4rd step, Make a zip file of complete data.

5. HUMAN_ACTIVITY_RECOGNIZTION_TRAINING.ipnyb : Copy data.zip file into Google colab which stores the training and validation folder and in each folder, 45 catefory folders are available and move all validation images to training, then training and inside training, 45 categories folders store total data. So divide data into training and validation. 80% data in training and 20% data in validation. This process done for divide the data into 80:20 ratio because we had the data of 50:50 ratio. Then simple execute remaining code to train the model.


<h3>Deployment using python's framework flask:-</h3>

<h4> There are four folders and two files you will get: </h4>

1. Static: Static folder store the JavaScript file, css file and images.
2. Template: Template folder store all web pages.
3. Test: Test folder store the testing videos.
4. Result: Result folder store the result video.
5. preprocess csv file dataset : This folder contain preprocess csv files.
6. Data: Data is a extra folder which is created at the running time, Data folder stores the video’s frames temporary.
7. Human_Activity_Recognition.py file is our python file.
8. Human_Activity_Recognition.h5 is our pre trained model to classify human activity in video.
9. human_activity_recognition.sql is a database for feedback. just import in the xampp or wampp server.


 You just simply run the Human_Activity_Recognition.py file then you will get a link like (http://127.0.0.1:5000) then copy and paste this ink into any browser. Then you can use the project.
 
<h3> Note : Make sure before running the project, see a hierarchy of project. You'll also setup like below image and for use the feedback form in project, You import the human_activity_recognition.sql file in xampp or wampp server. For importing (Go to new -> Create dataset with name (human_activity_recognition) -> click on import -> choose file -> choose human_activity_recognition.sql file -> click on Go-> Done </h3>

<h1> Flask application setup </h1>
<img src="images/fours.png" alt="one" width="800" height="450">


<h1>Overview of Deployement of Human Activity Recognition</h1>

<h1>Page 1 : Home</h1>
<img src="images/five.png" alt="one" width="800" height="450">

<h1>Page 2 : Home (remaining)</h1>
<img src="images/six.png" alt="one" width="800" height="450">

<h1>Page 3 : Feedback</h1>
<img src="images/seven.png" alt="one" width="800" height="450">

<video width="320" height="800" controls>
  <source src="result/1307489.avi" type="video/mp4">
</video>
