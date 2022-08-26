.. highlight:: rst

Welcome to Solar's Documentation!
=================================

.. image:: _static/solar_icon_head.png
   :alt: Solar
   :align: center
   :target: https://github.com/tristanhdez/soy-solar
   :width: 400
   :height: 400

.. admonition:: How can I contribute in this project?

   You can start here: `Soy Solar <https://github.com/tristanhdez/soy-solar/blob/master/CONTRIBUTING.md>`_


Solar depends on the `Flask`_ and `MySQL`_. The documentation for these can be found at:

- `Flask Documentation <https://flask.palletsprojects.com/en/2.2x/>`_
- `MySQL Documentation <https://dev.mysql.com/doc/>`_

.. _Flask: https://flask.palletsprojects.com/en/2.2x/
.. _MySQL: https://dev.mysql.com/doc/


This document is meant to give a tutorial-like overview of all common tasks
while using Solar.


Getting Start
=============

Development
***********


The root file of Solar is the file :file:`main.py` where you can run the project.
After of that you need to configure all aspects of :file:`config.py` where in our class
:data:`Config` get the default configuration but we need to focus on Database Configuration.
Just change ::

    MYSQL_DATABASE_HOST = "******"
    MYSQL_DATABASE_USER = "********"
    MYSQL_DATABASE_PASSWORD = "******"
    MYSQL_DATABASE_DB= "******"

Mount your database, export the :data:`Config Development` with ::

   $ export FLASK_DEBUG=development

and then, run :file:`main.py` and join to :data:`http://127.0.0.1:5000`

To join like :data:`student` you can take in consideration the next credentials ::

   Student:
   Name: Tristán Pérez Pérez
   Code: 000000000
   Career: INGC
   Email: tristan@gmail.com
   Tutor: Juan Perez

And taking a Tutor Reference like ::

   Tutor:
   Name: Juan Pérez El Tutor
   Email: Juanito69@gmail.com
   Career: INGC

Student
=======

decorator
*********

login_required
--------------

As you know, we're using cookies with sessions and the intention is
get more control about who can join to our Student. If exist our Student ID in session
you can continue with your progress like "Student", otherwise It'll return to login page.

.. code:: python


   def login_required(f):
      @wraps(f)
      def wrap(*args, **kwargs):
         if 'studentCode' in session:
               return f(*args, **kwargs)
         else:
               return redirect('login')
      return wrap

Utils
=====

classes
*******

Solar
-----

   As we know, :data:`Solar()` is the main class where we're working a lot.
   Where we're creating an string constant that is our base error message when
   we doesn't found any answer on the database

   .. code:: python

      BASE_ERROR_MESSAGE = "¡Uy! Actualmente {error_reason}"


      class Solar:

         def __init__(self, keywords):
            self.keywords = keywords


         def find_answer(self, keywords):
            return f"{keywords}"


   Our child class are searching by query our question and answer where the keyword it will be at the user input

   .. code:: python

      class Question(Solar):

         def find_answer(self):
            connection = mysql.connect()
            cursor = connection.cursor()
            row = cursor.execute("SELECT question, answer, link FROM questions WHERE keyword='"+str(self.keywords)+"'")
            connection.commit()
            answer = cursor.fetchall()
            cursor.close()
            if row == 1:
                  return super().find_answer(keywords=answer)
            error_find_answer_reason = "no tenemos esa información en nuestra base de datos, nos apoyarías muchísimo si colaboras con tu pregunta en la sección: ¡Colabora una Pregunta!"
            context = BASE_ERROR_MESSAGE.format(error_reason=error_find_answer_reason)
            return super().find_answer(keywords=context)


Clean_Str
---------

   We're using a class called :data:`Clean_Str()`

   .. code:: python

      class Clean_Str():

         def __init__(self, str):
            self.str = str


         def cleaned(self, str):
            return str(str)


   And then using our child class where we'll clean
   our tuple to prevent the typical characters using  :data:`replace()` function

   .. code:: python

      class Clean(Clean_Str):


         def cleaned(self):
            result = self.str.replace("(","").replace(")","").replace("'","") \
                  .replace('\\n', '\n').replace('\\t', '\t').replace("\\r","\r") \
                     .replace("\\"," ").replace(","," ")
            return result


Tutor
----------

   This is so similar to :data:`Solar()` class but in this case, we're searching our tutor by student code.
   Getting only the name and the email.

.. code:: python

   class Get_Tutor(Tutor):

      def find_tutor(self):
         connection = mysql.connect()
         cursor = connection.cursor()
         row = cursor.execute("SELECT tutors.name from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+self.code+"'")
         connection.commit()
         tutor_name = cursor.fetchall()
         row2 = cursor.execute("SELECT tutors.email from tutors join students on tutors.id_tutor = students.id_tutor where students.code = '"+self.code+"'")
         connection.commit()
         tutor_email = cursor.fetchall()
         cursor.close()
         if row == 1 and row2 == 1:
               context = BASE_TUTOR_FOUND.format(student_code = self.code, tutor_name = tutor_name, tutor_email = tutor_email)
               return super().find_tutor(code=context)
         error_find_tutor_reason = "no cuenta con un tutor, de lo contrario, no se ha actualizado mi base de datos con tu información. Puedes contactarte con nosotros para darte una solución en la sección ¡Contáctate con Nosotros!"
         context = BASE_ERROR_MESSAGE.format(error_reason=error_find_tutor_reason)
         return super().find_tutor(code=context)



getting_keywords
----------------

   Getting the keywords is the same that the last classes but it's just reading and getting
   all the keywords of our questions on database

   .. code:: python

         def find_keywords(self):
            connection = mysql.connect()
            cursor = connection.cursor()
            cursor.execute("SELECT keyword_human, description FROM questions;")
            connection.commit()
            data = cursor.fetchall()
            cursor.close()
            return data



validate_student
----------------

   Getting the students with their code by query on database

   .. code:: python

      def validate_student(self):
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT code FROM students WHERE code='"+self.code+"'")
        connection.commit()
        data = cursor.fetchall()
        cursor.close()
        return super().validate_student(code = data)

database
--------

   We're just getting our MySQL class to interactuate with the database

   .. code:: python

      from flaskext.mysql import MySQL


      mysql= MySQL()



.. rubric:: Footnotes

.. [#] This is the usual lay-out.  However, :file:`conf.py` can also live in
       another directory, the :term:`configuration directory`.  See
       :ref:`invocation`.

.. |more| image:: more.png
          :align: middle
          :alt: more info
