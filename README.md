# Siren_detection_with_ANN

### Is's a college mini porject done by group of three people including myself.

We trained a model for audio classification which uses normalised mfcc features to training and predictions

### We have done ANN model rather than a CNN model for two reason
  1: CNN models are very complex and hard to train and it takes a lot of time and computing power <br>
  2: Where for ANN a single vector of fecatures is enough for the training and prediction and it is the fatstest of two 


### On accuracy CNN has the upper hand but as for our Siren dectection ANN does the job pretty well.

## How to run it:

### Make sure you have these modules on your machine:

`tensorflow` <br>
`librosa` <br>
`tkinter` <br>
`pygame` <br>
`pandas` <br>
`numpy` <br>

### Step 1:
run the sirenApp.py file in your machine: <br>
a window will appear like this <br>
![intial window](./img/empty.png) <br>

### Step 2: <br>
Click the add button <br>
![after add button](./img/add.png) <br>
### Step 3: <br>
click on any sound file in the menu and click play <br>
if it is a siren the out will display **siren** <br>
![siren](./img/play_siren.png) <br>
else the out put will be **not a siren** <br>
![not a siren](./img/play_no_siren.png) <br>
