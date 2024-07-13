import os 
from transformers import AutoProcessor,BlipForConditionalGeneration
from PIL import Image 
from gtts import gTTS 
from playsound import playsound 




class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename
        self.captions= None

    def predict(self):
        #load_model
        model= BlipForConditionalGeneration.from_pretrained("model/model_withbin")#yaha pr saved model ki file ki location deni h 
        processor=AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base") # ye wese ka wese hi rehne de
        print("process has been successfully completed image ")
        img = Image.open(self.filename)
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs)
        captions=processor.decode(out[0], skip_special_tokens=True)
        self.captions=captions
        return captions
    def Play(self,captions):
        if os.path.exists('static/audio/2.mp3'):
            os.remove('static/audio/2.mp3')
        myobj=gTTS(text=captions, lang='en', slow=False)
        audio_path = os.path.join(os.path.dirname(__file__), 'static/audio/2.mp3')
        myobj.save(audio_path)