import sqlite3


def connect_to_db():
    conn = sqlite3.connect('db_warga.db')
    return conn



# buat tabel

def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''
        CREATE TABLE IF NOT EXISTS tbl_warga (
            id_warga INTEGER PRIMARY KEY NOT NULL,
            nama TEXT NOT NULL,
            jenis_kelamin TEXT NOT NULL,
            no_hp INTEGER NOT NULL,
            alamat TEXT NOT NULL
        );
        ''')
        conn.commit()
        print('Tabel warga berhasil dibuat')
    except:
        print("Tabel warga gagal dibuat")
    finally:
        conn.close()



# tambah warga

def insert_warga(warga):
    inserted_warga = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_warga(nama, jenis_kelamin, no_hp, alamat) VALUES (?, ?, ?, ?)",
                    (warga['nama'], warga['jenis_kelamin'], warga['no_hp'], warga['alamat']))
        conn.commit()
        # mendapatkan id warga yang baru ditambahkan
        inserted_warga['id'] = cur.lastrowid
        inserted_warga['nama'] = warga['nama']
        inserted_warga['jenis_kelamin'] = warga['jenis_kelamin']
        inserted_warga['no_hp'] = warga['no_hp']
        inserted_warga['alamat'] = warga['alamat']

    except Exception as e:
        print(f"Error: {e}")
        conn().rollback()
    finally:
        conn.close()
    return inserted_warga



# get semua warga

def get_wargas():
    wargas = []

    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_warga")
        rows = cur.fetchall()

        for i in rows:
            warga = {}
            warga["id_warga"] = i["id_warga"]
            warga["nama"] = i["nama"]
            warga["jenis_kelamin"] = i["jenis_kelamin"]
            warga["no_hp"] = i["no_hp"]
            warga["alamat"] = i["alamat"]
            wargas.append(warga)
    except:
        wargas = []
    return wargas



# get warga by id

def get_warga_by_id(id_warga):
    warga = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tbl_warga WHERE id_warga = ?", (id_warga))
        row = cur.fetchone()

        if row is not None:
            warga["id_warga"] = row["id_warga"]
            warga["nama"] = row["nama"]
            warga["jenis_kelamin"] = row["jenis_kelamin"]
            warga["no_hp"] = row["no_hp"]
            warga["alamat"] = row["alamat"]
    except Exception as e:
        print(f"Error: {e}")
    return warga



# update warga

def update_warga(warga):
    updated_warga = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE tbl_warga SET nama = ?, jenis_kelamin = ?, no_hp = ?, alamat = ? WHERE id_warga = ?",
                    (warga["nama"], warga["jenis_kelamin"], warga["no_hp"], warga["alamat"], warga["id_warga"],))
        conn.commit()
        updated_warga = get_warga_by_id(warga["id_warga"])
    except:
        conn.rollback()
        updated_warga = {}
    finally:
        conn.close()
    return updated_warga



# hapus warga

def delete_warga(id_warga):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE FROM tbl_warga WHERE id_warga = ?", (id_warga))
        conn.commit()
        message["status"] = "warga deleted successfully"
    except:
        conn.rollback()
        message["status"] = "Cannot delete warga"
    finally:
        conn.close()
    return message



# data
if __name__ == '__main__':
    wargas = []
    warga1 = {
        "nama": "Riatul soleh",
        "jenis_kelamin": "Perempuan",
        "no_hp": "0983495234",
        "alamat": "jalan Mawar rt 03 rw 02"
    }
    warga2 = {
        "nama": "Arya Gunawan",
        "jenis_kelamin": "Laki-laki",
        "no_hp": "085463823782",
        "alamat": "jalan Kamboja rt 04 rw 02"
    }
    warga3 = {
        "nama": "Gunawan Slamet",
        "jenis_kelamin": "Laki-laki",
        "no_hp": "085435948223",
        "alamat": "jalan Kamboja rt 04 rw 02"
    }    
    wargas.append(warga1)
    wargas.append(warga2)
    wargas.append(warga3)


    create_db_table()

    for i in wargas:
        print(insert_warga(i))
