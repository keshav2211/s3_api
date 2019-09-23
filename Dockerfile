FROM python

ADD . / /usr/share/s3_api/
ADD config_container.py /usr/share/s3_api/config.py

RUN pip install -r /usr/share/s3_api/requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "/usr/share/s3_api/app.py"]