from time import sleep
from colegio import Alumno, Docente, Curso, Salon, Seccion, Grado, Anio_Escolar, Docente_Curso, Periodo_Evaluacion_Detalle, Periodo_Evaluacion, Grado_Nivel,Grado_Nivel_Seccion, Ubicacion, Asignacion_Alumno, Asignacion_Docente

class Interfaz(Alumno, Docente, Curso, Salon, Seccion, Grado, Anio_Escolar, Docente_Curso, Periodo_Evaluacion_Detalle, Periodo_Evaluacion, Grado_Nivel,Grado_Nivel_Seccion, Ubicacion, Asignacion_Alumno, Asignacion_Docente):
    def interfaz(self):

        print('''\nBienvenido al Menú Principal del Colegio
        ¿Que deseas hacer?
        1) Interfaz Alumno
        2) Asignar Docente - Salon
        3) Asignar Docente - Curso
        4) Mantenimiento
        5) Distribución de Salones
        6) Reportes
        7) Salir del programa''')
        opcion_principal = input('> ')

        if opcion_principal == '1':
            print('''\n¿Que deseas hacer?
            1) Mostrar alumnos matriculados 
            2) Matricular Alumno
            3) Modificar matricula del alumno
            4) Modulo de Notas del Alumno''')

            opcion_matricula = input('Ingrese la opción: ')

            if opcion_matricula == '1':

                self.fetchall_TB_Alumno_doc_salon()
            
            elif opcion_matricula == '2':

                # IdAlumno - IdAsigDoc
                print('\nElegir alumno:')
                self.fetchall_alumnos()

                Idalumno = int(input('Elegir el alumno: '))

                print('\nElegir Docente con su salón')
                self.fetchall_TB_asignacion_Docente_salon()

                IdAsig_Doc = int(input('Elegir al docente con el salón: '))

                asig_alumno = Asignacion_Alumno(Idalumno,IdAsig_Doc)

                asig_alumno.insert_TB_Asignacion_Alumno()

            elif opcion_matricula == '3':
                
                print('\nVer listado de matriculados\n')

                self.fetchall_TB_Alumno_doc_salon()

                modificacion_matricula = int(input('Elegir el alumno matriculado: '))

                print('\nEmpezamos a modificar :)\n')

                print('\n==Elegir alumno==\n')
                self.fetchall_alumnos()

                Idalumno = int(input('Elegir el alumno: '))

                print('\n==Elegir Docente con su salón==\n')
                self.fetchall_TB_asignacion_Docente_salon()

                IdAsig_Doc = int(input('Elegir al docente con el salón: '))

                asig_alumno = Asignacion_Alumno(Idalumno,IdAsig_Doc)

                asig_alumno.update_TB_Asignacion_Alumno(modificacion_matricula)

            elif opcion_matricula == '4':

                print('''\n¿Que deseas hacer?
                1) Mostrar los alumnos con sus notas
                2) Ingresar notas del alumno
                3) Modificar notas del alumno''')

                opcion_nota = input('Ingrese la opción: ')

                if opcion_nota == '1':
                
                    self.fetchall_TB_Per_Eval_Det()
                
                elif opcion_nota == '2':
                    
                    print('\n==Elegir alumno matriculado==\n')

                    self.fetchall_TB_Alumno_doc_salon()

                    IdAsignacion_Alumno = int(input('Elegir al alumno matriculado: '))

                    print('\n==Elegir Periodo Evaluación==\n')

                    self.fetchall_Periodo_Evaluacion()

                    IdPeriodoEval = int(input('Elegir el periodo de evaluación: '))

                    nota = int(input('Ingresar nota del alumno: '))

                    asignar_nota = Periodo_Evaluacion_Detalle(IdAsignacion_Alumno,IdPeriodoEval,nota)

                    asignar_nota.insert_TB_Per_Eval_Det()

                elif opcion_nota == '3':

                    print('\nVer listado de matriculados con sus notas\n')

                    self.fetchall_TB_Per_Eval_Det()

                    fin = int(input('Elegir el alumno matriculado: '))

                    print('\nEmpezamos a modificar :)\n')

                    print('\n==Elegir alumno matriculado==\n')

                    self.fetchall_TB_Alumno_doc_salon()

                    IdAsignacion_Alumno = int(input('Elegir al alumno matriculado: '))

                    print('\n==Elegir Periodo Evaluación==\n')

                    self.fetchall_Periodo_Evaluacion()

                    IdPeriodoEval = int(input('Elegir el periodo de evaluación: '))

                    nota = int(input('Ingresar nota del alumno: '))

                    asignar_nota = Periodo_Evaluacion_Detalle(IdAsignacion_Alumno,IdPeriodoEval,nota)

                    asignar_nota.update_TB_Per_Eval_Det(fin)

        elif opcion_principal == '2':
            print('''\n¿Que deseas hacer?
            1) Mostrar Asignación Docente - Salon 
            2) Ingresar en Asignación Docente - Salon
            3) Actualizar Asignación Docente - Salon''')

            opcion_asig_doc_curso = input ('> ')

            if opcion_asig_doc_curso == '1':

                self.fetchall_TB_asignacion_Docente_salon()

            elif opcion_asig_doc_curso == '2':

                self.fetchall_TB_Docente_Curso()

                IdcursoDocente = int(input('Ingrese el IdDocenteCurso: '))

                self.fetchall_ubicacion()

                IdUbicacion = int(input('Ingrese el IdUbicacion: '))

                asig_docente = Asignacion_Docente(IdcursoDocente, IdUbicacion)

                asig_docente.insert_TB_Asignacion_Docente()

            elif opcion_asig_doc_curso == '3':

                self.fetchall_TB_Docente_Curso()

                Idasigdocente = int(input('Ingrese la opción para modificar: '))

                print('\nEmpecemos a modificar :)')

                self.fetchall_TB_Docente_Curso()

                IdcursoDocente = int(input('Ingrese el IdDocenteCurso: '))

                self.fetchall_ubicacion()

                IdUbicacion = int(input('Ingrese el IdUbicacion: '))

                asig_docente = Asignacion_Docente(IdcursoDocente, IdUbicacion)

                asig_docente.update_TB_Asignacion_Docente(Idasigdocente)
            
            else:
                
                print('\nHas introducido una opción erronea')

        elif opcion_principal == '3':
            print('''\n¿Que deseas hacer?
            1) Mostrar Asignación Docente 
            2) Ingresar en Asignación Docente
            3) Actualizar Asignación Docente''')

            opcion_asig_doc_curso = input ('> ')

            if opcion_asig_doc_curso == '1':

                self.fetchall_TB_Docente_Curso()

            elif opcion_asig_doc_curso == '2':

                self.fetchall_docente()

                IdDocente = int(input('Ingrese el IdDocente: '))

                self.fetchall_TB_curso()

                IdCurso = int(input('Ingrese el IdCurso: '))

                docente_curso = Docente_Curso(IdDocente, IdCurso)

                docente_curso.insert_TB_Docente_Curso()

            elif opcion_asig_doc_curso == '3':

                self.fetchall_TB_Docente_Curso()

                IdDocenteCurso = int(input('Ingrese la opción para modificar: '))

                print('\nEmpecemos a modificar :)')

                self.fetchall_docente()

                IdDocente = int(input('Ingrese el IdDocente: '))

                self.fetchall_TB_curso()

                IdCurso = int(input('Ingrese el IdCurso: '))

                docente_curso = Docente_Curso(IdDocente, IdCurso)

                docente_curso.update_TB_Docente_Curso(IdDocenteCurso)
            
            else:

                print('\nHas introducido una opción erronea')

        elif opcion_principal == '4':
            print('''\n¿Que deseas hacer?
            1) Modulo Alumno
            2) Modulo Docente
            3) Modulo Curso
            4) Modulo Recursos''')
            opcion = input("> ")
            if opcion == "1":
                print(
                    '''\n¿Que deseas hacer en Alumno?
                1) Agregar Alumno
                2) Actualizar Alumno
                3) Eliminar Alumno
                4) Mostrar Alumno
                '''
                )
                opcion_alumno = input("> ")
                if opcion_alumno == '1':
                    self.insert_alumnos()
                elif opcion_alumno == '2':
                    print('''
                    Para actualizar: 
                    -Debe de tener el IdAlumno, caso contrario regrese y escoja la opcion "Mostrar Alumno"
                    ¿Tiene el IdAlumno? (Si = 1 , No = 2)
                    ''')
                    escoger = input('> ')
                    if escoger == '1':
                        self.update_alumnos()
                    elif escoger == '2':
                        return
                    else:
                        print('\nHas introducido una opción erronea')
                elif opcion_alumno == '3':
                    self.delete_alumno()
                elif opcion_alumno == '4':
                    self.fetchall_alumnos()
            elif opcion == "2":
                print(
                    '''\n¿Que deseas hacer en Docente?
                1) Agregar Docente
                2) Actualizar Docente
                3) Eliminar Docente
                4) Mostrar Docente
                '''
                )
                opcion_docente = input("> ")
                if opcion_docente == '1':
                    self.insert_docente()
                elif opcion_docente == '2':
                    print('''
                    Para actualizar: 
                    -Debe de tener el IdDocente, caso contrario regrese y escoja la opcion "Mostrar Docente"
                    ¿Tiene el IdDocente? (Si = 1 , No = 2)
                    ''')
                    escoger = input('> ')
                    if escoger == '1':
                        self.update_docente()
                    elif escoger == '2':
                        return
                    else:
                        print('\nHas introducido una opción erronea')
                elif opcion_docente == '3':
                    self.delete_docente()
                elif opcion_docente == '4':
                    self.fetchall_docente()
            elif opcion == "3":
                try:
                    while True:
                        print(
                            '''\n¿Que deseas hacer en Curso?
                        1) Agregar Curso
                        2) Actualizar Curso
                        3) Eliminar Curso
                        4) Mostrar Curso
                        '''
                        )
                        opcion_curso = input("> ")
                        if opcion_curso == '1':
                            self.insert_TB_Cursos()

                            print('\n¿Deseas matricular curso en docentes?')
                            print('\n(Si = 1, No = 2)')
                            asignar = input('> ')
                            if asignar == '1':
                                self.fetchall_docente()

                                IdDocente = int(input('Ingrese el IdDocente: '))

                                self.fetchall_TB_curso()

                                IdCurso = int(input('Ingrese el IdCurso: '))

                                docente_curso = Docente_Curso(IdDocente, IdCurso)

                                docente_curso.insert_TB_Docente_Curso()

                            elif asignar == '2':
                                pass

                        elif opcion_curso == '2':

                            self.update_TB_Cursos()

                        elif opcion_curso == '3':
                            print('¿Estas seguro que deseas eliminar? (Si = 1 , No = 2)')
                            eliminar = input('> ')
                            if eliminar == '1':
                                self.delete_TB_Cursos()
                            elif eliminar == '2':
                                pass
                            else:
                                print('\nHas introducido una opción erronea')
                        elif opcion_curso == '4':
                            self.fetchall_TB_curso()
                except Exception as e:
                    print(f'{str(e)}')
            elif opcion == "4":
                print(
                    '''\n¿Que deseas hacer en el Modulo de Recursos?
                1) Modulo Salones
                2) Modulo Secciones
                3) Modulo Grado - Seccion
                4) Modulo Año Escolar
                5) Modulo Periodo Evaluación
                '''
                )
                opcion_recursos = input('> ')
                if opcion_recursos == '1':

                    print(
                        '''\n¿Que deseas hacer en el Modulo de Recursos?
                    1) Mostrar Salones
                    2) Ingresar Salones
                    3) Actualizar Salones
                    4) Eliminar Salones
                    '''
                    )
                    opcion_salon = input('> ')

                    if opcion_salon == '1':
                        self.fetchall_Salon()
                    elif opcion_salon == '2':
                        
                        self.fetchall_Salon()

                        salon = int(input('Ingresar el nuevo salón: '))

                        salones = Salon(salon)

                        salones.insert_TB_salon()

                    elif opcion_salon == '3':
                        
                        self.fetchall_Salon()

                        IdSalon = int(input('Ingresar el IdSalon: '))

                        print('\nEmpecemos a actualizar :)')

                        salon = int(input('Ingresar el nuevo número del salón: '))

                        salones = Salon(salon)

                        salones.update_TB_salon(IdSalon)

                    elif opcion_salon == '4':
                        
                        self.fetchall_Salon()

                        IdSalon = int(input('Ingresar el IdSalon para eliminar: '))

                        self.delete_TB_salon(IdSalon)

                elif opcion_recursos == '2':
                    
                    print(
                        '''\n¿Que deseas hacer en el Modulo de Recursos?
                    1) Mostrar Secciones
                    2) Ingresar Secciones
                    3) Actualizar Secciones
                    4) Eliminar Secciones
                    '''
                    )
                    opcion_Secciones = input('> ')

                    if opcion_Secciones == '1':

                        self.fetchall_Salon()

                    elif opcion_Secciones == '2':
                        
                        self.fetchall_TB_Seccion()

                        seccion = input('Ingresar la nueva sección: ')

                        secciones = Seccion(seccion)

                        secciones.insert_TB_Seccion()

                    elif opcion_Secciones == '3':
                        
                        self.fetchall_TB_Seccion()

                        IdSeccion = int(input('Ingresar el IdSeccion: '))

                        print('\nEmpecemos a actualizar :)')

                        seccion = int(input('Ingresar la nueva sección: '))

                        secciones = Seccion(seccion)

                        secciones.update_TB_Seccion(IdSeccion)

                    elif opcion_Secciones == '4':
                        
                        self.fetchall_Salon()

                        IdSeccion = int(input('Ingresar el IdSeccion para eliminar: '))

                        self.delete_TB_Seccion(IdSeccion)

                elif opcion_recursos == '3':
                    print(
                        '''\n¿Que deseas hacer en el Modulo de Recursos?
                    1) Mostrar Grado - Seccion
                    2) Insertar Grado - Seccion
                    3) Actualizar Grado - Seccion
                    '''
                    )
                    opcion_grado_nivel = input('> ')
                    if opcion_grado_nivel == '1':
                        self.fetchall_TB_grado_seccion()
                    elif opcion_grado_nivel == '2':
                        print('\nLista de Grado - Nivel')

                        self.fetchall_TB_Grado_Nivel()

                        Idgradosnivel = int(input('Ingrese el Idgradosnivel: '))

                        print('\nLista de Sección: ')

                        self.fetchall_TB_Seccion()

                        IdSeccion = int(input('Ingrese el IdSeccion: '))

                        print('\nLista de Año Escolar: ')

                        self.fetchall_anio_escolar()

                        IdAnioEscolar = int(input('Ingrese el IdAnioEscolar: '))

                        grado_seccion = Grado_Nivel_Seccion(Idgradosnivel, IdSeccion, IdAnioEscolar)

                        grado_seccion.insert_TB_Grado_Nivel_Seccion()
                    
                    elif opcion_grado_nivel == '3':

                        print('\nQue es lo que desea modificar?')

                        self.fetchall_TB_grado_seccion()

                        Idgradoseccion = int(input('Ingrese la opción ha modificar: '))

                        print('\nPasemos ha actualizar :)')

                        print('\nLista de Grado - Nivel')

                        self.fetchall_TB_Grado_Nivel()

                        Idgradosnivel = int(input('Ingrese el Idgradosnivel: '))

                        print('\nLista de Sección: ')

                        self.fetchall_TB_Seccion()

                        IdSeccion = int(input('Ingrese el IdSeccion: '))

                        print('\nLista de Año Escolar: ')

                        self.fetchall_anio_escolar()

                        IdAnioEscolar = int(input('Ingrese el IdAnioEscolar: '))

                        update_grados_seccion = Grado_Nivel_Seccion(Idgradosnivel, IdSeccion, IdAnioEscolar)

                        update_grados_seccion.update_TB_Grado_Nivel_Seccion(Idgradoseccion)

                elif opcion_recursos == '4':
                    pass                            
                elif opcion_recursos == '5':
                    pass
            elif opcion == "6":
                print('\nGracias por usar esta aplicación\n')
                sleep(2)
                quit()
            else:
                print('\nHas introducido una opción erronea')
        elif opcion_principal == '5':
            print('''\n¿Que deseas en el Modulo de Distribución de Salones?
            1) Mostrar Distribución
            2) Ingresar Distribución
            3) Actualizar Distribución''')
            opcion_distribucion = input('> ')
            if opcion_distribucion == '1':

                self.fetchall_ubicacion()

            elif opcion_distribucion == '2':

                print('\nLista de Grados - Sección: ')

                self.fetchall_TB_grado_seccion()

                id_grados_nivel = int(input('Ingrese el id_grados_nivel: '))

                print('\nLista de Salones: ')

                self.fetchall_Salon()

                id_salon = int(input('Ingrese el id_salon: '))

                ubicaciones = Ubicacion(id_grados_nivel, id_salon)

                ubicaciones.insert_ubicacion()

            elif opcion_distribucion == '3':
                print('\nLista de Distribución')

                self.fetchall_ubicacion()

                IdUbicacion = int(input('Ingrese el IdUbicacion: '))

                print('\nLista de Grados - Sección: ')

                self.fetchall_TB_grado_seccion()

                id_grados_nivel = int(input('Ingrese el id_grados_nivel: '))

                print('\nLista de Salones: ')

                self.fetchall_Salon()

                id_salon = int(input('Ingrese el id_salon: '))

                ubicaciones = Ubicacion(id_grados_nivel, id_salon)

                ubicaciones.update_ubicacion(IdUbicacion)

class Inicio(Interfaz):
    def __init__(self):
        self.interfaz()

Inicio()