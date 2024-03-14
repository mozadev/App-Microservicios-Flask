from application import create_app, db
from application import models
from flask_migrate import Migrate

app = create_app()

migrate = Migrate(app, db) # define the migration object

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 7001)
     

