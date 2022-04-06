
#https://www.youtube.com/watch?v=xaDJ5xnc8dc&ab_channel=Pythoholic -- to check how to install the face-recognition if pip fails

# install Cmake , then dlib and then face_recognition installed using pip in terminal {IN ORDER}

#https://github.com/ntshvicky/face-similarity/blob/master/face_similarity.py
import face_recognition
from pathlib import Path
from PIL import Image
import os
from django.conf import settings

def compare_faces(image1):
    from django.core.files.storage import default_storage

    filename = "temporary_image.png"  # received file name
    tmp_file = os.path.join(settings.MEDIA_ROOT, 'tmp/' + filename)

    with default_storage.open('tmp/' + filename, 'wb+') as destination:
        for chunk in image1.chunks():
            destination.write(chunk)


    # Load the image of the person we want to find similar people for
    known_image = face_recognition.load_image_file(tmp_file)

    # Encode the known image
    try:
        known_image_encoding = face_recognition.face_encodings(known_image)[0]
    except IndexError:
        return IndexError
    # Variables to keep track of the most similar face match we've found
    best_face_distance = 1.0
    best_face_image = None
    fd_array = [] ## created to obtain smallest distance of face

    # Loop over all the images we want to check for similar people


    file = os.path.join(settings.MEDIA_ROOT, 'images/profile')

    for image_path in os.listdir(file):
        # Load an image to check
        unknown_image = face_recognition.load_image_file(file+"\\"+image_path)

        # Get the location of faces and face encodings for the current image
        face_encodings = face_recognition.face_encodings(unknown_image)


        # Get the face distance between the known person and all the faces in this image
        face_distance = face_recognition.face_distance(face_encodings, known_image_encoding)[0]


        fd_array.append(face_distance)


        # If this face is more similar to our known image than we've seen so far, save it
        if face_distance < best_face_distance:
            # Save the new best face distance
            best_face_distance = face_distance

        fd_array.sort()
        threshold=fd_array[0]


    if(threshold>0.6): # the threshold was set to 0.6 if higher its different person
        print("Different person!")
        print("lowest face distance",threshold)
        return True
    else:
        print("Same person!!")
        print("lowest face distance",threshold)

        return False

