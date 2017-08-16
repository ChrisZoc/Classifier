'''
 QUITO
==============
'''
import couchdb
import sys
import urllib3 
import textblob
import os
import re
import string
from textblob.classifiers import NaiveBayesClassifier
from couchdb import view
from textblob import TextBlob
train = [
...     ('Presidente Lenin se está haciendo eco de un anacrónico e interesado discurso, si ud quiere le puedo demostrar lo equivocado que está.', 'neu'),
...     ('Hoy me visto de sonrisas no permitas que nada ni nadie amargue tu día', 'pos'),
...     ('Soy una cicatriz que ya no existe un beso ya lavado por el tiempo un amor y otro amor que ya enterraste... D D', 'neg'),
...     ('Esto es lo que se debe seguir haciendo UEMs y siglo XXI con transporte gratuito para transformar la educación rural', 'neu'),
...     ("De lunes a viernes acompáñenme a revisar las noticias del día por teleamazonasec en", 'neu'),
...     ('Los tengo en mi corazón y en mi mente siempre Los amo y siempre voy a valorar todo lo que hacen por mi', 'pos'),
...     ('Belifans Muchas gracias por todo su cariño son lo más importante en mi vida mi motivación mi TODO', 'pos'),
...     ("Así mismo no evalúa impacto en Ciencias Sociales y en Ciencias Naturales donde impacto positivo es mayor", 'neu'),
...     ('Para navidad no quiero regalos', 'neg'),
...     ('Hay cosas que definitiva me borran la sonrisa de la cara', 'neg'),
...     (' Que tu alma tenga voz que tus besos tengan pies Que al amor le llames Dios y tu pensamiento mire con memoria', 'pos'),
...     ('Vía eluniversocom Hace pocos minutos el Presidente anunció estas medidas de austeridad', 'neu'),
...     ('La felicidad no es un estado de ánimo es un modo de vida'pos'),
...     ('Sería muy interesante organizar un foro académico en el que los autores presenten sus respectivos estudios ', 'pos'),
...     ("A veces dos personas se deben separar para darse cuenta de que necesitan estar juntas", 'neg'),
...     ('El problema no es la eficacia del programa de las UEM y su ubicación y cumplimiento de los objetivos SINO LA MALA FE de desprestigiar', 'neg'),
...     ('Si vas a ser guapa e inteligente prepárate para ser odiada', 'pos'),
...     ("Quien dice amo mi soltería es quien más quiere estar con alguien", 'pos'),
...     ('La invalidez del alma y corazón quiere desprestigiar a DOS HOMBRES trabajadores y honestos', 'neg'),
...     ('Esa precisamente fue la disposición de MashiRafael y el proyecto estaba en marcha', 'neu'),
...     (' No temo al que ha practicado 10000 patadas pero temo al que ha practicado una patada 10000 veces', 'neg'),
...     ('Los verdaderos amigos son como diamantes preciosos pero raros ', 'pos'),
...     ('Buenaventurado  aquel que en su corazón  no o existe  envidia', 'pos'),
...     ('No te preocupes por lo que está bien o está mal sino por lo que es importante', 'pos'),
...     ("La confianza es como un espejo Una vez roto se puede arreglar pero aún se pueden ver las grietas", 'neg'),
...     ('No dudes de la inteligencia de tu pareja solo mira con quien tiene una relación', 'pos'),
...     ('Feliz comienzo de semana','pos'),
...     ("Felicidad es despertar y ver el nuevo día estar o hablar con los hijoso amigoso vecinos Es elegir estar solo o en compañíaTantas cosas", 'pos'),
...     ('Hace falta quién ajuste las velas', 'neu'),
...     ('Un banco es una forma de control materialista', 'neu'),
...     ('Lamentable sii ya nadamas estas esperando el momento de fracasar ', 'neg'),
...     ('Los ratones se siguen paseando casi se escapa uno bien bruto el hpta', 'neg'),
...     ('Y usted le  cree a este señor espere un poco y verá como se derrumba la tela de araña y quien queda enredada en ella', 'neg'),
...     ('Y me puede decir como lo comprobó con una sola visita el pueblo no es tonto no comemos cuentos basta de insultar nuestra inteligencia', 'neu'),
...     ("Los honestos son más a los deshonestos ya los pondremos ante la justicia", 'neu'),
...     ('Cuenten con nosotros que sin duda nosotros contamos con ustedes', 'pos'),
...     ('Esa renegociación le ahorrará al Estado USD 250 millones solo en el 2018', 'neu'),
...     ("Con decisión y el compromiso de todos saldremos adelante la Lucha Contra La Corrupción es un tema prioritario", 'pos'),
...     ('¡Así deben actuar los trabajadores honestos', 'pos'),
...     ('Valoramos a los trabajadores petroleros Es mucho mayor el bien que han hecho al país', 'pos'),
...     (' Ranking de las mejores hamburguesas en Quito', 'neu'),
...     ('Personas solo van 4 veces al año a agencias físicas Usuarios quieren hacer transacciones a través de su smartphone ', 'neu'),
...     ('Tink automatiza referidos para diferentes instituciones Capitaliza la conectividad de los clientes ', 'neu'),
...     ('América del Sur tiene 426 millones de personas y 66 accede a Internet ', 'neu'),
...     ('Los clientes solo piden amor y tu das sexo dice speaker de BCP Comunica', 'neu'),
...     ('Ecuatorianos prueban cholas de Guano ', 'neu'),
...     ('Hoy fueron 15 horas de trabajo Al fin en casa satisfecha por entregar todo', 'pos'),
...     ("Maridaje en Quito: cerveza con té verde y sushi en el pub de Sinners", 'pos'),
...     ('Helados con nitrógeno en Guayaquil', 'neu'),
...     ('La división de Lenin y JorgeGlas en un video de GkillCitycom Ecuador', 'neu'),
...     ('El Metro Está Pasando no olviden inscribirse para programar su visita al Metro de Quito  ', 'neu'),
...     ('El Metro Está Pasando 98.000 dovelas piezas de hormigón conformarán el túnel del Metro Al momento tenemos un 43 de la producción total ', 'neu'),
...     ('Movilidad Quito Tenga en cuenta cómo funcionará el transporte público y las vías peatonales para que pueda disfrutar de la Fiesta Luz Quito', 'neu'),
...     ('Mira el Centro Histórico con otros ojos y enorgullécete de vivir en Quito', 'pos'),
...     ("Fiesta Luz Quito los esperamos esta noche Por favor no olviden tomar estas recomendaciones:", 'neu'),
...     ('A mi me arrojaron de cara al suelo', 'neg'),
...     ('Lo dijo Confucio', 'neu'),
...     ("Muy cierto", 'neu'),
...     ('La fe es certeza', 'pos'),
...     ('Me  encanta la abuela', 'pos'),
...     ('A quien buen árbol se arrima buen cobijo le da ', 'pos'),
...     ('La felicidad llevada a cabo es la semilla, la felicidad compartida es la flor', 'pos'),
...     ('No debemos creer demasiado en los elogios. La crítica a veces es muy necesaria', 'neg'),
...     ('No confíes tu secreto ni al más íntimo amigo;no podrías pedirle', 'neg'),
...     ("preciosa foto de un nazareno de mi hermandad", 'pos'),
...     ('Si quieres que tu secreto sea guardado, guárdalo tú mismo, 'neu'),
...     ('Y si le cortamos esa lengua mentirosa y le recortamos el sueldo', 'neg'),
...     ("Si te quiere por tu lencería no es amor Es algo mejor", 'pos'),
...     ('Amaos los unos a los otros como vos ama Dios', 'pos'),
...     ('Si los ojos son considerados como las ventanas del alma una sonrisa debe ser la puerta de entrada al corazón', 'pos'),
...     ('La más terrible de las pobrezas es la soledad y el sentimiento de no ser amado ', 'neg'),
...     ('No debemos creer demasiado en los elogios', 'neg'),
...     ('Lo único que no regresa es el tiempo, es lineal. No nos estamos haciendo más jóvenes', 'neg'),
...     ('El tiempo es oro. No lo desperdicies en alguien que no valora lo que eres.', 'pos'),
...     ("Mientras que el corazón tiene deseo, la imaginación conserva ilusiones", 'pos'),
...     ('Excelente abuelita', 'pos'),
...     ('La envidia y el odio van siempre unidos Se fortalecen recíprocamente porque persiguen el mismo objeto', 'neg'),
...     ("Siempre es mejor demostrar el amor entre abrazos que entre comillas", 'pos'),
...     ('Si tu perro cree que tu eres la mejor persona del mundo, no busques una segunda opinión', 'pos'),
...     ('Quédate con alguien que sabe lo que tiene cuando te tiene', 'pos'),
...     ('Eso lo hizo correa no usted Inaugure obras q ud haya hecho ', 'neg'),
...     ('Qué pena señor Lenin Moreno que ya no tener seguidores en Twitter mentalmente ya la gente no cree en mí confía en usted', 'neg'),
...     ('El compromiso de trabajo junto a nuestros Agricultores de todo el País es nuestra mayor fortaleza', 'pos'),
...     ('Presidencia Ec lo mal que somos pagados los emplados y como no acatan todos nuestro beneficios los empleadores.', 'neg'),
...     ("Dios le bendiga y le de sabiduria Sr Presidente", 'pos'),
...     ('Todos tienen derecho a una vivienda digna', 'pos'),
...     ('Toma Traidor Judas', 'neg'),
...     ("La dos cosas", 'neu'),
...     ('Todo sucede por una razón', 'neu'),
...     ('Demos gracias a las personas que nos hacen felices', 'pos'),
...     (' Lo que está en nuestro poder hacer también está en nuestro poder no hacerlo', 'neu'),
...     ('No hay mayor cinismo que el de aquellos que reclaman para sí lo que nunca han dado', 'neg'),
...     ('cuéntame más  checaaaaaa', 'neu'),
...     ('No hay cosas sin interés. Tan sólo personas incapaces de interesarse', 'neg'),
...     ("La felicidad es amor, no otra cosa. El que sabe amar es feliz", 'pos'),
...     ('La razón y la sinrazón viven en el mismo escalón', 'neu'),
...     ('Vívelo, ámalo, aprende de aquello', 'pos'),
...     ("Agradece todo amanecer y desea que siempre sea para bien", 'pos'),
...     ('Siempre el que quiera engañar encontrará a quien le permita ser engañado', 'neg'),
...     ('Las grandes personas hablan de ideas ', 'pos')
... ]
cl = NaiveBayesClassifier(train)
URL = '54.242.72.224'
db_name = 'tweet'
db1_name = 'cleantweet'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
server1 = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print(db_name)
    db = server[db_name]
    print(db1_name)
    db1 = server1[db1_name]
    print('success')
    print('success1')

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

view = "vistaprincipal/vistaprincipal"


for data in db.view(view):
    # print '=' * 40
    # print '====>', data['value']
    # print '---->', data['value'].split()
    line = data['value']
    line = re.sub(r'[.,"!]+', '', line, flags=re.MULTILINE)  # removes the characters specified
    line = re.sub(r'^RT[\s]+', '', line, flags=re.MULTILINE)  # removes RT
    line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)  # remove link
    line = re.sub(r'[:]+', '', line, flags=re.MULTILINE)

    new_line = ''
    for i in line.split():  # remove @ and #words, punctuataion
        if not i.startswith('@') and not i.startswith('#') and i not in string.punctuation:
            new_line += i + ' '
        line = new_line
    data['value']=line
    data['Sentiment']=cl.classify(line)
    print(new_line +"-->"+ data['Sentiment']+ '''''')
    
    try:
        db1.save(data)
    except:
        print("Data repeated...")

    
