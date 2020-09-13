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

#alumno = Alumno('Christian', 24, 'christian.guerra1013@gmail.com','M')
#alumno.fetchall_alumnos()

class Docente:
    def __init__(self, nombre_docente, edad_docente, correo_dcoente, sexo_docente):
        self.nombre_docente = nombre_docente
        self.edad_docente = edad_docente
        self.correo_dcoente = correo_dcoente
        self.sexo_docente = sexo_docente
        self.create_table_docente()

    def create_table_docente(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_DOCENTE(
                    IdDocente SERIAL PRIMARY KEY NOT NULL,
                    nombre_docente VARCHAR(255) NOT NULL,
                    edad_docente INT,
                    correo_docente VARCHAR(255),
                    sexo_docente VARCHAR(1)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_docente(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_DOCENTE;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdDocente = {row[0]}')
                print(f'nombre_docente = {row[1]}')
                print(f'edad_docente = {row[2]}')
                print(f'correo_docente = {row[3]}')
                print(f'sexo_docente = {row[4]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

#docente = Docente('Christian', 24, 'christian.guerra1013@gmail.com','M')
#docente.fetchall_docente()

#class Curso:

#class Salon:

#class Seccion:

class Año_Escolar:
    def __init__(self, anio_escolar):
        self.anio_escolar = anio_escolar
        self.create_table_anio_escolar()
    
    def create_table_anio_escolar(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_ANIO_ESCOLAR(
                    IdAnioEscolar SERIAL PRIMARY KEY NOT NULL,
                    anio_escolar VARCHAR(4) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
    
    def fetchall_anio_escolar(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_ANIO_ESCOLAR;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdAnioEscolar = {row[0]}')
                print(f'anio_escolar = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

anios_escolares = Año_Escolar('2020')
anios_escolares.fetchall_anio_escolar()


class Nivel:
    def __init__(self, nombre_nivel):
        self.nombre_nivel = nombre_nivel
        self.create_table_nivel()
    
    def create_table_nivel(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_NIVEL(
                    IdNivel SERIAL PRIMARY KEY NOT NULL,
                    nombre_nivel VARCHAR(255) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
    
    def fetchall_nivel(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_NIVEL;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdNivel = {row[0]}')
                print(f'nombre_nivel = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

#nivel = Nivel('Primaria')
#nivel.fetchall_nivel()

class Grado:
    def __init__(self, nombre_grado):
        self.nombre_grado = nombre_grado
        self.create_table_grado()
    
    def create_table_grado(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_GRADO(
                    IdGrado SERIAL PRIMARY KEY NOT NULL,
                    nombre_grado VARCHAR(255) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
    
    def fetchall_grado(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_GRADO;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdGrado = {row[0]}')
                print(f'nombre_grado = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

grado = Grado('Primaria')
grado.fetchall_grado()

#class Periodo_Evaluacion:

##Tablas Pivots

#class Grado_Nivel:

#class Gardo_Nivel_Seccion:

#class Ubicacion:
#    def __init__(self, id_grados_nivel, id_salon):
#        self.id_grados_nivel = id_grados_nivel
#        self.id_salon = id_salon
#        self.create_table_ubicacion()
#    
#    def create_table_ubicacion(self):
#        try:
#            conn = Connection()
#            query = '''
#                CREATE TABLE IF NOT EXISTS TB_UBICACION(
#                    IdUbicacion SERIAL PRIMARY KEY NOT NULL,
#                    Id_grados_nivel INT NOT NULL,
#                    Id_salon INT NOT NULL,
#                    CONSTRAINT FK_grado_nivel FOREIGN KEY (Id_grados_nivel) REFERENCES tb_grado_nivel(Id_grados_nivel),
#                    CONSTRAINT FK_salon FOREIGN KEY (Id_salon) REFERENCES tb_salon(Id_salon)
#                );
#            '''
#
#            conn.execute_query(query)
#            conn.commit()
#        except Exception as e:
#            raise print(e)
#    
#    def fetchall_ubicacion(self):
#        try:
#            conn= Connection()
#            query= '''
#                SELECT * FROM TB_UBICACION;
#            '''
#            cursor = conn.execute_query(query)
#            rows = cursor.fetchall()
#
#            for row in rows:
#                print(f'IdUbicacion = {row[0]}')
#                print(f'Id_grados_nivel = {row[1]}')
#                print(f'Id_salon = {row[2]}')
#                print('=============================')
#        except Exception as e:
#            print(f'{str(e)}')
#
#ubicacion = Ubicacion(2,1)
#ubicacion.fetchall_ubicacion()

#class Docente_Curso:

#class Asignacion_Docente:

#class Asignacion_Alumno:

#class Periodo_Evaluacion_Detalle:
