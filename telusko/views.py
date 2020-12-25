from django.shortcuts import render,HttpResponse
from .models import Destination
from .models import Business
from .models import Intro
from .models import Demo
def index (request):
    dest1 = Destination()
    dest1.name ='Machine Xtreme'
    dest1.price = '700'
    dest1.desc = 'Here you will find the perfect good luck messages for new business and entrepreneurs to wish and congratulate your dear person.'
    dest1.review = 'Start where you are'
    dest1.review2 = 'Use what you have'
    dest1.img = 'c.jpg'
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Machine Xtreme'
    dest2.price = '300'
    dest2.desc = 'Here you will find the perfect good luck messages for new business and entrepreneurs to wish and congratulate your dear person.'
    dest2.review = 'Start where you are'
    dest2.review2 = 'Use what you have'
    dest2.img = 'c2.jpg'
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Machine Xtreme'
    dest3.price = '500'
    dest3.desc = 'Here you will find the perfect good luck messages for new business and entrepreneurs to wish and congratulate your dear person.'
    dest3.review = 'Start where you are'
    dest3.review2 = 'Use what you have'
    dest3.img = 'c3.jpg'
    dest3.offer = True

    dest4 = Destination()
    dest4.name = 'Machine Xtreme'
    dest4.price = '700'
    dest4.desc = 'Here you will find the perfect good luck messages for new business and entrepreneurs to wish and congratulate your dear person.'
    dest4.review = 'Start where you are'
    dest4.review2 = 'Use what you have'
    dest4.img = 'c.jpg'
    dest4.offer = True

    dests = [dest1,dest2,dest3,dest4]

    comp = Business()
    comp.title = 'We provide all custom web based services.'
    comp.point1 = 'So many books, so little time.'
    comp.point2 = 'So many books, so little time.'
    comp.para = 'Two things are infinite: the universe and human stupidity and i am not sure about the universe'

    start = Intro()
    start.title = 'Be willing to be a beginner every single morning.'
    start.author = 'Tareq Hasan - CEO'
    start.mission = 'Start where you are. Use what you have. Do what you can.'
    start.vision = 'Your goal should be just out of reach. But not out of sight.'

    demmo1 = Demo()
    demmo1.title = 'Web Development'
    demmo1.paragraph = 'Our Hotel management system provides you the room service management system, hotel restaurant catering system, hotel room booking system and other hotel amenities with complete web automation solution.'
    demmo2 = Demo()
    demmo2.title = 'School Management'
    demmo2.paragraph = 'Our School management system manage the day-to-day administrative tasks of schools. It schools to digitally monitor the daily activities along with managing all the resources and information on a single platform. We have also integrated student performance analysis using AI.'
    demmo3 = Demo()
    demmo3.title = 'Inventory System'
    demmo3.paragraph = 'We provide inventory system software for warehouse management, fleet management and supply chain management at one stack.'

    demmos = [demmo1,demmo2,demmo3]


    return render(request, 'index.html', {'dests': dests, 'comp': comp, 'start':start, 'demmos':demmos})
