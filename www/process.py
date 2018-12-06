from flask import Flask
from flask import render_template
from flask import request
from models import Events
import random
import signal
from database import Database
import time 
import urllib.request
# Metodo que busca en el servidor del ESP por nuevos eventos.
def getvalue():
    texto = urllib.request.urlopen("http://192.168.4.1").read()
    print (texto)
    if texto==b'71' :  
        semaphore_state=False
        # semáforo en verde cuando pasó un objeto
    elif texto==b'82':
        semaphore_state=True
        # semáforo en rojo cuando pasó un objeto
    else:
        return 3 
    return semaphore_state


class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, signum, frame):
		self.kill_now = True
# Funcion que guarda los eventos si tienen valores correctos.
def main(session):
    killer = GracefulKiller()
    while(True):
        s_state = getvalue()
        if s_state!=3:
            event = Events(semaphore_state=s_state)
            session.add(event)
            session.commit()
            print("Evento guardado ")
        time.sleep(1)
        # print x
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':
    db = Database()
    session = db.get_session()
    main(session)