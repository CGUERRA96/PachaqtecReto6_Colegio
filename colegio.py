from conn import Connection
from time import sleep

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
                print(f'{row[0]}) {row[1]}, {row[2]}, {row[3]}, {row[4]}')
                print('====================================================')

        except Exception as e:
            print(f'{str(e)}')

    def insert_alumnos(self):
        try:
            conn = Connection()
            self.nombre_alumno = input(f'Insertar nuevo alumno: ')
            self.edad_alumno = int(input(f'Insertar nueva edad del alumno: '))
            self.correo_alumno = input(f'Insertar correo del nuevo alumno: ')
            self.sexo_alumno = input(f'Insertar el sexo del nuevo alumno: ')

            query = f'''
                INSERT INTO TB_ALUMNO (nombre_alumno, edad_alumno, correo_alumno, sexo_alumno)
                VALUES('{self.nombre_alumno}', {self.edad_alumno}, '{self.correo_alumno}', '{self.sexo_alumno}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego al Alumno -> {self.nombre_alumno}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_alumnos(self):
        try:
            conn = Connection()
            self.nombre_alumno = input(f'Actualizar al alumno: ')
            self.edad_alumno = int(input(f'Actualizar la edad del alumno: '))
            self.correo_alumno = input(f'Actualizar el correo del alumno: ')
            self.sexo_alumno = input(f'Actualizar el sexo del alumno: ')

            IdAlumno = int(input('Indicar el IdAlumno: '))

            query = f'''
                UPDATE TB_ALUMNO SET nombre_alumno = '{self.nombre_alumno}', edad_alumno = {self.edad_alumno}, correo_alumno = '{self.correo_alumno}', sexo_alumno = '{self.sexo_alumno}'
                WHERE IdAlumno = {IdAlumno};
            '''

            cursor = conn.execute_query(query)
            conn.commit()
            print(f'Se actualizo el alumno con el IdAlumno {IdAlumno} por -> {self.nombre_alumno} - {self.edad_alumno} - {self.correo_alumno} - {self.sexo_alumno}')

        except Exception as e:
            print(f'{str(e)}')

    def delete_alumno(self):
        try:
            conn = Connection()

            IdAlumno = int(input('Indicar el IdAlumno para eliminar: '))

            query = f'''
                DELETE FROM TB_ALUMNO WHERE IdAlumno = {IdAlumno};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino al alumno con IdAlumno {IdAlumno}')
        except Exception as e:
            print(f'{str(e)}')

#alumno = Alumno('Christian', 24, 'christian.guerra1013@gmail.com','M')
#alumno.fetchall_alumnos()

