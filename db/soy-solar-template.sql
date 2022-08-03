-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Server version: 10.8.3-MariaDB
-- PHP Version: 8.1.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `soy-solar-template`
--

-- --------------------------------------------------------

--
-- Table structure for table `careers`
--

CREATE TABLE `careers` (
  `id_career` int(11) NOT NULL,
  `name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `careers`
--

INSERT INTO `careers` (`id_career`, `name`) VALUES
(1, 'INGC'),
(2, 'DERR'),
(3, 'CPUA'),
(4, 'MCPA'),
(5, 'INEN'),
(6, 'LGER'),
(7, 'LISP'),
(8, 'LIDA'),
(9, 'LHAR'),
(10, 'LIEL'),
(11, 'MAAE'),
(12, 'DAEN'),
(13, 'MIGA'),
(14, 'MATT'),
(15, 'DOTT'),
(16, 'LIHA'),
(17, 'LCOP'),
(18, 'NANO'),
(19, 'LIAN'),
(20, 'MACO'),
(21, 'LNTO'),
(22, 'MCPE'),
(23, 'MCOP'),
(24, 'DERC'),
(25, 'MMOT'),
(26, 'DAGE'),
(27, 'MGGL'),
(28, 'LICF'),
(29, 'DDHU'),
(30, 'DECH'),
(31, 'EMFM'),
(32, 'EMUR'),
(33, 'MBIO'),
(34, 'DAE'),
(35, 'MCAE'),
(36, 'DAYE'),
(37, 'INEL'),
(38, 'INAN'),
(39, 'LHIA'),
(40, 'LIAR'),
(41, 'MUTT'),
(42, 'DIMS'),
(43, 'DIMS'),
(44, 'LESL'),
(45, 'MCIU');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id_question` int(11) NOT NULL,
  `question` varchar(1000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `answer` varchar(10000) COLLATE utf8mb4_unicode_ci NOT NULL,
  `keyword` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id_stage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`id_question`, `question`, `answer`, `keyword`, `id_stage`) VALUES
(1, '¿Cuál es el reglamento del estudiante?', 'REGLAMENTO ESTUDIANT \\nCON GUSTO, TE COMPARTO EL ENLACE DONDE PUEDES ENCONTRAR LA NORMATIVA GENERAL DE LA UNIVERSIDAD DE GUADALAJARA:\\n  🗡️', 'reglamentoestudiante', 1),
(2, '¿Qué procede en caso de estar en artículo 34?', 'ARTÍCULO 34\r\nRESPUESTA:\r\n¡CLARO! Aquí en este documento podrás encontrar toda la información referente al artículo 34 en las páginas 5 y 6: ', 'articulo34', 1),
(3, '¿A dónde puedo dirigirme para tramitar la credencial de estudiante? (¿Qué sucede si perdí mi credencial de estudiante?)', 'CREDENCIAL ESTUDIANTE\nCON GUSTO TE COMPARTO EL LINK DE LA PAGINA DONDE PODRÁS REALIZAR TU TRÁMITE  ', 'credencialestudiante', 1),
(4, '¿Cuáles son los horarios de atención en el sistema de control escolar?', 'HORARIOS CONTROL ESCOLAR\r\nCON GUSTO TE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS LA INFORMACIÓN QUE DESEAS  ', 'horarioscontrolescolar', 1),
(5, '¿Cómo puedo obtener el acceso a la biblioteca digital?', 'BIBLIOTECA DIGITAL\r\nEN EL SIGUIENTE LINK TE COMPARTO LA INFORMACIÓN  ', 'bibliotecadigital', 1),
(6, '¿Dónde puedo consultar la malla curricular?', 'MALLA CURRICULAR\r\nDE ACUERDO, TE COMPARTO EL LINK DONDE ENCONTRARÁS LA MALLA DE TU CARRERA \r\n ', 'mallacurricular', 1),
(7, '¿Dónde obtengo información sobre el centro global de idiomas?', 'CENTRO GLOBAL DE IDIOMAS\r\nDE ACUERDO, TE COMPARTO EL SIGUIENTE LINK DONDE  PODRÁS ENCONTRAR LA INFORMACIÓN: ', 'centroglobaldeidiomas', 1),
(8, '¿Cuál es el horario de atención del centro global de idiomas?', 'HORARIO DE CENTRO GLOBAL DE IDIOMAS\r\nCON GUSTO TE COMPARTO LA INFORMACIÓN EN EL SIGUIENTE LINK ', 'horariocentroglobaldeidiomas', 1),
(9, '¿Cómo pedir las instalaciones deportivas y culturales?', 'INSTALACIONES DEPORTIVAS/CULTURALES\r\nAQUÍ ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS\r\n ', 'instalacionesdeportivas', 1),
(10, '¿Cuáles son los horarios de la cineteca?', 'CINETECA\r\nPOR SUPUESTO, AQUÍ TIENES LA CARTELERA DE LA CINETECA: \r\n\r\n', 'cineteca', 1),
(11, '¿Qué requisitos se necesitan para tramitar la beca de intercambio?', 'BECAS INTERCAMBIO\r\nCON GUSTO TE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS EL CONTACTO PARA PEDIR INFORMACIÓN ', 'becasintercambio', 2),
(12, '¿En cuántas becas me puedo inscribir?', 'BECAS\r\nCON GUSTO TE COMPARTO LA INFORMACIÓN, ESTAS SON LAS BECAS QUE PODRÍAS SOLICITAR:\r\n1 Apoyo alimentario\r\n2 Becarios CUT\r\n3 Movilidad\r\n', 'becas', 2),
(13, '¿Cada cuánto tiempo se abren las convocatorias?', 'CONVOCATORIAS\r\nCON GUSTO TE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS ', 'convocatorias', 2),
(14, '¿Cómo cursó una materia en otro centro universitario?', 'MATERIAS EN OTRO CENTRO\r\nRESPUESTAS:\r\nLA INFORMACIÓN  QUE BUSCAS ESTÁ RELACIONADA CON LA SIGUIENTE INFORMACIÓN \r\nMovilidad ', 'materiasenotrocentro', 2),
(15, 'Información sobre Movilidad estudiantil', 'MOVILIDAD ESTUDIANTIL\r\nRESPUESTA:\r\nCON GUSTO, LA INFORMACION QUE ESTAS BUSCANDO LA PODRÁS ENCONTRAR DE MANERA MÁS DETALLADA EN EL SIGUIENTE ENLACE:\r\nMovilidad \r\n', 'movilidadestudiantil', 2),
(16, '¿Cuáles son las becas que puedo solicitar?', 'SOLICITUD DE BECAS\nCON GUSTO TE COMPARTO LA INFORMACIÓN, ESTAS SON LAS BECAS QUE PODRÍAS SOLICITAR\no  Apoyo alimentario: http://www.cutonala.udg.mx/becas/alimentos\no   Becarios CUT http://cutonala.udg.mx/Becarios\no   Movilidad http://cutonala.udg.mx/Becarios', 'solicituddebecas', 2),
(17, '¿Cuándo puedo iniciar mi servicio?,¿Cuántos créditos necesito para iniciar mi servicio?', 'SERVICIO SOCIAL\r\nCON GUSTO TE COMPARTO EL LINK DONDE ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS  ', 'serviciosocial', 3),
(18, '¿Cómo puedo realizar mi servicio social?', 'SERVICIO SOCIAL\r\nCON GUSTO TE COMPARTO EL LINK DONDE ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS ', 'realizarserviciosocial', 3),
(19, '¿Cuál es el proceso de titulación?', 'TITULACIÓN\r\nEN ESTE LINK ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS  ', 'titulacion', 3),
(20, '¿A partir de cuándo puedo iniciar el proceso de titulación?', 'TITULACIÓN\r\nEN ESTE LINK ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS  ', 'creditostitulacion', 3),
(21, '¿Cuáles son las modalidades de titulación? ¿Qué hago si ya terminé mis créditos?', 'MODALIDADES TITULACIÓN\r\nEN ESTE LINK ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS ', 'modalidadestitulacion', 3),
(22, '¿Cuál es el reglamento general de titulación?', 'REGLAMENTO TITULACIÓN\r\nEN ESTE LINK ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS  ', 'reglamentotitulacion', 3),
(23, '¿Quién me puede ayudar en mi tesis? ', 'ASESOR TESIS\r\nEN ESTE LINK ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS ', 'asesortesis', 3),
(40, '¿Tengo derecho a extraordinario?', 'EXTRAORDINARIO\\r\\nCON GUSTO TE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS LA INFORMACIÓN QUE NECESITAS A PARTIR DEL CAPÍTULO V ', 'requisitosextraordinario', 1),
(41, '¿Cuántos son el mínimo de créditos que puedo inscribir por semestre?', 'MÍNIMO DE CRÉDITOS\\r\\nLA ADMINISTRACIÓN DE LOS PLANES DE ESTUDIO SE HARÁ EN BASE AL SISTEMA DE CRÉDITOS, DE CONFORMIDAD CON EL SIGUIENTE LINEAMIENTO: DEL TOTAL DE CRÉDITOS ESTABLECIDOS EN UN PLAN DE ESTUDIOS DEL NIVEL SUPERIOR, EL NÚMERO MÍNIMO DE CRÉDITOS A CURSAR EN UN CICLO ESCOLAR SERÁ DE 30, EL PROMEDIO DE 60 Y EL MÁXIMO DE 90 CRÉDITOS.\\r\\nPODRÁS ENCONTRAR MAS INFORMACIÓN EN EL REGLAMENTO GENERAL DE PLANES DE ESTUDIO  \\r\\n', 'creditosporsemestre', 1),
(42, '¿Cómo sé que una materia tiene prerrequisitos?', 'PRERREQUISITOS\\r\\nLOS PRERREQUISITOS, SON UNA SERIE DE NÚMEROS QUE INDICAN SI ES NECESARIO QUE TENGAS ACREDITADA OTRA MATERIA. SI ES QUE LOS HAY LOS PODRÁS ENCONTRAR JUSTO ARRIBA DEL NOMBRE DE LA MATERIA\\r\\n', 'requisitosmaterias', 1),
(43, '¿Quién es y dónde puedo encontrar al coordinador de mi carrera?', 'COORDINADOR CARRERA\\r\\nEN EL SIGUIENTE LINK PODRÁS ELEGIR LA LICENCIATURA, DOCTORADO O MAESTRÍA QUE ESTUDIAS Y ENCONTRARÁS EL CONTACTO DE TU COORDINADOR ', 'coordinadorcarrera', 1),
(44, '¿Cuál es el plazo para dar de baja una materia?', 'BAJA DE MATERIAS\\r\\nCON GUSTO TE COMPARTO EL LINK  DONDE PODRÁS ENCONTRAR LA INFORMACIÓN QUE NECESITAS EN EL ARTÍCULO OCTAVO DEL CAPÍTULO XIII ARTÍCULOS TRANSITORIOS', 'bajademateria', 1),
(45, '¿Dónde puedo consultar el calendario escolar? ¿Cuáles el calendario de los días festivos?', 'CALENDARIO ESCOLAR\\r\\nCON GUSTO TE COMPARTO EL LINK DONDE PODRÁS ENCONTRAR LOS CALENDARIOS ESCOLARES ', 'calendarioescolar', 1),
(46, '¿Qué es la semana de la ciencia?', 'SEMANA CIENCIA\\r\\n CON GUSTO TE COMPARTO EL SIGUIENTE LINK  DONDE ENCONTRÁS MAYOR INFORMACIÓN ACERCA DEL TEMA DE TU INTERÉS\\r\\n', 'semanaciencia', 1),
(47, '¿Cuándo se abre la agenda para registrar las materias?', 'REGISTRO MATERIAS/AGENDA\\r\\nPARA SABER CUANDO SE ABRE TU REGISTRO DE MATERIAS TENDRÁS QUE INGRESAR Al link  EN EL APARTADO DE REGISTRO-AGENDA', 'registromaterias', 1),
(48, '¿Hasta qué fecha puedo liquidar la orden de pago?', 'ORDEN DE PAGO\\r\\nLA FECHA LÍMITE DE PAGO VIENE DETALLADA EN LA ORDEN DE PAGO CORRESPONDIENTE AL SEMESTRE EN CURSO', 'ordendepago', 1),
(49, '¿Cómo puedo solicitar ayuda psicológica o ayuda/atención médica?', 'APOYO PSICOLÓGICO/MÉDICO\\r\\nTE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS EL CONTACTO DEL CONSULTORIO MÉDICO DE LA UNIVERSIDAD ', 'apoyopsicologico', 1),
(50, '¿Qué pasa si tengo una crisis?', 'CRISIS\\r\\nEN CASO DE UNA CRISIS, TE PUEDES COMUNICAR AL NÚMERO 3338333838 CON EL CENTRO DE INTERVENCIÓN EN CRISIS', 'crisis', 1),
(51, '¿A quién le informo si tengo un tratamiento médico especial?', 'TRATAMIENTO MÉDICO\\r\\nTE COMPARTO EL SIGUIENTE LINK DONDE ENCONTRARÁS EL CONTACTO DEL CONSULTORIO MÉDICO DE LA UNIVERSIDAD ', 'tratamientomedico', 1),
(52, '¿Cómo puedo solicitar el apoyo de becarios?, ¿Cómo puedo ser becario?', 'BECARIOS\\r\\nCON GUSTO TE COMPARTO EL SIGUIENTE LINK DONDE PODRÁS INFORMARTE ACERCA DEL PROGRAMA ', 'becarios', 2),
(53, '¿Dónde puedo consultar las ofertas de plazas del servicio social?', 'PLAZAS SERVICIO SOCIAL\\r\\nDEBERÁS INICIAR SESIÓN EN  CON TU CÓDIGO Y CONTRASEÑA DE ESTUDIANTE', 'plazasserviciosocial', 3),
(54, '¿Cuándo puedo iniciar mis prácticas profesionales?,¿Cuántos créditos necesito para iniciar mis prácticas profesionales?', 'REQUISITOS PRÁCTICAS PROFESIONALES\\r\\nDEBERÁS INGRESAR AL SIGUIENTE LINK  DONDE PODRÁS ENCONTRAR LA LICENCIATURA QUE CURSAS Y EN EL APARTADO DE “ACERCA DEL PROGRAMA” SE TE INDICARÁ LA OPCIÓN “PRÁCTICAS PROFESIONALES', 'practicasprofesionales', 3),
(55, '¿Dónde puedo consultar información acerca de vacantes en las empresas? (bolsa de trabajo)', 'BOLSA TRABAJO\\r\\nEN EL SIGUIENTE LINK DEBERÁS ELEGIR LA LICENCIATURA QUE ESTÁS CURSANDO Y EN EL APARTADO DE “ACERCA DEL PROGRAMA” ENCONTRARÁS LA OPCIÓN “BOLSA DE TRABAJO', 'bolsatrabajo', 3),
(56, '¿Qué requisitos necesito de las vacantes de la bolsa de trabajo?', 'REQUISITOS BOLSA TRABAJO\\r\\nPARA PODER BRINDARTE EL CONTACTO QUE TE DARÁ LA INFORMACIÓN EXACTA TIENES QUE INGRESAR AL SIGUIENTE LINK  DEBERÁS ELEGIR LA LICENCIATURA QUE ESTÁS CURSANDO Y EN EL APARTADO DE “ACERCA DEL PROGRAMA” ENCONTRARÁS LA OPCIÓN “BOLSA DE TRABAJO', 'requisitosbolsatrabajo', 3),
(57, '¿Qué requisitos necesito para la titulación?', 'REQUISITOS TITULACIÓN\\r\\nCON GUSTO TE COMPARTO LOS REQUISITOS (ICCO)\\r\\n1.	Haber obtenido los siguientes créditos en las áreas de formación:\\r\\nÁrea de Formación Básica Común Obligatoria	126 Créditos\\r\\n Área de Formación Básica Particular Obligatoria	135 Créditos\\r\\nÁrea de Formación Especializante Obligatoria	36 Créditos\\r\\nÁrea de Formación Especializante Selectiva	18 Créditos\\r\\nÁrea de Formación Optativa Abierta	18 Créditos\\r\\nNúmero mínimo total de créditos	 333 Créditos\\r\\n', 'requisitostitulacion', 3),
(62, '¿Qué es una estancia académica?', 'ESTANCIA ACADÉMICA\r\nCONSISTE EN LA ASISTENCIA REGULAR A CLASES EN OTRA INSTITUCIÓN NACIONAL O EXTRANJERA DURANTE UNO O DOS SEMESTRES (EN EL CASO DE LICENCIATURA, EL ESTUDIANTE PUEDE CURSAR HASTA 1 AÑO)\r\nPARA MAYOR INFORMACION PUEDES CONSULTAR EL SIGUIENTE LINK HTTP://CI.CGAI.UDG.MX/ES/ESTUDIANTES/UDG/INTERCAMBIO/ESTANCIA_ASIG_1', 'estanciaacademica', 2),
(63, '¿Qué becas hay de idiomas?', 'BECAS DE IDIOMAS\r\nLAS BECAS QUE SE PUEDEN SOLICITAR SON EN JOBS, BUSUU Y PROULEX', 'idiomas', 2),
(64, '¿Qué tipos de becas hay?', 'TIPOS DE BECAS\r\nHAY BECA POR RENDIMIENTO, BECA DE APOYO ECONÓMICO, BECA DE APOYO SOCIAL Y BECAS PARA PROGRAMAS INTERNACIONALES', 'tiposbecas', 2),
(65, '¿Qué beneficios ofrece la beca Manutención?', 'BECA MANUTENCIÓN\r\nLA BECA FEDERAL PARA APOYO A LA MANUTENCIÓN CONSISTE EN UN APOYO ECONÓMICO POR UN MONTO TOTAL DE HASTA $9,000.00 (NUEVE MIL PESOS 00/100 M.N.) DISTRIBUIDOS EN HASTA 5 PAGOS CORRESPONDIENTES A 5 BIMESTRES DE HASTA $1,800.00 (MIL OCHOCIENTOS PESOS 00/100 M.N.) CADA UNO', 'beneficiosmanutencion', 2),
(66, '¿Cuáles son los requisitos para solicitar la beca Excelencia?', 'BECA EXCELENCIA\r\nEL REQUISITO PARA LA BECA DE EXCELENCIA ES SER POSTULADO POR EL RECTOR DEL CENTRO UNIVERSITARIO DONDE ESTUDIES', 'requisitosexcelencia', 2),
(67, '¿Cuándo sale la convocatoria para la beca Excelencia?', 'BECA EXCELENCIA\r\nLA CONVOCATORIA SE ABRE ANUALMENTE, POR LO GENERAL, EN LOS MESES DE SEPTIEMBRE U OCTUBRE', 'convocatioriaexcelencia', 2),
(68, '¿Cuáles son los requisitos para solicitar la Beca Apoyos a Grupos Vulnerables?', 'BECA VULNERABLES\r\nSER ALUMNO DE LA UNIVERSIDAD DE GUADALAJARA, CONTAR CON UN PROMEDIO DE 8.0 Y FORMAR PARTE DE ALGÚN GRUPO VULNERABLE', 'gruposvulnerables', 2),
(69, '¿Cuáles son los requisitos para solicitar la beca de manutención?\r\n', 'BECA MANUTENCIÓN\r\nSER MEXICANO, ESTAR INSCRITO EN UNA IPES DE JALISCO PARA CONTINUAR O INICIAR ESTUDIOS DE NIVEL SUPERIOR Y PROVENIR DE UN HOGAR CUYO INGRESO SEA IGUAL O MENOR A CUATRO SALARIOS MÍNIMOS PER CÁPITA MENSUALES', 'requisitosmanutencion', 2),
(70, '¿Qué beneficios ofrece la  Beca de Excelencia?', 'BECA EXCELENCIA\r\nLOS ESTUDIANTES BENEFICIADOS RECIBIRÁN ESTÍMULO ECONÓMICO POR LA CANTIDAD DE: $3,080.40 MENSUALES Y ESTÁN COMPROMETIDOS A REALIZAR ACTIVIDADES EXTRACURRICULARES DE APOYO A LA MODALIDAD POR LA QUE RESULTARON DICTAMINADOS POR UN PERIODO DE 5 MESES', 'beneficiosexcelencia', 2),
(71, '¿Cuáles son los requisitos para solicitar la Beca Santander Iberoamérica de Grado?', 'BECA SANTANDER\r\nTENER UN PROMEDIO MÍNIMO DE 8.5, HABER CURSADO, AL MENOS, EL 40% DE LOS CRÉDITOS DE TU PROGRAMA ACADÉMICO Y CONTAR CON LA ACEPTACIÓN DE LA UNIVERSIDAD DONDE SE QUIERA REALIZAR LA ESTANCIA, PARA PARTICIPAR EN ALGUNO DE SUS PROGRAMAS DE ESTUDIO', 'requisitossantander', 2),
(72, '¿Cómo aplico para la Beca Santander Iberoamérica de Grado?', 'BECA SANTANDER\r\nLLENA TU SOLICITUD EN LÍNEA EN LA PÁGINA ELECTRÓNICA DE LA\r\n', 'becasantander', 2),
(73, '¿Qué pasa si repruebo por primera vez una materia?', 'REPROBAR MATERIAS\nTIENES QUE AGENDARLA EN EL SEMESTRE SIGUIENTE AL QUE LA REPROBASTE, SI DEJAS PASAR UN SEMESTRE DESPUÉS DE REPROBARLA SIN AGENDARLA CAERÁS EN BAJA DE LA LICENCIATURA POR ARTÍCULO 33', 'reprobar', 1),
(74, '¿Qué hacer si me aplicaron baja por artículo 33?', 'ARTÍCULO 33\r\nCON GUSTO TE PROPORCIONO EL LINK DONDE ENCONTRARAS LA INFORMACIÓN QUE NECESITAS ', 'articulo33', 1),
(75, '¿Cuándo puedo solicitar un justificante por inasistencias a clase?', 'JUSTIFICANTE\r\nPOR ENFERMEDAD, POR PARTICIPAR EN ALGUNA ACTIVIDAD ACADÉMICA RELACIONADA CON TU CARRERA, SIEMPRE Y CUANDO EL COORDINADOR DE LA CARRERA TENGA CONOCIMIENTO PREVIO Y POR CAUSA DE FUERZA MAYOR JUSTIFICADA QUE IMPIDA AL ALUMNO ASISTIR COMO ES EL FALLECIMIENTO DE UN FAMILIAR CERCANO', 'justificante', 1),
(76, '¿Qué pasa si no estoy de acuerdo con la evaluación de una materia?', 'EVALUACIÓN MATERIAS\r\nDE ACUERDO CON EL ARTÍCULO 49 DEL REGLAMENTO GENERAL DE EVALUACIÓN Y PROMOCIÓN DE ALUMNOS, PUEDES SOLICITAR POR ESCRITO Y DE MANERA JUSTIFICADA, LA REVISIÓN DEL RESULTADO DE SU EVALUACIÓN O DE UN EXAMEN AL JEFE DEL DEPARTAMENTO QUE TENGA A SU CARGO LA MATERIA', 'evaluacion', 1),
(77, '¿Cuándo pierdo derecho a ordinario y extraordinario?', 'ORDINARIO Y EXTRAORDINARIO\r\nPIERDES DERECHO A ORDINARIO CUANDO NO HAS ASISTIDO AL 80% DE CLASES DURANTE EL CICLO, PIERDES DERECHO A EXTRAORDINARIO CUANDO NO ASISTISTE AL 65% DE CLASES', 'derechoordinario', 1),
(78, '¿Cómo puedo hacer una cita para atención en psicología?', 'PSICOLOGÍA\r\nCON GUSTO TE PROPORCIONO EL LINK A LA SIGUIENTE PÁGINA DONDE PUEDES AGENDAR TUS CITAS PARA PSICOLOGIA ', 'citapsicologia', 1),
(79, '¿Qué es protección civil?', 'PROTECCIÓN CIVIL\r\nSEGÚN LA ORGANIZACION INTERNACIONAL DE PROTECCIÓN CIVIL, ESTA SE DEFINE COMO \"EL SISTEMA POR EL QUE CADA PAÍS PROPORCIONA LA PROTECCIÓN Y LA ASISTENCIA PARA TODOS ANTE CUALQUIER TIPO DE CATÁSTROFE O ACCIDENTE RELACIONADO CON ESTO”', 'proteccioncivil', 1),
(80, '¿Cómo ayudo en las brigadas de protección civil?', 'PROTECCIÓN CIVIL\r\nCON GUSTO TE PROPORCIONO EL LINK DONDE PODRÁS ENCONTRAR LA INFORMACIÓN QUE BUSCAS ', 'ayudarbrigadas', 2),
(81, '¿Qué requisitos necesito para pedir una licencia?', 'LICENCIA\r\nCLARO, AQUÍ ESTÁ EL LINK DONDE PUEDES ENCONTRAR LA INFORMACIÓN QUE BUSCAS \r\n', 'licencia', 2),
(82, '¿Cuántos y cuales consejos de división y de centro hay?', 'CONSEJOS DIVISIÓN\r\nI. EL RECTOR DE CENTRO UNIVERSITARIO;\r\nII. EL SECRETARIO ACADÉMICO;\r\nIII. EL SECRETARIO ADMINISTRATIVO;\r\nIV. LOS DIRECTORES DE DIVISIÓN;\r\nV. UN REPRESENTANTE ACADÉMICO, DIRECTIVO Y ESTUDIANTIL POR CADA DEPARTAMENTO, SIEMPRE QUE NO EXCEDAN DE CINCO DEPARTAMENTOS POR DIVISIÓN;\r\nVI. EL PRESIDENTE DEL CONSEJO SOCIAL DEL CENTRO UNIVERSITARIO,\r\nVII. UN REPRESENTANTE GENERAL DE LAS SIGUIENTES ORGANIZACIONES: A) DEL PERSONAL ACADÉMICO, ACREDITADO POR LA ORGANIZACIÓN QUE AGRUPE AL MAYOR NÚMERO DE ELLOS', 'consejosdivision', 1),
(83, '¿Qué tips son recomendables para las presentaciones de proyectos o informes?', 'PRESENTACIÓN PROYECTO\r\nEN EL SIGUIENTE LINK TE PROPORCIONAMOS LA INFORMACION QUE NECESITAS ', 'presentacionproyecto', 3),
(84, '¿Cuál es el formato CV (Curriculum)? (ejemplos)', 'CURRICULUM\r\nCON GUSTO TE PROPORCIONO EL LINK DE LA PAGINA DONDE ENCONTRARAS LA INFORMACION QUE NECESITAS \r\n', 'curriculum', 2),
(85, '¿El tutor es obligatorio solo en primer semestre o en toda la carrera?', 'TUTOR\r\nLA UNIDAD DE TUTORÍAS TE ASIGNA UN TUTOR SOLO EN PRIMER SEMESTRE, EN LOS SEMESTRES SIGUIENTES  PODRÁS SOLICITAR UN TUTOR DE TRAYECTORIA SOLO SI ASÍ LO REQUIERES O EN EL CASO DE LOS ESTUDIANTES QUE ESTÁN EN ARTÍCULO 35 LA UNIDAD TAMBIÉN LES ASIGNA UN TUTOR', 'tutor', 1),
(86, '¿Puedo elegir a mi tutor si estoy en el articulo 35?', 'ARTÍCULO 35\r\nSOLAMENTE SI SE ENCUENTRA REGISTRADO EN EL LISTADO DE PROFESORES CON CAPACITACIÓN', 'elegirtutor', 2),
(87, '¿Existen recursos de apoyo para las materias?', 'APOYO MATERIAS\r\nCLARO, CON GUSTO TE PROPORCIONO EL LINK DONDE ENCONTRARAS LA INFORMACION QUE SOLICITAS\r\n', 'recursosmaterias', 1);

-- --------------------------------------------------------

--
-- Table structure for table `stages`
--

CREATE TABLE `stages` (
  `id_stage` int(11) NOT NULL,
  `stage` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `stages`
--

INSERT INTO `stages` (`id_stage`, `stage`) VALUES
(1, 'inicial'),
(2, 'media'),
(3, 'final');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id_student` int(11) NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `code` int(11) NOT NULL,
  `id_career` int(11) NOT NULL,
  `id_tutor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id_student`, `name`, `email`, `code`, `id_career`, `id_tutor`) VALUES
(1, 'Tristán Pérez Pérez', 'tristan@gmail.com', 0, 1, 31);

-- --------------------------------------------------------

--
-- Table structure for table `tutors`
--

CREATE TABLE `tutors` (
  `id_tutor` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `email` varchar(100) NOT NULL,
  `id_career` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tutors`
--

INSERT INTO `tutors` (`id_tutor`, `name`, `email`, `id_career`) VALUES
(31, 'Juan Pérez El Tutor', 'Juanito69@gmail.com', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `careers`
--
ALTER TABLE `careers`
  ADD PRIMARY KEY (`id_career`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id_question`),
  ADD KEY `id_etapa` (`id_stage`);

--
-- Indexes for table `stages`
--
ALTER TABLE `stages`
  ADD PRIMARY KEY (`id_stage`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id_student`),
  ADD KEY `id_tutor` (`id_tutor`),
  ADD KEY `id_carrera` (`id_career`);

--
-- Indexes for table `tutors`
--
ALTER TABLE `tutors`
  ADD PRIMARY KEY (`id_tutor`),
  ADD KEY `id_carrera` (`id_career`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `careers`
--
ALTER TABLE `careers`
  MODIFY `id_career` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id_question` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=102;

--
-- AUTO_INCREMENT for table `stages`
--
ALTER TABLE `stages`
  MODIFY `id_stage` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id_student` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=449;

--
-- AUTO_INCREMENT for table `tutors`
--
ALTER TABLE `tutors`
  MODIFY `id_tutor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `questions`
--
ALTER TABLE `questions`
  ADD CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`id_stage`) REFERENCES `stages` (`id_stage`);

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`id_tutor`) REFERENCES `tutors` (`id_tutor`),
  ADD CONSTRAINT `students_ibfk_2` FOREIGN KEY (`id_career`) REFERENCES `careers` (`id_career`);

--
-- Constraints for table `tutors`
--
ALTER TABLE `tutors`
  ADD CONSTRAINT `tutors_ibfk_1` FOREIGN KEY (`id_career`) REFERENCES `careers` (`id_career`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
