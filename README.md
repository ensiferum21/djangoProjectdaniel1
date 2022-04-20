# theblog
-----
[Requirements for the project]
-----
pip must be installed to use the pip command
see
[link]https://pip.pypa.io/en/stable/installation/

regarding the face_recognition package the Numpy and Scipy packages are installed first then cmake is to be installed secondly then dlib then finally face_recognition
using the pip install in the command terminal

The pycharm editor 2021 2.3 was used
_____
make sure database is migrated before running server(commands shown below):

python manage.py makemigrations ,
python manage.py migrate
----------
The command shown below can be used to create an admin account to configure the website:
python manage.py createsuperuser 
-------

If conda is installed in system, to download the face_recognition do this steps:
conda create -n py36 python=3.6
activate py36
conda config --add channels conda-forge
conda install numpy
conda install scipy
conda install dlib
pip install --no-dependencies face_recognition

If any problems with face recognition problem look:
Source: [link]https://stackoverflow.com/questions/56696940/how-to-install-face-recognition-module-for-python
------- 
-------
asgiref==3.5.0
click==8.0.4
cmake==3.22.3
colorama==0.4.4
Django==4.0.3
dlib==19.23.1
face-recognition==1.3.0
face-recognition-models==0.3.0
numpy==1.22.3
Pillow==9.0.1
sqlparse==0.4.2
tzdata==2021.5

-------
