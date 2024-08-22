from fastai.vision.all import load_learner
import gradio as gr

#--Below 3 line of code should be uncommented when deploying gradio app / run app.py in terminal
#import pathlib
#temp=pathlib.PosixPath
#pathlib.PosixPath=pathlib.WindowsPath


jersey_labels=[
    'AC Milan Jersey',
    'Arsenal Jersey',
    'Atletico Madrid Jersey',
    'Barcelona Jersey',
    'Bayern Munich Jersey',
    'Borussia Dortmund Jersey',
    'Chelsea Jersey',
    'FC Porto Jersey',
    'Inter Milan Jersey',
    'Juventus Jersey',
    'Leeds United Jersey',
    'Liverpool Jersey',
    'Manchester City Jersey',
    'Manchester United Jersey',
    'Napoly Jersey',
    'Newcastle Jersey',
    'PSG Jersey',
    'Real Madrid Jersey',
    'Southampton Jersey',
    'Tottenham Jersey'
]

model=load_learner("jersey-recogniser-v2.pkl")

def recognize_image(image):
  #import pdb;pdb.set_trace()
  pred,idx,probs=model.predict(image)
  print(pred)
  return dict(zip(jersey_labels, map(float,probs)))

image = gr.Image()
label = gr.Label()
examples = [
   "Test_images/Test_image1.jpg",
   "Test_images/Test_image2.jpg",
   "Test_images/Test_image3.jpg",
   "Test_images/Test_image4.jpg"]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label,examples=examples)
iface.launch(inline=False,share=True)