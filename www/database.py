from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Events
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "proyecto10"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection
        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session

    # def init_samples(self):
    #     """Generate the samples in the database
    
    #     Returns:
    #         [id of samples] --
    #     """
    #     session = self.get_session()
    #     sample = Samples()
    #     session.add(sample)
    #     session.commit()
    #     sample_id = int(sample.id)
    #     session.close()     
    #     return sample_id
        # Si hay muestras en la base de datos, retorna la ultima, es decir la mas actual
    def get_event(self):
        session = self.get_session()
        event = session.query(Events).order_by(Events.id.desc()).first()
        session.close()
        if(event is not None):        
            return event.serialize()
        else:
            return []

        # Si hay 10 muestras o más, devuelve las ultimas 10, es decir las 10 mas recientes 
    def get_10_last_events(self):
        events=0
        session = self.get_session()
        events = session.query(Events).order_by(Events.id.desc()).limit(10).all()
        session.close()
        if(events!=0):        
            return [e.serialize() for e in events]
        else:
            return [] 