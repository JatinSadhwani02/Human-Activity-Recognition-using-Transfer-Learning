# Importing all necessary libraries
import cv2
import os
from keras.models import load_model
from keras.preprocessing.image import load_img , img_to_array
from keras.preprocessing import image
import numpy as np
import shutil
import glob
from flask import Flask, redirect, url_for, request, render_template
from tensorflow.keras.models import load_model
import random
import pymysql


app = Flask(__name__)
model_path = 'human_activity_recognition_95_95.h5'
model = load_model(model_path)



def Preprocess_video(videopath,save):

    labels = {'Archery': 0,
    'Beatboxing': 1,
    'Blowing Out Candles': 2,
    'Bouncing On Trampoline': 3,
    'Breakdancing': 4,
    'Brushing Hair': 5,
    'Canoeing or Kayaking': 6,
    'Capoeira': 7,
    'Cartwheeling': 8,
    'Catching or Throwing Baseball': 9,
    'Celebrating': 10,
    'Cheerleading': 11,
    'Chopping Wood': 12,
    'Cooking Sausages': 13,
    'Dancing Macarena': 14,
    'Deadlifting': 15,
    'Dribbling Basketball': 16,
    'Driving Car': 17,
    'Eating Cake': 18,
    'Exercising With an Exercise Ball': 19,
    'Feeding Birds': 20,
    'Finger Snapping': 21,
    'Hammer Throw': 22,
    'Headbanging': 23,
    'High Jump': 24,
    'Ice Climbing': 25,
    'Kitesurfing': 26,
    'Laughing': 27,
    'Making Pizza': 28,
    'Milking Cow': 29,
    'Opening Present': 30,
    'Paragliding': 31,
    'Playing Flute': 32,
    'Playing Keyboard': 33,
    'Roller Skating': 34,
    'Shoveling Snow': 35,
    'Side Kick': 36,
    'Slacklining': 37,
    'Snowboarding': 38,
    'Snowmobiling': 39,
    'Stretching Leg': 40,
    'Swinging On Something': 41,
    'Throwing Ball': 42,
    'Watering Plants': 43,
    'Welding': 44}





    key = list(labels.keys())
    value = list(labels.values())


    # Read the video from specified path
    cam = cv2.VideoCapture(videopath)
    # model=load_model('human_activity_recognition.h5')

    try:

        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
            
        if os.path.exists('data'):
            shutil.rmtree("data")
            os.makedirs('data')

    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')

    # frame
    currentframe = 100

    while(True):

        # reading from frame
        ret,frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = 'data/frame' + str(currentframe) + '.jpg'

            # writing the extracted images
            cv2.imwrite(name, frame)




            img=image.load_img(name,target_size=(224,224))
            x=image.img_to_array(img)
            x=x/255
            x=np.expand_dims(x,axis=0)
            pred = np.argmax(model.predict(x)[0], axis=-1)

            pos = value.index(pred)
            lab = key[pos]

            img = cv2.imread(name)
            img = cv2.putText(img, lab, (18, 70), cv2.FONT_HERSHEY_SIMPLEX, 
                       2, (255,0,0), 3, cv2.LINE_AA)

            cv2.imwrite(name, img)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()
    
    print("Frames creation successfully done.......")
    print("Video is preprocessing.......")
    
    img_array = []
    for filename in glob.glob('data/*.jpg'):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)


    out = cv2.VideoWriter(f'result/{save}.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    
    return f"Your result is ready {save}.avi"




@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')




@app.route('/feedback',methods=['GET'])
def feedback():
    return render_template('feedback.html')

@app.route('/predict',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        img = request.form.get("file")
        
        if os.path.exists(img):
            save = random.randint(1, 10000000)
            pred = Preprocess_video(img , save) # return index
            return pred
        else:
            return "You entered incorrect path"
    return None 




@app.route("/feedback_us",methods=['GET','POST'])
def feedback_us():
	if (request.method=='POST'):
		name=request.form.get('name')
		contactno=request.form.get('contactno')
		msg=request.form.get('msg')

		if name=="" or msg=="":
			flash("Please fill all fields and correct fields")
			return render_template("feedback.html")
		elif len(contactno)>10 or len(contactno)<10:
			flash("Please fill correct contact number")
			return render_template("feedback.html")
		else:
			con=pymysql.connect(host='localhost',user='root',password='',database='human_activity_recognition')
			cur=con.cursor()
			cur.execute('insert into feedback values(%s,%s,%s)',(name,contactno,msg))
			con.commit()
			con.close()
			return render_template("index.html")


app.run(debug=True)
