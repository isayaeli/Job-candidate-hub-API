### Job-candidate-hub-API

Follow these simple steps to initilize this project
  ## Installation
  
  1 clone repository from this https://github.com/isayaeli/Job-candidate-hub-API.git and then cd into project folder (Job-candidate-hub-AP)
  
  2 install virtual env
  
     -for linux = sudo pip install virtualenv or sudo apt-get  virtualenv
     -for windows =  pip install virtualenv
     -for mac = sudo pip3 install virtualenv
            
  3 create env
  
     -linux = virtualenv -p python3 env
     -windows = python -m venv env
     -for mac = virtualenv env_ -p python3
     
  4 activate virtual env
  
    -linux source venv/bin/activate
    -windows env\scripts\activate
    -mac source venv/bin/activate
       
  5 install depebencies
  
     -pip install -r requements.txt
  
  6 run project
  
    -python manage.py runserver
    
  7 open this link to access endpoints
  
    - http://localhost:8000/docs/
