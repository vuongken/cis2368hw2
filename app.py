from flask import Flask, request, jsonify
from sql import DBconnection, execute_query, execute_read_query
from creds import myCreds

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/api/zoo', methods=['GET'])
def get_animals():
    conn = DBconnection()
    if conn:
        sql = "SELECT * FROM zoo"
        results = execute_read_query(conn, sql)
        conn.close()
        return jsonify(results)
    return jsonify({"error": "DB connection failed"}), 500

@app.route('/api/zoo', methods=['POST'])
def add_animal():
    data = request.get_json()
    conn = DBconnection()
    if conn:
        sql = """
            INSERT INTO zoo (domain, kingdom, class, species, age, animalname, alive)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['domain'], data['kingdom'], data['class'], data['species'],
            data['age'], data['animalname'], data['alive']
        )
        execute_query(conn, sql, values)
        conn.close()
        return jsonify({"message": "Animal added successfully"})
    return jsonify({"error": "DB connection failed"}), 500

@app.route('/api/zoo', methods=['PUT'])
def update_animal():
    data = request.get_json()
    conn = DBconnection()
    if conn:
        sql = "UPDATE zoo SET alive = %s WHERE id = %s"
        values = (data['alive'], data['id'])
        execute_query(conn, sql, values)
        conn.close()
        return jsonify({"message": "Animal updated successfully"})
    return jsonify({"error": "DB connection failed"}), 500

@app.route('/api/zoo', methods=['DELETE'])
def delete_animal():
    data = request.get_json()
    conn = DBconnection()
    if conn:
        sql = "DELETE FROM zoo WHERE id = %s"
        values = (data['id'],)
        execute_query(conn, sql, values)
        conn.close()
        return jsonify({"message": "Animal deleted successfully"})
    return jsonify({"error": "DB connection failed"}), 500

if __name__ == '__main__':
    app.run()