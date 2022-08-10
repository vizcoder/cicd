FROM python:3.6

WORKDIR /opt/program

COPY requirments.txt .

RUN pip install -r requirments.txt

COPY src /opt/program


# docker run --gpus all --rm -it -v "$(pwd)/localhost/Data_Folder:/opt/ml" -p 5000:5000 cicd_testing_api /bin/bash 
#docker run -p 5000:5000  cicd_testing_api python app.py
#docker build -t cicd_testing_api .


#dckr_pat_zInsTWyMi8ynW0R7KbvXBoIPt1k