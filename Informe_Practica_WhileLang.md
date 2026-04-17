# Práctica: Análisis Semántico con WhileLang y ANTLR4

## Portada
- **Práctica**: Análisis Semántico con WhileLang y ANTLR4
- **Objetivo**: construir un analizador semántico en Python para el lenguaje WhileLang usando ANTLR4 y validar casos de prueba semánticos.
- **Herramientas**: ANTLR4, Python 3, `antlr4-python3-runtime`.

## Introducción
El análisis semántico es la fase de un compilador que valida el significado correcto del programa después de su análisis sintáctico. Comprueba reglas como el uso de variables declaradas, tipos compatibles en expresiones y asignaciones, y el manejo de ámbitos.

ANTLR4 es un generador de analizadores que produce un parser y un visitor/listener a partir de una gramática. En esta práctica, ANTLR4 se utiliza para generar el parser Python que construye el árbol sintáctico de WhileLang.

## Descripción de la gramática WhileLang
La gramática define un lenguaje imperativo simple con las siguientes construcciones:

- `program`: una secuencia de `statement` hasta EOF.
- `statement`: puede ser declaración, asignación, `while`, `if`, `break` o `continue`.
- `declaration`: `int x = expr;` o `string s = expr;`.
- `assignment`: `x = expr;`.
- `whileStatement`: `while (condition) { statement* }`.
- `ifStatement`: `if (condition) { statement* } (else { statement* })?`.
- `condition`: puede ser una expresión simple o una comparación binaria con `>`, `<`, `==`, `!=`.
- `expr`: identificador, número, cadena, expresión aritmética, o paréntesis.

Los tokens admitidos incluyen palabras reservadas, operadores aritméticos y de comparación, así como literales `NUMBER`, `STRING`, y nombres `ID`.

## Diseño del Analizador Semántico

### Tabla de símbolos y scopes
Se usa una pila de scopes, donde cada scope es un diccionario:
- al entrar en un bloque `while`, `if` u `else`, se empuja un nuevo scope.
- al salir, se destruye el scope actual.
- las variables se buscan desde el scope local hacia afuera.

### Tipos soportados
- `int`
- `string`

### Reglas semánticas implementadas
- Declaración con tipo: `int x = 10;` y `string s = "hola";`.
- Detectar redeclaración en el mismo scope.
- Detectar uso de variable no declarada.
- Verificar compatibilidad de tipos en asignaciones.
- Operaciones aritméticas:
  - `int + int` → `int`
  - `string + string` → `string`
  - `int * int` → `int`
  - `string * ...` → error semántico
- Condiciones:
  - `if (expr)` e `while (expr)` requieren que `expr` sea `int`.
  - Comparaciones `GT`, `LT`, `EQ`, `NE` solo entre `int`.

## Implementación
El archivo principal es `SemanticVisitor.py`.

### Estructura clave
- `self.scopes`: pila de diccionarios.
- `self.errors`: lista de errores semánticos.
- `declare_variable(name, type, ctx)`: registra variables en el scope actual.
- `resolve_variable(name, ctx)`: busca la variable en los scopes.

### Reglas importantes en `SemanticVisitor.py`
- `visitDeclaration`: declara y comprueba que el tipo del lado derecho coincida con el tipo declarado.
- `visitAssignment`: comprueba que la variable exista y que los tipos coincidan.
- `visitIfStatement` y `visitWhileStatement`: crean scopes nuevos para los bloques.
- `visitComparisonCondition`: valida que ambos operandos sean `int`.
- `visitExprCondition`: valida que una condición simple sea `int`.
- `visitArithmeticExpr`: evalúa y valida operadores aritméticos.

### Ejecutable principal
`main.py`:
- recibe el archivo `.txt` como argumento.
- parsea el código con ANTLR4.
- recorre el árbol con `SemanticVisitor`.
- imprime los errores semánticos o `✓ Sin errores semánticos`.

## Pruebas realizadas
Las pruebas se ejecutaron con `python main.py testN.txt`.

