import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er #este permite exportar las imagenes
#Hay que ejecutar el command: python src/models.py
#Quizas haya que ejecutar el command: pipenv shell
#Tambien se puede hacer todo junto: pipenv run python src/models.py

Base = declarative_base()

#Ejemplos de tablas: Lo que esta dentro de los parentesis es la herencia
class Person(Base):
    __tablename__ = 'person' #Nombre de la tabla, siempre en minuscula
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True) #Una columna con el nombre "id", luego entre parentesis se pone que tipo de dato va a venir
    name = Column(String(250), nullable=False)#Columna con el nombre "name", el "nullable= False" es para poner la columna obligatoria

class Address(Base):
    __tablename__ = 'address' 
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250)) #Por defecto las columnas son nullable=True, osea que pueden quedar vacia
    post_code = Column(String(250), nullable=False) 
    person_id = Column(Integer, ForeignKey('person.id')) #se pone el nombre de la tabla (no de la clase) seguido del nombre del columna. En este caso queremos poner bajo la columna "person_id" de esta tabla, el ID de la OTRA tabla (person)
    person = relationship(Person) #Aca si va el nombre de la clase. Estas dos ultimas lineas de codigo son necesarias para que el guarde la relacion

    def to_dict(self):
        return {}
class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30))
    lastname = Column(String(30))
    email = Column(String(40), nullable=False, unique=True)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
