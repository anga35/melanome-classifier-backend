from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import cv2 as cv
import tempfile
from django.core.files.storage import default_storage
import pickle
import os
import numpy as np
from tensorflow import keras
# Create your views here.

class PredictImageView(APIView):

    def post(self,request):
        print(default_storage.location)
        file=request.FILES['sample'].file
        default_storage.save('temp.png',file)
        img=None
        with default_storage.open('temp.png') as mfile:
            img=cv.imread(mfile.name)
            img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
            img=img/255.0
            img=cv.resize(img,(224,224))
            img=np.expand_dims(img,axis=0)


        model=keras.models.load_model(os.path.join(default_storage.location,'ml_models','skin_model.h5'))

        result=model.predict(img)
        result=np.argmax(result)
        print(result)
        default_storage.delete('temp.png')
        return Response(result)

