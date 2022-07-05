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

