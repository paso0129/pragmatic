FROM python:3.8.7

WORKDIR /home/

RUN git clone https://github.com/paso0129/pragmatic.git

WORKDIR /home/pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-t3#wmc_b-s6(49$-=4!xxkgeex679o-_g*zw_6$+ng6(&@%847" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py","runserver","0.0.0.0:8000"]
