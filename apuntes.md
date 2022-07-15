# introduccion a python
Python es un lenguaje de programacion muy popular por su syntax simple y legible. Al mismo tiempo, es uno de los lenguajes mas ocupados hoy en dia en la industria, y es famoso por *la gran variedad de aplicaciones que tiene* en variadas areas tales como: 
- ciencia de datos
- inteligencia artificial
- desarrollo web
- cyberseguridad
y muchas mas areas. 

## hola mundo y lenguajes de programacion!
El codigo mas simple que se aprende es el famoso "hola mundo". Asi se ve su implementacion en python: 
```python
print("hello world")
```
este programa genera una salida una vez ejecutado, y podremos leer el mensaje `hello world`.
Notemos que es un codigo **bastante simple** en comparacion a otros lenguajes, como `C++`:
```cpp
#include<iostream>
using namespace std;

int main(){
	cout<<"hello world"<<endl;
	return 0;
}
```
Con esto, ya podemos apreciar lo **simple** que es python para llevar a cabo ciertas tareas. 
## Conceptos basicos
### Tipos de dato
La informacion en los lenguajes de programacion tiene una forma especial de ser almacenada (que se vera mas adelante), llamada el "tipo de dato". Es muy importante sabes cuales son, dado que nos permite operar de diferentes maneras entre ellas dependiendo del tipo de dato. 
Los cuatro tipos de dato mas basicos y frecuentes son los siguientes: 
- `int`: es un numero entero (-1, 10, 0, 15, ...).
#### operaciones de enteros: 
Nosotros podemos sumar (`+`), multiplicar(`*`), dividir (`/`), restar (`-`) y exponenciar (`**`) numeros. Existen otras operaciones como el modulo, pero por ahora no son tan importantes:
```py
print(1+1)#uno mas uno
print(1-1)#uno menos uno
print(1*10)# uno por diez
print(1/10)#uno sobre diez
print(2**3)#dos al cubo
```
- `float`: es un numero decimal (1.8, 1.000, 2.15, -15.21, ...)
- `string`: corresponde a "una palabra"/ cadena de caracteres. Para utilizar una `string` debemos siempre utilizar las commilas. Asi, nuestras palabras/oraciones se veran de la siguiente manera:
```py
p1= "esta es una string"
p2= "esta es otra string"
p3= "3" #esto es una string! no un int!
suma = "ho"+"la" #nosotros podemos unir strings usando la suma!
print("hola "*100)#imprime hola cien veces


```
- `bool`: corresponde a un valor de verdad. Solo puede ser `True` o `False`. Mas adelante veremos la relevancia de estos.
### interactuando con python
Nosotros ya podemos obtener informacion desde python gracias a la funcion `print()`. Ahora, tambien nos gustaria a nosotros **darle** informacion a python. Esto lo podemos lograr **guardando la informacion en una variable** ocupando la funcion `input()`:
```py
nombre = input()
edad = input("ingresa tu edad: ") #podemos ingresar una string para generar un prompt para el usuario :D
```
#### typecasting
un problema que tiene la funcion `input()` es que *siempre nos dara una string*. Esto es malo, por ejemplo, si queremos leer un numero o un bool. La solucion es *cabiar el tipo del input* al deseado utilizando las funciones `int()`, `float()`, `bool()`. Asi, podemos ingresar la informacion de la siguiente manera:
```py
num = int(input("ingresa un numero: "))
palabra = string(input("ingresa una palabra: "))#esto ultimo es redundante, es solo un ejemplo
decimal = float(input("ingresa un decimal: "))
boolean= bool(input("ingresa un booleano: "))
```
### variables
Nosotros para leer los datos del usuario guardamos la informacion de input en una variable. Por ejemplo, en el codigo
```py
nombre = input()
```
`nombre` seria una variable. Nosotros podemos imaginar a una variable como un estacionamiento. Los estacionamientos solo pueden tener un auto. Lo mismo pasa con las variables, solo pueden tener un valor. Entonces, las variables *almacenan informacion*. Ahora, nosotros podemos asignarle un valor a una variable, y este valor *lo podemos cambiar*:
```py
nombre = "mob"
apellido = "su"
print(nombre) #accedemos su valor y lo imprimimos. veremos mob
nombre = "bom" # cambiamos su valor
print(nombre) #accedemos nuevamente su valor. veremos bom
nombre=apellido #podemos asignar el valor de una variable a otra
print(nombre) #accedemos nuevamente su valor. veremos su
nombre = 40
print(nombre)# ahora obtendremos 40.
```
notemos que en la ultima linea de codigo, asignamos el valor `40` a una variable que contenia una `string`. Esto en python esta permitido, es decir, podemos reasignarle a una variable un valor de un tipo de dato diferente. Esto, no es posible en lenguajes como `C++` o `Java`, pues estos son conocidos como lenguajes estaticamente tipeados (statically typed).

