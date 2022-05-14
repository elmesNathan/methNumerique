from flask import Flask
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = '9d2f712a62f692dcdfaadd06'

app.config['MYSQL_HOST'] = 'mysql-elmes.alwaysdata.net'
app.config['MYSQL_USER'] = 'elmes'
app.config['MYSQL_PASSWORD'] = 'mot2p@sse'
app.config['MYSQL_DB'] = 'elmes_data'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)