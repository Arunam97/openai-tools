import os
from neo4j import GraphDatabase
import pandas as pd
from sqlalchemy import create_engine

def execute_mysql_query(query, database):
    """
    Executes an SQL query on a specified MySQL database.

    Args:
    query (str): The SQL query to be executed.
    database (str): The name of the database to execute the query against.

    Returns:
    list: A list of dictionaries containing the query results.
    str: An error message if an exception occurs.
    """
    # Hardcoded connection details
    user = 'root'
    password = 'qwerty'
    host = 'localhost'
    port = 3306

    # Create the connection string
    connection_string = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}'

    try:
        # Create the SQLAlchemy engine
        engine = create_engine(connection_string)
        
        # Execute the query
        df = pd.read_sql_query(query, engine)
        
        # Convert the result to JSON
        result_json = df.to_json(orient='records')
        
        return result_json
    
    except Exception as e:
        return str(e)
    
def execute_cypher_query(query):
    """
    Executes a Cypher query on the Neo4j database.

    Args:
    query (str): The Cypher query to be executed.

    Returns:
    list: A list of dictionaries containing the query results.
    str: An error message if an exception occurs.
    """
    NEO4J_URI = "neo4j+ssc://ae9fac9e.databases.neo4j.io"
    NEO4J_USER = "neo4j"
    NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")

    try:
        # Connect to the Neo4j database
        driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
    except Exception as e:
        return str(e)
    
    try:
        # Open a session
        with driver.session() as session:
            # Execute the Cypher query
            result = session.run(query)
            
            # Collect the results
            results = [record.data() for record in result]
            return results
    
    except Exception as e:
        print("An error occurred while executing the query or collecting results:", e)
        return str(e)
    
    finally:
        driver.close()

def test_function(input_string):
    result_string = "123" + input_string + "123"
    return {"input_string": input_string, "result_string": result_string}

def get_order_details(order_number):
    orders_db = {
        "ORD123": {"location": "New York", "delivery_date": "2024-08-15"},
        "ORD124": {"location": "Los Angeles", "delivery_date": "2024-08-16"},
        "ORD125": {"location": "Chicago", "delivery_date": "2024-08-17"}
    }
    
    # Fetch order details
    order_details = orders_db.get(order_number, None)
    
    if order_details:
        return {"location": order_details["location"], "delivery_date": order_details["delivery_date"]}
    else:
        return {"error": "Order not found"}

def get_temperature(city_name):
    weather_db = {
        "New York": {"temperature": "25°C"},
        "Los Angeles": {"temperature": "30°C"},
        "Chicago": {"temperature": "22°C"}
    }
    
    # Fetch temperature
    temperature_details = weather_db.get(city_name, None)
    
    if temperature_details:
        return {"temperature": temperature_details["temperature"]}
    else:
        return {"error": "City not found"}
