from sqlalchemy import create_engine

# Database connection string format for MySQL
# Dialect+Driver://Username:Password@Host:Port/Database
database_url = "mysql+mysqlconnector://username:password@remote_host:3306/your_database"

# Create an engine
engine = create_engine(database_url)

# Connect to the database
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM your_table LIMIT 5")
    for row in result:
        print(row)
