from data_warga import *
from flask import Flask, request, jsonify


app = Flask(__name__)

#============== RESOURCE ============#



# resource get semua warga

@app.route('/api/v1/warga', methods=['GET'])
def warga():
    wargas = get_wargas()
    if wargas:
        return jsonify(wargas), 200  # Sukses dengan kode status 200
    else:
        return jsonify({'message': 'No users found.'}), 404


# resource get warga by id

@app.route('/api/v1/warga/<id_warga>', methods=['GET'])
def get_wargas_by_id(id_warga):
    return jsonify(get_warga_by_id(id_warga))


# resource tambah warga

@app.route('/api/v1/warga', methods=['POST'])
def add_wargas():
    warga = request.get_json()
    return jsonify(insert_warga(warga))


# resource update warga

@app.route('/api/v1/warga', methods=['PUT'])
def update_wargas():
    pasien = request.get_json()
    return jsonify(update_warga(warga))


# resource delete warga by id

@app.route('/api/v1/warga/<id_warga>', methods=['DELETE'])
def delete_wargas(id_warga):
    return jsonify(delete_warga(id_warga))



if __name__ == "__main__":
    app.run(debug=True, port=4040)
