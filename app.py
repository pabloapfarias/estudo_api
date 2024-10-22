from flask import Flask, jsonify, request
import psycopg as pg

app = Flask(__name__)

# Função auxiliar para abrir a conexão com o banco de dados
def get_db_connection():
    conn = pg.connect(
                       dbname='alvorapido', 
                       user='alvorapido_owner', 
                       password='TqJ6Gx3lHdBM', 
                       host='ep-flat-fog-a5ijafb1.us-east-2.aws.neon.tech', 
                       port=5432)
    
    return conn

@app.route('/top10wta', methods=['GET'])
def top10wta():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('SELECT * FROM usuarios;')
    users = cur.fetchall()

    cur.close()
    conn.close()

    
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)