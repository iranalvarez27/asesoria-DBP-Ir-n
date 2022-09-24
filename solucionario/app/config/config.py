class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/asesoria'       # dialecto + dbapi
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = './static/img/'
    MAIL_SERVER= 'smtp.gmail.com'
    MAIL_DEBUG = True
    MAIL_USERNAME= 'dbpcorreoprueba@gmail.com'
    MAIL_PASSWORD= 'Utecdbp12345'
    MAIL_DEFAULT_SENDER= 'dbpcorreoprueba@gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL=True
    MAIL_USE_TLS=False
    GOOGLE_CLIENT_ID = '59012120039-54jvcg23a2met0bl2oheigt0sfrdn9mu.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = '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'