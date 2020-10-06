
import os
import pandas as pd
import sqlalchemy as db
from sqlalchemy import Column, Float, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#hoe de strings in de class te verwerken? (heb ze nu in de create_tb functie gezet maar staat er erg lelijk vind ik
# strings = ["Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D", "Contract_Valid_Until"]

    class DBUTIL:

    def __init__(self):
        db_loc = os.environ['DB_LOC']
        self.engine = db.create_engine
        self._reflect()

    def create_tb(self, table_name, column_names):
        conn = self.engine.connect()
        self._reflect()
        trans = conn.begin()
        strings = ["Name", "Preferred_Foot", "Work_Rate", "Position", "Work_Rate_A", "Work_Rate_D",
                   "Contract_Valid_Until"]
        columns = (Column(name, String(32), quote=False) if name in strings else Column(name, Float, quote=False) for name in column_names)
        v_table = Table(table_name, self.Base.metadata, Column('id', Integer, primary_key=True, autoincrement=True),
                        extend_existing=True, *columns)
        v_table.create(self.engine, checkfirst=True)
        trans.commit()

    def drop_tb(self, table_name):
        conn = self.engine.connect()
        trans = conn.begin()
        self._reflect()
        v_table = self.Base.metadata.tables[table_name]
        v_table.drop(self.engine, checkfirst=True)
        trans.commit()

    def add_data_records(self, table_name, records):
        self._reflect()
        v_table = self.Base.metadata.tables[table_name]
        query = db.insert(v_table)
        connection = self.engine.connect()
        trans = connection.begin()
        connection.execute(query, records)
        trans.commit()

    def read_data_records(self, table_name):
        self._reflect()
        v_table = self.Base.metadata.tables[table_name]
        connection = self.engine.connect()
        trans = connection.begin()
        query = db.select([v_table])
        df = pd.read_sql_query(query, con=connection)
        trans.commit()
        return df

    def _reflect(self):
        self.Base = declarative_base()
        self.Base.metadata.reflect(self.engine)

# engine = sqal.create_engine('sqlite:///trainingdata.db', echo=True)
#
#
# Base = declarative_base()
# Base.metadata.reflect(engine)
#
# def create_tb(table_name, column_names):
#     conn = engine.connect()
#     trans = conn.begin()
#     columns = (Column(name, String(32), quote=False) if name in strings else Column(name, Float, quote=False) for name in column_names)
#     v_table = Table(table_name, Base.metadata, Column('ID', Integer, primary_key=True, autoincrement=True),
#                     extend_existing=True, *columns)
#     v_table.create(engine, checkfirst=True)
#     trans.commit()
#
# def drop_tb(table_name):
#     conn = engine.connect()
#     trans = conn.begin()
#     v_table = Base.metadata.tables[table_name]
#     v_table.drop(engine, checkfirst=True)
#     trans.commit()
#
# def add_data_records(table_name, records):
#     v_table = Base.metadata.tables[table_name]
#     query = sqal.insert(v_table)
#     connection = engine.connect()
#     trans = connection.begin()
#     connection.execute(query, records)
#     trans.commit()
#
# def read_data_records(table_name):
#     v_table = Base.metadata.tables[table_name]
#     connection = engine.connect()
#     trans = connection.begin()
#     query = sqal.select([v_table])
#     df = pd.read_sql_query(query, con=connection)
#     trans.commit()
#     return df