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

    #def insert_alumnos(self):
    #    try:
    #        conn = Connection()
    #        query = f''''''
    #    except expression as identifier:
    #        pass

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
                print(f'Idcurso = {row[0]}')
                print(f'nombrecurso = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

curso = Curso('Literatura')
curso.fetchall_TB_curso()

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
                print(f'IdSalon = {row[0]}')
                print(f'num_salon = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

salon = Salon(103)
salon.fetchall_Salon()

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
                print(f'IdSeccion = {row[0]}')
                print(f'Nombre_Seccion = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

seccion = Seccion('A')
seccion.fetchall_TB_Seccion()

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
                print(f'IdAnioEscolar = {row[0]}')
                print(f'anio_escolar = {row[1]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

anios_escolares = Anio_Escolar('2020')
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
                print(f'IdPeriodoEval = {row[0]}')
                print(f'nombretiempo = {row[1]}')
                print('=============================')
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
                SELECT * FROM TB_Grado_Nivel;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdGradoNivel = {row[0]}')
                print(f'IdGrado = {row[1]}')
                print(f'IdNivel = {row[2]}')
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
                SELECT * FROM TB_Grado_Nivel_Seccion;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'Idgradoseccion = {row[0]}')
                print(f'Idgradosnivel = {row[1]}')
                print(f'IdSeccion = {row[2]}')
                print(f'IdAnioEscolar = {row[3]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

grado_seccion = Grado_Nivel_Seccion(1,1,1)
grado_seccion.fetchall_TB_grado_seccion()


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
                SELECT * FROM TB_UBICACION;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdUbicacion = {row[0]}')
                print(f'Id_grados_nivel = {row[1]}')
                print(f'Id_salon = {row[2]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

ubicacion = Ubicacion(1,1)
ubicacion.fetchall_ubicacion()

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
                SELECT * FROM TB_Docente_Curso;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'Iddocentecurso = {row[0]}')
                print(f'IdDocente = {row[1]}')
                print(f'IdCurso = {row[2]}')                
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

docente_curso = Docente_Curso(1,1)
docente_curso.fetchall_TB_Docente_Curso()


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
                SELECT * FROM TB_Asignacion_Docente;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'Idasigdocente = {row[0]}')
                print(f'IdcursoDocente = {row[1]}')
                print(f'IdUbicacion = {row[2]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

asig_doc = Asignacion_Docente(1,1)
asig_doc.fetchall_TB_asignacion_Docente_salon()


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
                SELECT * FROM TB_Asignacion_Alumno;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdAlumnodocsalon = {row[0]}')
                print(f'Idalumno = {row[1]}')
                print(f'Idasigdoc = {row[2]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

asig_alumn = Asignacion_Alumno(1,1)
asig_alumn.fetchall_TB_Alumno_doc_salon()

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
                SELECT * FROM TB_Per_Eval_Det;
            '''
            cursor = conn.execute_query(query)
            rows = cursor.fetchall()

            for row in rows:
                print(f'IdDocente = {row[0]}')
                print(f'IdPeriodoEval = {row[1]}')
                print(f'nota = {row[2]}')
                print('=============================')
        except Exception as e:
            print(f'{str(e)}')

fin = Periodo_Evaluacion_Detalle(1,1,17)
fin.fetchall_TB_Per_Eval_Det()