### test1.txt
Código de entrada:
```text
int x = 10;
string s = "hola";
x = x + 5;
s = s + " mundo";
```
Resultado esperado: sin errores semánticos.
Resultado obtenido:
```text
✓ Sin errores semánticos
```
Análisis: las declaraciones y operaciones `int`/`string` son válidas.

### test2.txt
Código de entrada:
```text
int x = 10;
string s = "hola";
x = s;
```
Resultado esperado: error por tipo incompatible.
Resultado obtenido:
```text
Error semántico: asignación de tipo incompatible en 'x' (esperado int, obtenido string) en la línea 3
```
Análisis: `x` se declaró como `int` y se asignó una `string`.

### test3.txt
Código de entrada:
```text
y = 5;
```
Resultado esperado: error por variable no declarada.
Resultado obtenido:
```text
Error semántico: variable no declarada 'y' usada en la línea 1
```
Análisis: se usa `y` sin declaración previa.

### test4.txt
Código de entrada:
```text
int x = 1;
string x = "hola";
```
Resultado esperado: error por redeclaración en el mismo scope.
Resultado obtenido:
```text
Error semántico: redeclaración de variable 'x' en el mismo scope en la línea 2
```
Análisis: no se permite declarar el mismo nombre dos veces en el mismo bloque.

### test5.txt
Código de entrada:
```text
string s = "hola";
if (s) {
  int x = 0;
}
```
Resultado esperado: error por condición no entera.
Resultado obtenido:
```text
Error semántico: condición debe ser de tipo int en la línea 2, se obtuvo string
```
Análisis: una condición `if` requiere un `int` en esta gramática semántica.

### test6.txt
Código de entrada:
```text
string a = "hola";
string b = "mundo";
while (a < b) {
  break;
}
```
Resultado esperado: error por comparación de strings con `<`.
Resultado obtenido:
```text
Error semántico: comparación solo permitida entre int en la línea 3 (tipos: string, string)
```
Análisis: las comparaciones relacionales solo son válidas entre `int`.

### test7.txt
Código de entrada:
```text
int x = 0;
if (x < 5) {
  int y = 10;
} else {
  int y = 20;
}
```
Resultado esperado: sin errores semánticos.
Resultado obtenido:
```text
✓ Sin errores semánticos
```
Análisis: los bloques `if` y `else` usan scopes independientes.

### test8.txt
Código de entrada:
```text
int i = 0;
while (i < 3) {
  int j = 0;
  while (j < 2) {
    if (i == j) {
      j = j + 1;
    }
    j = j + 1;
  }
  i = i + 1;
}
```
Resultado esperado: sin errores semánticos.
Resultado obtenido:
```text
✓ Sin errores semánticos
```
Análisis: el anidamiento de scopes y las comparaciones `int` son correctos.

### test9.txt
Código de entrada:
```text
int i = 0;
while (i < 5) {
  if (i == 2) {
    continue;
  }
  if (i == 4) {
    break;
  }
  i = i + 1;
}
```
Resultado esperado: sin errores semánticos.
Resultado obtenido:
```text
✓ Sin errores semánticos
```
Análisis: `break` y `continue` no tienen chequeos semánticos adicionales en esta implementación.

### test10.txt
Código de entrada:
```text
string s = "hola";
string t = "mundo";
string u = s * t;
```
Resultado esperado: error por operación aritmética inválida con strings.
Resultado obtenido:
```text
Error semántico: operador '*' solo permite int*int/int/int o int-int en la línea 3 (tipos: string, string)
```
Análisis: la multiplicación entre strings no está permitida.

## Conclusiones
Se construyó un analizador semántico funcional para WhileLang que verifica:
- declaraciones y asignaciones de tipos,
- redeclaraciones locales,
- uso de variables no declaradas,
- compatibilidad de tipos en expresiones y condiciones,
- scopes anidados en `while`, `if`, y `else`.

El enfoque con ANTLR4 y un visitor semántico en Python permite separar claramente la gramática de la lógica de chequeo semántico.

## Referencias
- ANTLR4 official documentation
- antlr4-python3-runtime
- MientrasLang como lenguaje de práctica de compiladores
