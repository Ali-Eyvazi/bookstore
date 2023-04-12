FROM python:slim
WORKDIR /home
COPY  . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 8000    
WORKDIR /home/bookstore/
CMD python manage.py runserver 0.0.0.0:8000