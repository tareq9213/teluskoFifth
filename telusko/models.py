from django.db import models

class Destination:
    id: int
    name : str
    img : str
    desc : str
    price : int
    review: str
    review2: str
    offer: bool

class Business:
    title: str
    point1: str
    point2: str
    image: str
    para: str

class Intro:
    title: str
    mission: str
    vision: str
    author : str

class Demo:
    name: str
    paragraph: str



