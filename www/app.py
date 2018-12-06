# Import de librerias
from flask import Flask
from flask import render_template
from aux_pro import Process
from database import Database
from flask import redirect
from flask import jsonify
from flask import request
import datetime
import os

app = Flask(__name__)
db = Database()
pro = Process()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
# Ruta inicial
@app.route('/',methods=["GET"])
# Metodo inicial
def index():
	if not pro.is_running():
		pro.start_process()
		print("Empezando process ")

	return last_10_events()
# Metodo que retornan los ultimos 10 eventos 
def last_10_events():
	events=db.get_10_last_events()
	cant = len(events)
	if cant > 0:
		porc= percentage(events)
		return render_template('index.html',events=events,porc=porc)
	else:
		return render_template('index.html')
# Porcentaje de objetos que atravesaron el sensor infrarojo, con el semaforo en rojo.
def percentage(events):
	cant_true=0
	cant=len(events)
	for e in events:
		if e['semaphore_state']:
			cant_true=cant_true+1
	porc=(cant_true*100)/cant
	return porc

# @app.route('/eventsjson/',methods=["GET"])
# def get_events():
# 	events10=db.get_10_last_events()
# 	return jsonify(events10)	
	