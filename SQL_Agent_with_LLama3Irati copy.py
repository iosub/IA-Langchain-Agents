from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())
db.run("SELECT * FROM Artist LIMIT 10;")

from langchain_community.llms import Ollama

llm = Ollama(model = "llama3")#,temperature=0.2)
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
print(db.dialect)
print(db.get_usable_table_names())

db.run("SELECT * FROM Artist LIMIT 10;")
#qwen2:latest 
for chunk in llm.stream("Hi how are you?"):
    print(chunk, end = "")

from langchain_community.utilities import SQLDatabase

#conn_str = "mssql+pyodbc://gg:ostia@minipc/iatest?driver=ODBC+Driver+17+for+SQL+Server"
conn_str = "mssql+pyodbc://gg:ostia@minipc/MSPLITEPRO_v3gg?driver=ODBC+Driver+17+for+SQL+Server"

#conn_str = "mssql+pyodbc://gg:ostia@minipc/korta?driver=ODBC+Driver+17+for+SQL+Server"

q="Cual ha sido las ventas del año pasado a los clientes"
q="Cual ha sido las ventas por año  a los clientes. Muéstrame el resultado en Json"
q="Cuál ha sido el cliente al que más le he vendido"
q="Cuál ha sido el artículo que pasa vendido"
q="Para la empresa con codigo 1, que TIPOREG=CF en la tabla de T_ORDTER. Qué necesidades tengo de de compra para los artículos el 21 de diciembre del 2020"
q="Para la empresa con codigo 1,  Qué necesidades de compra de cantidad de artículos tengo el 21 de diciembre del 2020, Teniendo en cuenta los pedidos que estan en la tabla T_ORDTER con TIPOREG=CF y su stock que esta en la tabla T_STOCKS"
q="Para la empresa con codigo 1,  Qué necesidades de compra de cantidad de artículos tengo el 21 de diciembre del 2020, Teniendo en cuenta los pedidos que estan en la tabla T_ORDTER con TIPOREG=CF, su stock que esta en la tabla T_STOCKS y las ordenes de fabricacion que estan en T_ORDFAB y T_ORDFABM con TIPOREG=F" 
q="Cuántos Clientes hay?"
q="Cuántos Clientes hay con El nombre que contenga ELDU ?"
#q="Cuántas facturas hay"
#db = SQLDatabase.from_uri(conn_str) #("sqlite:///Chinook.db")
#def __init__(
 #       self,
 #       engine: Engine,
 #       schema: Optional[str] = None,
 #       metadata: Optional[MetaData] = None,
 #       ignore_tables: Optional[List[str]] = None,
 #       include_tables: Optional[List[str]] = None,
 #       sample_rows_in_table_info: int = 3,
 #       indexes_in_table_info: bool = False,
 #       custom_table_info: Optional[dict] = None,
 #       view_support: bool = False,
 #       max_string_length: int = 300,
 #       lazy_table_reflection: bool = False,
 #   ):
 #       metadata: Optional[MetaData] = None,
 #       ignore_tables: Optional[List[str]] = None,
 #       include_tables: Optional[List[str]] = None,
 #       sample_rows_in_table_info: int = 3,
 #       indexes_in_table_info: bool = False,
 #       custom_table_info: Optional[dict] = None,
 #       view_support: bool = False,
 #       max_string_length: int = 300,
 #       lazy_table_reflection: bool = False,

#tables=["T_FACTURAS","T_CLIENTES","T_EMPRESA"]
#db111 = SQLDatabase.from_uri(conn_str,include_tables=tables,sample_rows_in_table_info = 0 )
db = SQLDatabase.from_uri(conn_str,sample_rows_in_table_info = 2)#,lazy_table_reflection=True)

#db = SQLDatabase.from_uri("sqlite:///chinook.db", sample_rows_in_table_info = 3)
db.get_usable_table_names()

print(db.table_info)

from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType

print(db.table_info)


#agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True,stream_runnable=False,handle_parsing_errors=True)
#agent_executor = create_sql_agent(llm, db=db, agent_type="tool-calling", verbose=True, stream_runnable=False)
#agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True,handle_parsing_errors=True)
#agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True, stream_runnable=False ,handle_parsing_errors=False)


#agent_executor.invoke("How many different Artists are in the database?")
#print(agent_executor.agent.runnable.get_prompts()[0].messages[0].content)
#agent_executor.invoke(q,handle_parsing_errors=True,include_run_info=True)
agent_executor.invoke(q)
#agent_executor.invoke("How many Artists are in the database?")
