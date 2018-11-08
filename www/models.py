import datetime

from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.types import Float
from sqlalchemy.types import Boolean

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# Clase correspondienta a una muestra, que tiene como atributos las distintas variables climaticas
class Events(Base):
    __tablename__ = 'events'
    id=Column(Integer, primary_key=True)
    semaphore_state=Column('semaphore_state', Boolean)
    
    def serialize(self):
    		return {
    				'id' : self.id,
    				'semaphore_state' : self.semaphore_state,

    		}
 