### mas funciones de enteros y floats
Si bien nosotros podemos realizar las operaciones matematicas basicas con numeros, podemos hacer muchas mas cosas. Aqui van algunas: 
```py
decimal = 1.9
numero = -15
print(floor(decimal))#funcion piso
print(ceil(decimal))#funcion techo
print(abs(numero))#valor absoluto
print(pow(2, 3))#otra forma de escribir potencia
```

### mas funciones de strings
Al mismo tiempo, existen diferentes `funciones` y `metodos` para las strings. Primero diferenciemos la syntax de una funcion y la de un metodo:
```py
a = "palabra"
print(len(a))#funcion
print(a.lower())#metodo
```
notamos que las funciones siguen el patron `nombre(...)` mientras que los medotos siguen el patron `.nombre(...)`. Mas adelante veremos el motivo de la existencia de estas dos utilidades, y veremos como crear nuestra propias funciones y metodos.
#### funciones comunes de strings
```py
a = "palabra"
b = "otra palabra"
print(len(a)) #retorna la longitud de una string
print(reversed(a)) # da vuelva una palabra
print(join(a, b)) # une dos palabras como + lo hace
```

#### metodos comunes de strings
```py
a = "palabra"
b = "otra palabra"
print(a.upper())#transforma en mayuscula
print(a.lower())#transforma en minuscula
print(a.count("a"))#cuenta cuantas veces ocurre "a"
print(a.find("a"))#busca la posicion de "a"
```

### Listas
Las listas de Python son una estructura de dato *DEFINITIVAMENTE IMPORTANTISIMAS*. Con el tiempo confirmaremos esto. Si antes podiamos pensar a las variables como un solo estacimiento, entonces las listas son como un aparcamento entero. Es decir, nosotros podemos guardar mas de un dato en estas.
Por ejemplo, supongamos que nosotros queremos guardar los nombres de varias personas. Una forma de solucionar este problema, seria generando una gran cantidad de variables, e ir guardando individualmente cada valor. Esto se veria de la siguiente manera: 
```python
n1= "pepe"
n2= "diego"
n3= "juanpe"
n4= "seba"
...
```
entonces, si queremos recordar 1000 nombres, tendremos que escribir *manualmente* 1000 variables, lo que es poco conveniente. Las listas nos permiten guardar mucha informacion en una unica variable. Veamos un ejemplo: 
```python
nombres= ["pepe", "diego", "juanpe", "seba"]
print(nombres)#imprime TODOS los nombres
```
notemos que (por ahora) podriamos insertar una cantidad enorme de informacion. Pero, podemos hacer incluso mas cosas con las listas. Tambien podemos acceder cada nombre *individualmente*, y esto se hace **usando el indice del dato buscado**. Los indices se cuentan desde 0, y no desde 1. Los motivos de esto por ahora no son tan relevantes. 
```python
nombres= ["pepe", "diego", "juanpe", "seba"]
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[10])# nos tira error porque no hay 11 nombres.
```
Entonces, nosotros podemos acceder los datos usando `variable[numero]`. Pero, nosotros podemos hacer mucho mas con las listas. Aqui hay una lista de los comandos tipicos/mas usados:
```python
nombres = [] #lista vacia
print(nombres)
nombres.append("pepe")#inserta el nombre pepe 
nombres.append("jose")#inserta el nombre pepe
nombres.append("diego")#inserta el nombre pepe
print(nombres)
nombres.clear()#borra todos los elementos de la lista
print(nombres)
nombres.append("pepe")#inserta el nombre pepe 
nombres.append("jose")#inserta el nombre pepe
nombres.append("diego")#inserta el nombre pepe
nombres.count(valor)#cuenta la cantidad de elementos con un valor en la lista
print(nombres)
nombres.pop()#elimina el ultimo elemento
print(nombres)
nombres.reverse()#invierte una lista.
print(nombres)
nombres.sort()# ORDENA una lista
print(nombres)
max(nombres) #obtiene el maximo de una lista
min(nombres) #obtiene el maximo de una lista
len(nombres) #obtiene la cantidad de elementos de la lista
```
### condicionales
Esta bien, en python nosotros tenemos muchos tipos de datos que pueden guardar informacion de diferentes maneras, pero, nos gustaria poder hacer mas cosas con esta informacion, por ejemplo, hacer que print nos de algo *diferente* dependiendo de la longitud de una string, o de la paridad de un numero. 

Bueno, esto lo podemos lograr usando los condicionales. Estos se ven de la siguiente manera: 
```python
if condicion es verdadera: 
	print("hacer algo")
elif otra condicion es verdadera:
	print("hacer otra cosa")
else:
	print("hacer incluso otra cosa")
```
Analicemos este codigo. Primero que nada, recordemos los `Bool`. Nosotros establecimos que pueden ser o verdaderos o falsos. Por ejemplo, `1+1==2` es `True`, y `1+1==3` es `False`. De igual manera `len("hola")==4` tambien es `True`. 
#### = vs ==
Los operadores `=` y `==` tienen significados diferentes. `a=b` significa "asigna el valor b a la variable a", mientras que `a==b`nos dice si efectivamente a es igual a b, y retorna `True`, o si a no es igual a b, y retorna `False`.

