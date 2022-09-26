class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:202120074@localhost:5432/asesoria'   # dialecto + dbapi
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = './static/img/'