#!/usr/bin/python
import keras_ocr
import sys

if __name__ == "__main__":
    image_filepath = sys.argv[0]
    
    recognizer = keras_ocr.recognition.Recognizer()
    recognizer.compile()    
    recognizer.model.load_weights('./assets/dataset/trained_recognizer.h5')
    predicted = recognizer.recognize(image_filepath)
    print(" prediction:",predicted)
