from conn import Connection

class Alumno:
    def __init__(self, nombre_alumno, edad_alumno, correo_alumno, sexo_alumno):
        self.nombre_alumno = nombre_alumno
        self.edad_alumno = edad_alumno
        self.correo_alumno = correo_alumno
        self.sexo_alumno = sexo_alumno
        self.create_table_alumno()

        #print('Hola')

    def create_table_alumno(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_ALUMNO(
                    IdAlumno SERIAL PRIMARY KEY NOT NULL,
                    nombre_alumno VARCHAR(255) NOT NULL,
                    edad_alumno INT,
                    correo_alumno VARCHAR(255),
                    sexo_alumno VARCHAR(1)
                );
            '''

            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            raise print(e)

    def fetchall_alumnos(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_ALUMNO;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdAlumno = {row[0]}')
                print(f'nombre_alumno = {row[1]}')
                print(f'edad_alumno = {row[2]}')
                print(f'correo_alumno = {row[3]}')
                print(f'sexo_alumno = {row[4]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

alumno = Alumno('Christian', 24, 'christian.guerra1013@gmail.com','M')
alumno.fetchall_alumnos()
