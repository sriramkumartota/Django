import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


#Fake script

import random
from first_app.models import Topic,webpage,Records
from faker import Faker

fakegen= Faker()
topics = ['social','polotical','environmental']

def add_topic():
    t= Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t 

def populate(N=5):

    for entry in range(N):

        #topic for entry
        top = add_topic()

        #creation of fake entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #New webpage entry
        webpg = webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #Fake entry for  the record
        Rec = Records.objects.get_or_create(webpage =webpg,date = fake_date)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("Populated")

