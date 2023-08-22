from sqlalchemy import create_engine, text

db_connection_string = ""

engine = create_engine(db_connection_string, 
                       connect_args = {
                           "ssl" : {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       })

def get_posts():
    with engine.connect() as conn:
        # execute this query, which gives all objects in posts db 
        result = conn.execute(text("select * from posts"))
        # result is list of row objects
        # access each individual row of result with for loop
        # make row object into dictionary with row._mapping attribute 
        # return a list of dictionaries 
        posts = []

        for row in result:
            posts.append(row._mapping)

        return posts