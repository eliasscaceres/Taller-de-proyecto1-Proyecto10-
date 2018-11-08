from flask import Flask
from flask import render_template
from flask import request
from models import Events
import random
import signal
from database import Database
import time 
# Metodo que genera los valores para las muestras
def getrand():
	semaphore_state = True
	return semaphore_state

class GracefulKiller:
	kill_now = False
	def __init__(self):
		signal.signal(signal.SIGINT, self.exit_gracefully)
		signal.signal(signal.SIGTERM, self.exit_gracefully)

	def exit_gracefully(self, signum, frame):
		self.kill_now = True

def main(session):
    killer = GracefulKiller()
    while(True):
        s_state = getrand()
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