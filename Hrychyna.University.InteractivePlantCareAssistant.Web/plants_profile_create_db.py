from flask import Flask, request, render_template
from demo import conn

app = Flask(__name__)

# Your existing code for establishing connection goes here


def create_table():
    cursor = conn.cursor()
    sql = '''
    CREATE TABLE plant_profile_table (
        plant_name NVARCHAR(100),
        plant_type NVARCHAR(100),
        location NVARCHAR(100),
        planting_date DATE,
        light_exposure NVARCHAR(100),
        plant_image NVARCHAR(255)
    )
    '''
    cursor.execute(sql)
    conn.commit()
    cursor.close()


create_table()


@app.route('/create_profile', methods=['POST'])
def create_profile():
    if request.method == 'POST':
        # Extract form data
        plant_name = request.form['plantName']
        plant_type = request.form['plantType']
        location = request.form['location']
        planting_date = request.form['plantPlantingDate']
        light_exposure = request.form['plantLight']
        # Insert data into the database
        cursor = conn.cursor()
        sql = "INSERT INTO plant_profile_table (plant_name, plant_type, location, planting_date, light_exposure) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(sql, (plant_name, plant_type, location, planting_date, light_exposure))
        conn.commit()
        cursor.close()
        return 'Plant profile created successfully!'


if __name__ == '__main__':
    app.run(debug=True)
