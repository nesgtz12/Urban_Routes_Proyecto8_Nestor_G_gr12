# Proyecto 8 Urban Routes (qa-project-Urban-Routes-es)

Hola buenas tardes auditor, en esta ocasión se está comprobando la aplicación de Urban.Routes (proyecto 8)
Mi nombre es Nestor Gutierrez y pertenezco al grupo 12 de QA
Antes de inicia es necesario instalar los siguientes programas (paquetes) para que funcione de manera adecuada
*Pytest
*Coverage
*Selenium 

Nota: tengo instalada Selenium web driver en dos sistemas web (chrome y edge) pero funciona con ambos y no es necesario instarla ambos, para este caso se está utilizando chrome

También consulte mucho con chatgpt, ya que todavía no soy un experto en el tema

A continuación se realiza las siguientes pruebas (lista de comprobación) que se nos solicita en la comprobación y realización de las pruebas

Lista de comprobación:
1. Introducción de una dirección en este caso ('East 2nd Street, 601' y '1300 1st St')
2. Selecciona la tarifa, en este caso sería confort (taxi)
3. Proporcionar un número de teléfono ('+1 123 123 12 12')
4. Rellenar el formulario de agregar una tarjeta
5. Enviarle un mensaje al conductor
6. Seleccionar (pedir) manta y pañuelos
7. Pedir helados
8. Aparece una venta emergente de "búsqueda" del taxi
9. Esperar que aparezca la información del conductor del chofer


Entorno de pruebas
Pycharm 2024.1.4
Python versión 3.12.4
Pytest 8.3.2
Selenium 4.23.1 
Coverage 7.6.1
Chrome está actualizado
Versión 127.0.6533.120 (Build oficial) (64 bits)

Instrucciones para realizar las pruebas
1. Es necesario instalar los paquetes que se mencionan en el entorno de pruebas
2. Se debe de verificar que se cuente con selenium el navegador web (en este caso chrome) y también en pycharm
3. Actualice en data.py el link de urban_routes_url (remplace el antiguo link por el nuevo), para que con ello pueda entrar al servidor el programa
4. Corra en programa solamente en archivo de main.py y espere que se realicen las pruebas



Por mas que trate de cambiar y poner diferentes cosas la identificación de la ventana confort de manera general, no logre, lo lamento mucho ;(, pero si me indicara el como realizarlo sin arruinar el código,  lo hare con mucho gusto
Nota de este problema: Ya quedo corregido
•	Entiendo el punto de ingles/español, pero si traduzco el código al inglés, no encuentra los elementos de la pag de Urban, por más que ya estén indicados 