### retomando los condicionales
Retomando los condicionales, ya sabemos evaluar si algo es verdadero o no mediante `==`. Ahora, tambien podemos usar expresiones como `a>b`, `a<b`, `a<=b` (menor o igual), `a>=b`, y otras mas. Otra cosa que pudimos haber notado del ejemplo, es que las funciones `print` estan *ligeramente mas a la derecha* de donde inicia el `if`. Esto es muy importante, pues toas las acciones que queramos realizar dentro de un condicional, deben estar alineadas de esta manera. Asi, el compilador de python sabra que instrucciones corresponden al condicional en cuestion. 
Veamos despues de esto un ejemplo concreto:
```python
num = int(input("ingresa un numero: "))
if num==9:
	print("este numero es nueve")
elif num == 1:
	print("este numero es uno")
elif num>1 and num<9: 
	print("este numero esta entre 1 y nueve exclusivos")
else:
	print("hmmm este numero no esta en rango 1 a 9 inclusivo")
```
Este programa lo que hace es pedir al usuario un numero. El programa nos dira si el numero es 9, 1 , o algun numero entre 1 y 9 exclusivo. Si no se cumple ninguna de estas condiciones, se imprimira que el numero no se encuentra en el rango.

Tambien vimos el uso de `and` que es un operador logico. Si a y b son afirmaciones que son verdaderas, entonces and retorna verdadero. En cualquier otro caso, retorna falso. Tambien existe `or`, que retorna verdadero si *por lo menos* una afirmacion es verdadera.
```python
num = int(input("ingresa un numero: "))
if num >=1 or num<=-1:
	print("este numero esta a a dsitancia mayor igual que 1 de 0.")

```

## Loops
Hemos llegado a otro de los temas más relevantes de python, y probablemente uno de los más útiles para los lenguajes de programación en general: los *loops*. En python existen dos tipos de loops: `while` y `for`. Ambos tienen la finalidad de ejecutar una cierta cantidad de lineas de codigo de manera *repetitiva*. Si es que nosotros no especificamos un momento para que estas terminen, ocurrira que estas seguiran indefinidamente. Por ejemplo, nosotros podriamos querer imprimir `"hola mundo"` 20 veces. Si bien, podemos escribir 20 `print`, es poco conviente. Con `while` podemos repetir la linea `print('hello world')` 20 veces de la siguiente forma: 
```python
i = 1
while(i<=20);
	print("hello world")
	i+=1
```
Nosotros iniciamos `i` con el valor 1. Mientras que `i<=20` sea `True`, ejecutaremos nuestro `print` y ademas, sumaremos 1 a `i`, para asi llegar a 20, y no tener un ciclo infinito. Esto tambien se puede lograr con la syntax de `for`:
```python
for i in range(1, 21):
	print("hello world")
```
Notemos que aqui no fue necesario iniciar 1, sino que solo definimos un rango con la funcion `range(a, b)` en donde `a` es el inicio del ciclo y `b` es el inicio de este. OJO: `b` es no inclusivo. Asi, el comando se ejecutara para 1, 2, 3, 4, ..., 19, 20.
Nosotros tambien podemos imprimir `i`:

```python
for i in range(1, 21):
	print(i)
```
Con esto, nosotros podemos hacer cosas interesantes, como la suma de 100 numeros: 
```python
suma= 0
for i in range(1, 21):
	suma+=i
print(suma) 
```
Notemos que estamos utilizando el operador `a+=b`. Este se puede entender como `a=a+b`, es decir, al valor de  `a` le sumamos `b`. Tambien existe un operador para la resta: `a-=b`. Por lo general, nosotros podemos usar tanto `while` como `for` para las mismas accciones, pero, con el tiempo, nos daremos cuenta de cuando es mas conveniente usar `while` y cuando usar `for`.
### Algunos ejemplos de for y while
```python
for i in range(1, 101):
	if i<50:
		print("menor que 50")
	else:
		print("mayor igual que 50")

for i in range (1, 40):

	if i==1:
		print("uno")
	elif i==10:
		print("diez")
	elif i==39:
		print("39")
	else:
		print("no conozco ese numero...")
		
		
terminado = false
while(termimado == true):
	print("ingresa dos numeros positivos, para sumarlos. Si no quieres sumar mas, ingresa cero.")
	a = int(input())
	b = int(input())
	if(a>0 and b>0):
		print(a+b)
	else:
		print("programa terminado")
		terminado = true
```

El ultimo programa es especialmente interesante, pues ya podemos hacer un proceso infinito en donde el usuario decida si queremos terminar el programa o no.  









