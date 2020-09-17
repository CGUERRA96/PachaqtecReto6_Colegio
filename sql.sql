--Mostrar Docente - Curso
Select dc.iddocentecurso ,d.Nombre_docente, cs.nombrecurso 
from tb_docente_curso DC
left join tb_docente D on dc.iddocente = d.iddocente
left join tb_cursos Cs on Cs.idcurso = dc.idcurso;

--Mostrar Grado - Nivel

Select gn.idgradonivel, gr.nombre_grado, nv.nombre_nivel 
from tb_grado_nivel gn
left join tb_grado gr on gr.idgrado = gn.idgrado
left join tb_nivel nv on nv.idnivel = gn.idnivel;

--Mostrar Grado - Nivel - Seccion

Select gns.idgradoseccion, gr.nombre_grado, nv.nombre_nivel, sc.nombre_seccion, ae.anio_escolar
from tb_grado_nivel_seccion gns
left join tb_grado_nivel gn on gns.idgradosnivel = gn.idgradonivel
left join tb_grado gr on gr.idgrado = gn.idgrado
left join tb_nivel nv on nv.idnivel = gn.idnivel
left join tb_seccion sc on gns.idseccion = sc.idseccion
left join tb_anio_escolar ae on gns.idanioescolar = ae.idanioescolar;

--Mostrar Ubicación

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

--Asignacion Docente

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