class Docente:
    def __init__(self, nombre_docente, edad_docente, correo_docente, sexo_docente):
        self.nombre_docente = nombre_docente
        self.edad_docente = edad_docente
        self.correo_docente = correo_docente
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
                print(f'{row[0]}) {row[1]}, {row[2]}, {row[3]}, {row[4]}')
                print('====================================================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_docente(self):
        try:
            conn = Connection()

            self.nombre_docente = input(f'Insertar nuevo docente: ')
            self.edad_docente = int(input(f'Insertar nueva edad del docente: '))
            self.correo_docente = input(f'Insertar correo del nuevo docente: ')
            self.sexo_docente = input(f'Insertar el sexo del nuevo docente: ')

            query = f'''
                INSERT INTO TB_DOCENTE (nombre_docente, edad_docente, correo_docente, sexo_docente)
                VALUES('{self.nombre_docente}', {self.edad_docente}, '{self.correo_docente}', '{self.sexo_docente}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego al Docente -> {self.nombre_docente}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_docente(self):
        try:
            conn = Connection()

            self.nombre_docente = input(f'Actualizar al docente: ')
            self.edad_docente = int(input(f'Actualizar la edad del docente: '))
            self.correo_docente = input(f'Actualizar el correo del docente: ')
            self.sexo_docente = input(f'Actualizar el sexo del docente: ')

            IdDocente = int(input('Indicar el IdDocente: '))

            query = f'''
                UPDATE TB_DOCENTE SET nombre_docente = '{self.nombre_docente}', edad_docente = {self.edad_docente}, correo_docente = '{self.correo_docente}', sexo_docente = '{self.sexo_docente}'
                WHERE IdDocente = {IdDocente};
            '''

            cursor = conn.execute_query(query)
            conn.commit()
            print(f'Se actualizo el docente con el IdDocente {IdDocente} por -> {self.nombre_docente} - {self.edad_docente} - {self.correo_docente} - {self.sexo_docente}')

        except Exception as e:
            print(f'{str(e)}')

    def delete_docente(self):
        try:
            conn = Connection()

            IdDocente = int(input('Indicar el IdDocente para eliminar: '))

            query = f'''
                DELETE FROM TB_DOCENTE WHERE IdDocente = {IdDocente};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino al docente con IdDocente {IdDocente}')
        except Exception as e:
            print(f'{str(e)}')

#docente = Docente('Christian', 24, 'christian.guerra1013@gmail.com','M')
#docente.fetchall_docente()

class Curso:
    def __init__(self, nombrecurso):
        self.nombrecurso = nombrecurso
        self.create_table_curso()

    def create_table_curso(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Cursos(
                    Idcurso SERIAL PRIMARY KEY NOT NULL,
                    nombrecurso VARCHAR(255) NOT NULL
                    
                );
            '''
            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_curso(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_Cursos;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]}')
        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Cursos(self):
        try:
            conn = Connection()

            self.nombrecurso = input('Ingrese el nuevo curso: ')

            query = f'''
                INSERT INTO TB_Cursos (nombrecurso)
                VALUES('{self.nombrecurso}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha insertado la Tabla Cursos --> {self.nombrecurso}')
        except Exception as e:
            print(f'{str(e)}')

    def update_TB_Cursos(self):
        try:
            conn = Connection()

            self.nombrecurso = input('Ingrese el nuevo curso: ')
            
            Idcurso = int(input('Ingrese el IdCurso: '))

            query = f'''
                UPDATE TB_Cursos SET nombrecurso = '{self.nombrecurso}' 
                WHERE Idcurso = {Idcurso};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Cursos -> {self.nombrecurso}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_TB_Cursos(self):
        try:
            conn = Connection()

            Idcurso = int(input('Ingrese el IdCurso: '))

            query = f'''
                DELETE FROM TB_Cursos WHERE Idcurso = {Idcurso};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la Tabla Cursos con Idcurso {Idcurso}')
        except Exception as e:
            print(f'{str(e)}')

#curso = Curso('Literatura')
#curso.fetchall_TB_curso()

class Salon:
    def __init__(self, salon):
        self.salon = salon
        self.create_table_salon()
    
    
    def create_table_salon(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_salon(
                    IdSalon SERIAL PRIMARY KEY NOT NULL,
                    num_salon INT NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_Salon(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_salon;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_salon(self):
        try:
            conn = Connection()

            self.salon = int(input('Ingrese el nuevo número del salon: '))

            query = f'''
                INSERT INTO TB_salon (num_salon) 
                VALUES({self.salon});
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego en la Tabla Salon -> {self.salon}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_TB_salon(self, IdSalon):
        try:
            conn = Connection()

            query = f'''
                UPDATE TB_salon SET num_salon = {self.salon} 
                WHERE IdSalon = {IdSalon};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Salon con el IdSalon -> {IdSalon}')
        except Exception as e:
            print(f'{str(e)}')
    
    def delete_TB_salon(self, IdSalon):
        try:
            conn = Connection()

            query = f'''
                DELETE FROM TB_salon WHERE IdSalon = {IdSalon};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el salon con IdSalon -> {IdSalon}')
        except Exception as e:
            print(f'{str(e)}')

#salon = Salon(103)
#salon.fetchall_Salon()

class Seccion:
    def __init__(self, Nombre_Seccion):
        self.Nombre_Seccion = Nombre_Seccion
        self.create_table_Seccion()

    def create_table_Seccion(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Seccion(
                    IdSeccion SERIAL PRIMARY KEY NOT NULL,
                    Nombre_Seccion VARCHAR(255) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_Seccion(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_Seccion;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Seccion(self):
        try:
            conn = Connection()

            query = f'''
                INSERT INTO TB_Seccion (Nombre_Seccion)
                VALUES('{self.Nombre_Seccion}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha ingresado la nueva Seccion --> {self.Nombre_Seccion}')
        except Exception as e:
            print(f'{str(e)}')

    def update_TB_Seccion(self, IdSeccion):
        try:
            conn = Connection()

            query = f'''
                UPDATE TB_Seccion SET Nombre_Seccion = '{self.Nombre_Seccion}' 
                WHERE IdSeccion = {IdSeccion};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Seccion -> {self.Nombre_Seccion}')

        except Exception as e:
            print(f'{str(e)}')

    def delete_TB_Seccion(self, IdSeccion):
        try:
            conn = Connection()

            query = f'''
                DELETE FROM TB_Seccion WHERE IdSeccion = {IdSeccion};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la seccion con IdSeccion {IdSeccion}')
        except Exception as e:
            print(f'{str(e)}')

#seccion = Seccion('A')
#seccion.fetchall_TB_Seccion()

class Anio_Escolar:
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
                print(f'{row[0]}) {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')
    
    def insert_anio_escolar(self):
        try:
            conn = Connection()

            self.anio_escolar = input('Ingrese el nuevo año escolar: ')

            query = f'''
                INSERT INTO TB_ANIO_ESCOLAR (anio_escolar)
                VALUES('{self.anio_escolar}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego el año escolar -> {self.anio_escolar}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_anio_escolar(self):
        try:
            conn = Connection()

            self.anio_escolar = input('Actualice el año escolar: ')

            IdAnioEscolar = int(input('Ingrese el IdAñoEscolar: '))

            query = f'''
                UPDATE TB_ANIO_ESCOLAR SET anio_escolar = '{self.anio_escolar}' 
                WHERE IdAnioEscolar = {IdAnioEscolar};
            '''

            cursor = conn.execute_query(query)
            conn.commit()
            print(f'Se actualizo el año escolar con el IdAnioEscolar {IdAnioEscolar} por -> {self.anio_escolar}')

        except Exception as e:
            print(f'{str(e)}')

    def delete_anio_escolar(self):
        try:
            conn = Connection()

            IdAnioEscolar = int(input('Ingrese el IdAñoEscolar: '))

            query = f'''
                DELETE FROM TB_ANIO_ESCOLAR WHERE IdAnioEscolar = {IdAnioEscolar};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el año escolar con IdAnioEscolar {IdAnioEscolar}')
        except Exception as e:
            print(f'{str(e)}')

#anios_escolares = Anio_Escolar('2020')
#anios_escolares.fetchall_anio_escolar()


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

    def insert_nivel(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_NIVEL (nombre_nivel)
                VALUES('{self.nombre_nivel}');
            '''

            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha actualizado la Tabla nivel --> {self.nombre_nivel}')
        except Exception as e:
            print(f'{str(e)}')

    def update_nivel(self, IdNivel):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_NIVEL SET nombre_nivel = '{self.nombre_nivel}' 
                WHERE IdNivel = {IdNivel};
            '''
            cursor = conn.execute_query(query)
            conn.commit()
        except Exception as e:
            print(f'{str(e)}')
        
    def delete_nivel(self, IdNivel):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_NIVEL WHERE IdNivel = {IdNivel};
            '''
            conn.execute_query(query)
            conn.commit()
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

    def insert_grado(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_GRADO (nombre_grado)
                VALUES('{self.nombre_grado}');
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se agrego el grado -> {self.nombre_grado}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_grado(self, IdGrado):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_GRADO SET nombre_grado = '{self.nombre_grado}' 
                WHERE IdGrado = {IdGrado};
            '''

            cursor = conn.execute_query(query)
            conn.commit()
            print(f'Se actualizo el grado, con el IdGrado {IdGrado} por -> {self.nombre_grado}')

        except Exception as e:
            print(f'{str(e)}')

    def delete_grado(self, IdGrado):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_ANIO_ESCOLAR WHERE IdGrado = {IdGrado};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino el grado con IdGrado {IdGrado}')
        except Exception as e:
            print(f'{str(e)}')

            

#grado = Grado('Primaria')
#grado.fetchall_grado()

class Periodo_Evaluacion:
    def __init__(self, nombre_tiempo):
        self.nombre_tiempo = nombre_tiempo
        self.create_table_periodo_evaluacion()
    
    def create_table_periodo_evaluacion(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_periodo_evaluacion(
                    IdPeriodoEval SERIAL PRIMARY KEY NOT NULL,
                    nombretiempo VARCHAR(255) NOT NULL
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_Periodo_Evaluacion(self):
        try:
            conn= Connection()
            query= '''
                SELECT * FROM TB_periodo_evaluacion;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:

                print(f'{row[0]}) {row[1]}')

        except Exception as e:
            print(f'{str(e)}')

#periodoeval = Periodo_Evaluacion('Bimestre 1')
#periodoeval.fetchall_Periodo_Evaluacion()

##Tablas Pivots

class Grado_Nivel:
    def __init__(self, IdGrado, IdNivel):
        self.IdGrado = IdGrado
        self.IdNivel = IdNivel
        self.create_table_Grado_Nivel()
    
    def create_table_Grado_Nivel(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Grado_Nivel(
                    IdGradoNivel SERIAL PRIMARY KEY NOT NULL,
                    IdGrado INT NOT NULL,
                    IdNivel INT NOT NULL,
                    CONSTRAINT FK_GRADO FOREIGN KEY (IdGrado) REFERENCES tb_grado(IdGrado),
                    CONSTRAINT FK_NIVEL FOREIGN KEY (IdNivel) REFERENCES tb_nivel(IdNIvel)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_Grado_Nivel(self):
        try:
            conn= Connection()
            query= '''
                Select gn.idgradonivel, gr.nombre_grado, nv.nombre_nivel 
                from tb_grado_nivel gn
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]},{row[2]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

#gradonivel = Grado_Nivel(1,1)
#gradonivel.fetchall_TB_Grado_Nivel()

class Grado_Nivel_Seccion:
    def __init__(self, Idgradosnivel, IdSeccion, IdAnioEscolar):
        self.Idgradosnivel = Idgradosnivel
        self.IdSeccion = IdSeccion
        self.IdAnioEscolar = IdAnioEscolar
        self.create_table_grado_seccion()

    def create_table_grado_seccion(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Grado_Nivel_Seccion(
                    Idgradoseccion SERIAL PRIMARY KEY NOT NULL,
                    Idgradosnivel INT NOT NULL,
                    IdSeccion INT NOT NULL,
                    IdAnioEscolar INT NOT NULL,
                    CONSTRAINT FK_gradosnivel FOREIGN KEY (Idgradosnivel) REFERENCES TB_Grado_Nivel(IdGradoNivel),
                    CONSTRAINT FK_Seccion FOREIGN KEY (IdSeccion) REFERENCES TB_Seccion(IdSeccion),
                    CONSTRAINT FK_AnioEscolar FOREIGN KEY (IdAnioEscolar) REFERENCES tb_anio_escolar(IdAnioEscolar)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_grado_seccion(self):
        try:
            conn= Connection()
            query= '''
                Select gns.idgradoseccion, gr.nombre_grado, nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar
                from tb_grado_nivel_seccion gns
                left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel
                left join tb_seccion sc on gns.idseccion = sc.idseccion
                left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]} - {row[2]} - {row[3]} - {row[4]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Grado_Nivel_Seccion(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_Grado_Nivel_Seccion (Idgradosnivel, IdSeccion, IdAnioEscolar)
                VALUES({self.Idgradosnivel}, {self.IdSeccion}, {self.IdAnioEscolar});
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha actualizado la Tabla Grado Nivel Seccion --> {self.Idgradosnivel}, {self.IdSeccion}, {self.IdAnioEscolar}')
        except Exception as e:
            print(f'{str(e)}')

    def update_TB_Grado_Nivel_Seccion(self, Idgradoseccion):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_Grado_Nivel_Seccion SET Idgradosnivel = {self.Idgradosnivel}, IdSeccion = {self.IdSeccion}, IdAnioEscolar = {self.IdAnioEscolar} WHERE Idgradoseccion = {Idgradoseccion};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Grado Nivel Seccion -> {self.Idgradosnivel}, {self.IdSeccion}, {self.IdAnioEscolar}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_TB_Grado_Nivel_Seccion(self, Idgradoseccion):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_Grado_Nivel_Seccion WHERE Idgradoseccion = {Idgradoseccion};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la Tabla Grado Nivel Seccion con Idgradoseccion {Idgradoseccion}')
        except Exception as e:
            print(f'{str(e)}')

#grado_seccion = Grado_Nivel_Seccion(1,1,1)
#grado_seccion.fetchall_TB_grado_seccion()


class Ubicacion:
    def __init__(self, id_grados_nivel, id_salon):
        self.id_grados_nivel = id_grados_nivel
        self.id_salon = id_salon
        self.create_table_ubicacion()
    
    def create_table_ubicacion(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_UBICACION(
                    IdUbicacion SERIAL PRIMARY KEY NOT NULL,
                    Id_grados_nivel INT NOT NULL,
                    Id_salon INT NOT NULL,
                    CONSTRAINT FK_grado_nivel FOREIGN KEY (Id_grados_nivel) REFERENCES tb_grado_nivel(IdGradoNivel),
                    CONSTRAINT FK_salon FOREIGN KEY (Id_salon) REFERENCES tb_salon(IdSalon)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)
    
    def fetchall_ubicacion(self):
        try:
            conn= Connection()
            query= '''
                Select u.idubicacion, gr.nombre_grado, 
                nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar, ss.num_salon
                from tb_ubicacion u
                left join tb_grado_nivel_seccion gns on u.id_grados_nivel = gns.idgradoseccion
                left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel
                left join tb_seccion sc on gns.idseccion = sc.idseccion
                left join tb_salon ss on u.id_salon = ss.idsalon
                left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

    def insert_ubicacion(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_UBICACION (Id_grados_nivel, Id_salon)
                VALUES({self.id_grados_nivel}, {self.id_salon});
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            print(f'{str(e)}')

    def update_ubicacion(self, IdUbicacion):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_UBICACION SET Id_grados_nivel = {self.id_grados_nivel}, Id_salon = {self.id_salon} 
                WHERE IdUbicacion = {IdUbicacion};
            '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(f'{str(e)}')

    def delete_ubicacion(self, IdUbicacion):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_UBICACION WHERE IdUbicacion = {IdUbicacion};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la Tabla Ubicacion con IdUbicacion {IdUbicacion}')
        except Exception as e:
            print(f'{str(e)}')

#ubicacion = Ubicacion(1,1)
#ubicacion.fetchall_ubicacion()

class Docente_Curso:
    def __init__(self, IdDocente, IdCurso):
        self.IdDocente = IdDocente
        self.IdCurso = IdCurso
        self.create_table_Docente_Curso()
    
    def create_table_Docente_Curso(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Docente_Curso(
                    IdDocenteCurso SERIAL PRIMARY KEY NOT NULL,
                    IdDocente INT NOT NULL,
                    IdCurso INT NOT NULL,
                    CONSTRAINT FK_DOCENTE FOREIGN KEY (IdDocente) REFERENCES tb_docente(IdDocente),
                    CONSTRAINT FK_CURSO FOREIGN KEY (IdCurso) REFERENCES tb_cursos(IdCurso)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_Docente_Curso(self):
        try:
            conn= Connection()
            query= '''
                Select dc.IdDocenteCurso ,d.Nombre_docente, cs.nombrecurso 
                from TB_Docente_Curso DC
                left join tb_docente D on dc.iddocente = d.iddocente
                left join tb_cursos Cs on Cs.idcurso = dc.idcurso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'{row[0]}) {row[1]}, {row[2]}')             
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')


    def insert_TB_Docente_Curso(self):
        try:
            conn = Connection()

            query = f'''
                INSERT INTO TB_Docente_Curso (IdDocente, IdCurso) 
                VALUES({self.IdDocente}, {self.IdCurso})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha actualizado la Tabla Docente Curso -> {self.IdDocente}, {self.IdCurso}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_TB_Docente_Curso(self, IdDocenteCurso):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_Docente_Curso SET IdDocente = {self.IdDocente}, IdCurso = {self.IdCurso} WHERE IdDocenteCurso = {IdDocenteCurso};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Periodo Evaluacion con el IdDocenteCurso-> {IdDocenteCurso}')
        except Exception as e:
            print(f'{str(e)}')
    
    def delete_TB_Docente_Curso(self, IdDocenteCurso):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_Docente_Curso WHERE IdDocenteCurso = {IdDocenteCurso};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la seccion con IdDocenteCurso -> {IdDocenteCurso}')
        except Exception as e:
            print(f'{str(e)}')

#docente_curso = Docente_Curso(1,1)
#docente_curso.fetchall_TB_Docente_Curso()


class Asignacion_Docente:
    def __init__(self, IdcursoDocente, IdUbicacion):
        self.IdcursoDocente = IdcursoDocente
        self.IdUbicacion = IdUbicacion
        self.create_table_asignacion_Docente_salon()

    def create_table_asignacion_Docente_salon(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Asignacion_Docente(
                    Idasigdocente SERIAL PRIMARY KEY NOT NULL,
                    IdcursoDocente INT NOT NULL,
                    IdUbicacion INT NOT NULL,
                    CONSTRAINT FK_cursodocente FOREIGN KEY (IdcursoDocente) REFERENCES TB_Docente_Curso(IdDocenteCurso),
                    CONSTRAINT FK_Ubicacion FOREIGN KEY (IdUbicacion) REFERENCES tb_ubicacion(IdUbicacion)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_asignacion_Docente_salon(self):
        try:
            conn= Connection()
            query= '''
                Select ad.idasigdocente, d.Nombre_docente, cs.nombrecurso, gr.nombre_grado, 
                nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar, ss.num_salon
                from tb_asignacion_docente ad
                left join tb_docente_curso dc on ad.idcursodocente = dc.iddocentecurso
                left join tb_docente d on dc.iddocente = d.iddocente
                left join tb_cursos cs on cs.idcurso = dc.idcurso
                left join tb_ubicacion u on u.idubicacion = ad.idubicacion
                left join tb_grado_nivel_seccion gns on u.id_grados_nivel = gns.idgradoseccion
                left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel
                left join tb_seccion sc on gns.idseccion = sc.idseccion
                left join tb_salon ss on u.id_salon = ss.idsalon
                left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:

                print(f'{row[0]}) {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]}')

        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Asignacion_Docente(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_Asignacion_Docente (IdcursoDocente, IdUbicacion)
                VALUES({self.IdcursoDocente}, {self.IdUbicacion})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha actualizado la Tabla Asignacion Docente --> {self.IdcursoDocente}, {self.IdUbicacion}')
        except Exception as e:
            print(f'{str(e)}')

    def update_TB_Asignacion_Docente(self, Idasigdocente):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_Asignacion_Docente SET IdcursoDocente = {self.IdcursoDocente}, IdUbicacion = {self.IdUbicacion} 
                WHERE Idasigdocente = {Idasigdocente};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la Tabla Asignacion Docente -> {self.IdcursoDocente}, {self.IdUbicacion}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_TB_Asignacion_Docente(self, Idasigdocente):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_Asignacion_Docente WHERE Idasigdocente = {Idasigdocente};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la Tabla Asignacion Docente con Idasigdocente {Idasigdocente}')
        except Exception as e:
            print(f'{str(e)}')

#asig_doc = Asignacion_Docente(1,1)
#asig_doc.fetchall_TB_asignacion_Docente_salon()


class Asignacion_Alumno:
    def __init__(self, Idalumno, Idasigdoc):
        self.Idalumno = Idalumno
        self.Idasigdoc = Idasigdoc
        self.create_table_Alumno_doc_salon()

    def create_table_Alumno_doc_salon(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Asignacion_Alumno(
                    IdAlumnodocsalon SERIAL PRIMARY KEY NOT NULL,
                    Idalumno INT NOT NULL,
                    Idasigdoc INT NOT NULL,
                    CONSTRAINT FK_Idalumno FOREIGN KEY (Idalumno) REFERENCES TB_ALUMNO(Idalumno),
                    CONSTRAINT FK_Idasigdoc FOREIGN KEY (Idasigdoc) REFERENCES TB_Asignacion_Docente(Idasigdocente)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_Alumno_doc_salon(self):
        try:
            conn= Connection()
            query= '''
                Select aa.idalumnodocsalon, al.nombre_alumno, al.edad_alumno, al.correo_alumno, al.sexo_alumno, d.Nombre_docente, cs.nombrecurso, gr.nombre_grado, 
                nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar, ss.num_salon
                from tb_asignacion_alumno aa
                left join tb_alumno al on aa.idalumno = al.idalumno
                left join tb_asignacion_docente ad on aa.idasigdoc = ad.idasigdocente
                left join tb_docente_curso dc on ad.idcursodocente = dc.iddocentecurso
                left join tb_docente d on dc.iddocente = d.iddocente
                left join tb_cursos cs on cs.idcurso = dc.idcurso
                left join tb_ubicacion u on u.idubicacion = ad.idubicacion
                left join tb_grado_nivel_seccion gns on u.id_grados_nivel = gns.idgradoseccion
                left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel
                left join tb_seccion sc on gns.idseccion = sc.idseccion
                left join tb_salon ss on u.id_salon = ss.idsalon
                left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:

                print(f'{row[0]}) {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]} - {row[8]} - {row[9]} - {row[10]} - {row[11]}')

        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Asignacion_Alumno(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_Asignacion_Alumno (Idalumno, Idasigdoc)
                VALUES({self.Idalumno}, {self.Idasigdoc})
                '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha matriculado nuevo alumno --> {self.Idalumno}, {self.Idasigdoc}')
        except Exception as e:
            print(f'{str(e)}')

    def update_TB_Asignacion_Alumno(self, IdAlumnodocsalon):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_Asignacion_Alumno SET Idalumno = {self.Idalumno}, Idasigdoc = {self.Idasigdoc} 
                WHERE IdAlumnodocsalon = {IdAlumnodocsalon};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha modificado la matricula del Alumno -> {self.Idalumno}, {self.Idasigdoc}')
        except Exception as e:
            print(f'{str(e)}')

    def delete_TB_Asignacion_Alumno(self, IdAlumnodocsalon):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_Asignacion_Alumno WHERE IdAlumnodocsalon = {IdAlumnodocsalon};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino ha eliminado la matricula, con IdAlumnodocsalon {IdAlumnodocsalon}')
        except Exception as e:
            print(f'{str(e)}')

#asig_alumn = Asignacion_Alumno(1,1)
#asig_alumn.fetchall_TB_Alumno_doc_salon()

class Periodo_Evaluacion_Detalle:
    def __init__(self, IdAsignacion_Alumno, IdPeriodoEval, nota):
        self.IdAsignacion_Alumno = IdAsignacion_Alumno
        self.IdPeriodoEval = IdPeriodoEval
        self.nota = nota
        self.create_table_Per_Eval_Det()

    
    def create_table_Per_Eval_Det(self):
        try:
            conn = Connection()
            query = '''
                CREATE TABLE IF NOT EXISTS TB_Per_Eval_Det(
                    IDPer_Eval_Det SERIAL PRIMARY KEY NOT NULL,
                    IdAsignacion_Alumno INT NOT NULL,
                    IdPeriodoEval INT NOT NULL,
                    nota REAL NOT NULL,
                    CONSTRAINT FK_ASIGNACIO_ALUMNO FOREIGN KEY (IdAsignacion_Alumno) REFERENCES TB_Asignacion_Alumno(IdAlumnodocsalon),
                    CONSTRAINT FK_PERIODO_EVALUACION FOREIGN KEY (IdPeriodoEval) REFERENCES TB_periodo_evaluacion(IdPeriodoEval)
                );
            '''

            conn.execute_query(query)
            conn.commit()
        except Exception as e:
            raise print(e)

    def fetchall_TB_Per_Eval_Det(self):
        try:
            conn= Connection()
            query= '''
                select ped.idper_eval_det ,al.nombre_alumno, al.edad_alumno, al.correo_alumno, al.sexo_alumno, d.Nombre_docente, cs.nombrecurso, gr.nombre_grado, 
                nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar, ss.num_salon, pe.nombretiempo as nombre_evaluacion, ped.nota
                from tb_per_eval_det ped
                left join tb_asignacion_alumno aa on ped.idasignacion_alumno = aa.idalumnodocsalon
                left join tb_periodo_evaluacion pe on ped.idperiodoeval = pe.idperiodoeval
                left join tb_alumno al on aa.idalumno = al.idalumno
                left join tb_asignacion_docente ad on aa.idasigdoc = ad.idasigdocente
                left join tb_docente_curso dc on ad.idcursodocente = dc.iddocentecurso
                left join tb_docente d on dc.iddocente = d.iddocente
                left join tb_cursos cs on cs.idcurso = dc.idcurso
                left join tb_ubicacion u on u.idubicacion = ad.idubicacion
                left join tb_grado_nivel_seccion gns on u.id_grados_nivel = gns.idgradoseccion
                left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
                left join tb_grado gr on gr.idgrado = gn.idgrado
                left join tb_nivel nv on nv.idnivel = gn.idnivel
                left join tb_seccion sc on gns.idseccion = sc.idseccion
                left join tb_salon ss on u.id_salon = ss.idsalon
                left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar
                ;
;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:

                print(f'{row[0]}) {row[1]} - {row[2]} - {row[3]} - {row[4]} - {row[5]} - {row[6]} - {row[7]} - {row[8]} - {row[9]} - {row[10]} - {row[11]} - {row[12]} - {row[13]}')


        except Exception as e:
            print(f'{str(e)}')

    def insert_TB_Per_Eval_Det(self):
        try:
            conn = Connection()
            query = f'''
                INSERT INTO TB_Per_Eval_Det (IdAsignacion_Alumno, IdPeriodoEval, nota) 
                VALUES({self.IdAsignacion_Alumno}, {self.IdPeriodoEval}, {self.nota})
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se ha insertado la nota -> {self.IdAsignacion_Alumno}, {self.IdPeriodoEval}, {self.nota}')
        except Exception as e:
            print(f'{str(e)}')
    
    def update_TB_Per_Eval_Det(self, IDPer_Eval_Det):
        try:
            conn = Connection()
            query = f'''
                UPDATE TB_Per_Eval_Det SET IdAsignacion_Alumno = {self.IdAsignacion_Alumno}, IdPeriodoEval = {self.IdPeriodoEval}, nota = {self.nota} WHERE IDPer_Eval_Det = {IDPer_Eval_Det};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se actualizo la nota con IDPer_Eval_Det -> {IDPer_Eval_Det}')

        except Exception as e:
            print(f'{str(e)}')
    
    def delete_TB_Per_Eval_Det(self, IDPer_Eval_Det):
        try:
            conn = Connection()
            query = f'''
                DELETE FROM TB_Per_Eval_Det WHERE IDPer_Eval_Det = {IDPer_Eval_Det};
            '''
            cursor = conn.execute_query(query)
            conn.commit()

            print(f'Se elimino la nota con IDPer_Eval_Det -> {IDPer_Eval_Det}')
        except Exception as e:
            print(f'{str(e)}')

#fin = Periodo_Evaluacion_Detalle(1,1,17)
#fin.fetchall_TB_Per_Eval_Det()



#class Interfaz(Alumno, Docente):
#    def __init__(self):
#        #Metodos Alumno
#        self.fetchall_alumnos()
#        self.insert_alumnos()
#        self.update_alumnos()
#        self.delete_alumno()
#        #Metodos Docenet
#        self.fetchall_docente()
#        self.insert_docente()
#        self.update_docente()
#        self.delete_docente()
#
#
#
#    def interfaz(self):
#            while True:
#                print('''\nBienvenido al Menú del Colegio
#                ¿Que deseas hacer?
#                1) Modulo Alumno
#                2) Modulo Docente
#                3) Modulo Curso
#                4) Modulo Recursos
#                6) Salir del programa''')
#                opcion = input("> ")
#                if opcion == "1":
#                    print(
#                        '''\n¿Que deseas hacer en Alumno?
#                    1) Agregar Alumno
#                    2) Actualizar Alumno
#                    3) Eliminar Alumno
#                    4) Mostrar Alumno
#                    '''
#                    )
#                    opcion_alumno = input("> ")
#                    if opcion_alumno == '1':
#                        self.insert_alumnos()
#                    elif opcion_alumno == '2':
#                        print('''
#                        Para actualizar: 
#                        -Debe de tener el IdAlumno, caso contrario regrese y escoja la opcion "Mostrar Alumno"
#                        ¿Tiene el IdAlumno? (Si = 1 , No = 2)
#                        ''')
#                        escoger = input('> ')
#                        if escoger == '1':
#                            self.update_alumnos()
#                        elif escoger == '2':
#                            return
#                        else:
#                            print('\nHas introducido una opción erronea')
#                    elif opcion_alumno == '3':
#                        self.delete_alumno()
#                    elif opcion_alumno == '4':
#                        self.fetchall_alumnos()
#                elif opcion == "2":
#                    print(
#                        '''\n¿Que deseas hacer en Docente?
#                    1) Agregar Docente
#                    2) Actualizar Docente
#                    3) Eliminar Docente
#                    4) Mostrar Docente
#                    '''
#                    )
#                    opcion_docente = input("> ")
#                    if opcion_docente == '1':
#                        self.insert_docente()
#                    elif opcion_docente == '2':
#                        print('''
#                        Para actualizar: 
#                        -Debe de tener el IdDocente, caso contrario regrese y escoja la opcion "Mostrar Docente"
#                        ¿Tiene el IdDocente? (Si = 1 , No = 2)
#                        ''')
#                        escoger = input('> ')
#                        if escoger == '1':
#                            self.update_docente()
#                        elif escoger == '2':
#                            return
#                        else:
#                            print('\nHas introducido una opción erronea')
#                    elif opcion_docente == '3':
#                        self.delete_docente()
#                    elif opcion_docente == '4':
#                        self.fetchall_docente()
#                elif opcion == "3":
#                    pass
#                elif opcion == "4":
#                    pass
#                elif opcion == "6":
#                    print('\nGracias por usar esta aplicación\n')
#                    sleep(2)
#                    quit()
#                else:
#                    print('\nHas introducido una opción erronea')
#
#class Inicio(Interfaz):
#    def __init__(self):
#        self.interfaz()
#
#Inicio()