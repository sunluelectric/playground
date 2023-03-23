# **JavaScript**

Author: Sun Lu

This is a notebook on JavaScript programming. The notebook is based on following materials:

- Jonas Schmedtmann, _The Complete JavaScript Course 2023: From Zero to Expert!_, Udemy

The program is tested on a PC with RHEL 9.1.

---

# What Is JavaScript

JavaScript is a high-level object-oriented computer programming language. It is widely used in building web applications, both front-end and back-end, for both desktop or mobile devices. It is also one of the most widely used computer programming language for general purposes.

For example, consider a web page. HTML records the content of the web page, while CSS determines the presentation of the content. JavaScript is the actual logics integrated into the web page which makes it not only a static poster but a interactive application with data transmission. For example, JavaScript can respond to the button clicks on the web page, retrieve data from a remote server, and subsequently display the data on the in a dynamic manner.

# JavaScript Runtime Setup

## Browser-Based JavaScript Runtime

Many web browsers, including Microsoft Edge and Google Chrome, have so called "developer tools" that allows the user to check and test JavaScript codes using the browser. The outcome of the code can be immediately displayed on the browser.

Take Microsoft Edge as an example. To setup a browser-based JavaScript runtime on Edge, open a blank page with URL `about:blank`. Then press `F12` to open the developer tools. Select "Console" in the developer tools. The user can then test JavaScript codes using the console.

For quick demonstration, type the following in the console

```js
alert("Hello World!");
```

then press `Enter`. An alert message that says "Hello World!" shall pop up.

Another example where an `if` statement is used is given below.

```js
let js = "show";
if (js === "show") alert("Hello World Again!");
```

A message box that says "Hello World Again!" shall pop up.

## VSCode-Based JavaScript Runtime

Microsoft Visual Studio Code (VSCode) is a very powerful and flexible text and program editor. Download and install Microsoft Visual Studio Code from [here](https://code.visualstudio.com/).

VSCode is able to automatically detect and color-code html and JavaScript files.

# JavaScript Fundamentals

## Integration of JavaScript into HTML

In many applications, JavaScript is commonly "attached" in html files, where `<script></script>` is used to wrap the JavaScript code. The browser shall be able to comprehend the content of the JavaScript code when loading the web page. An example is given below.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Web Page Example</title>
    <script>
      let js = "flag";
      if (js === "flag") alert("Welcome to JavaScript!");
    </script>
  </head>
  <body>
    <h1>This is an example web page.</h1>
  </body>
</html>
```

where

```html
<script>
  let js = "flag";
  if (js === "flag") alert("Welcome to JavaScript!");
</script>
```

is a piece of JavaScript code integrated into the html file. This should pop up an alert message that says "Welcome to JavaScript!" each time the page is refreshed.

When the JavaScript code becomes complicated, it is often more convenient to save the script in a separate file than using the inline script, and call that script in the html file. As an example, create a file `script.js` under the same folder with the html file as follows.

```js
let js = "amazing";
if (js === "amazing") alert("Welcome to JavaScript!");
```

In the html file, use

```html
<script src="script.js"></script>
```

to replace the inline script. It should work all the same.

## JavaScript Comments

Use

```js
// comment
```

for single-line comments, and

```js
/*
comment
comment
comment
*/
```

for multiple-line comments.

## JavaScript Variables

The syntax of declaring a variable and assigning a value to the variable is

```js
let <variableName> = <val>;
```

where `val` is the value assigned to the variable. There are many data types defined in JavaScript, to name a few, string `'apple'`, `"apple"`, or numeric number `0`, `100`, `0.5`. More will be introduced later.

Notice that JavaScript uses camelCase notation to name variables (and UPPERCASE notion for constants) as a convention. Like many other languages, JavaScript reserved keywords cannot be used as variable names.

The following table summarizes the commonly used primitive data types.

| Data Type | Explanation                                                        | Example            |
| :-------- | :----------------------------------------------------------------- | :----------------- |
| Number    | Floating point numerical numbers, both integers and decimals.      | `let x = 1;`       |
| String    | Sequence of characters.                                            | `let x = "apple";` |
| Boolean   | Logic true or false.                                               | `let x = true;`    |
| Undefined | Empty value.                                                       | `let x;`           |
| Null      | Empty value, used in different circumstances from undefined value. |                    |
| Symbol    | Unique and static value.                                           |                    |
| BigInt    | Big integer value.                                                 |                    |

JavaScript uses dynamic typing. A variable can be assigned with value without declaring the data type in advance.

Use `typeof` followed by a variable to return its type. For example,

```js
let x = 3;
typeof x;
```

the second line of the above code would return a string that says `"number"`. If `x` is assigned with another value of a different data type, the `typeof` return would also change. An example is given below.

```js
let x = 3;
typeof x; // return "number"
x = true;
typeof x; // return "boolean"
x = "javascript";
typeof x; // return string
```

In the demonstration so far, `let` has been used to declare a new variable. It is used only in the first instance when the variable is declared. It is not allowed to use `let` to declare multiple variables with the same name, or to update variables. This setup helps to prevent defining a new variable with the same time as an existing variable without noticing it, hence accidentally overwriting the existing one.

There are other ways than using `let` to declare a variable, such as using `var`. These methods are introduced as follows.

- `let` is used to declare a variable whose value and data type can change later (mutable). It is allowed to declare an undefined variable using `let`, and later update its value.
- `const` is used to declare a constant whose value cannot be changed (immutable).
- `var` legacy way of declaring variables. Its usage looks similar `let`, but it has a different mechanism behind screen.
- Without using a keyword for declaring new variable. This defines the variable under the global object, but not the current program block. It is NOT recommended.

An example is given below.

```js
const birthYear = 1991; // never change
let age;
age = 2023 - 1991;
```

## JavaScript Operators

Arithmetic operators are supported in JavaScript. Examples are given below.

```js
const birthYearLu = 1991;
const birthYearZhe = 1992;
const ageDiff = birthYearZhe - birthYearLu;
let nowYear = 2023;
let ageLu = currentYear - birthYearLu;
```

Widely used supported arithmetic operators include `+`, `-`, `*`, `/`, `**` (to the power of). In addition, `=` is also an operator, namely the assign operator, which is widely used in all circumstances. Other assign operators are `+=`, `*=`, `++`, `--`, etc.

Comparison operators are supported, including `>`, `<`, `>=`, `<=`, `==`, `!=`, `===`, `!==` etc. The return of a comparison operator is a boolean value.

String operators are supported. For example, `+` can be used to concatenate strings. An example is given below.

```js
const firstName = Lu;
const lastName = Sun;
const fullName = lastName + " " + fullName;
```

The operators can be using in a nested manner, in which case the sequence with which operators are executed follows the pre-defined operator precedence. Details are given [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence).

## Template Literals for String Operation

To form a string with variables integrated inside, using string concatenate `+` can be inconvenient, especially when managing the spaces. The template literals can be used to handle this problem. An example is given below.

```js
let x = 10;
let y = 20;
let msg =
  "The values of x and y are " +
  x +
  " and " +
  y +
  ", respectively. \n The sum is " +
  (x + y) +
  ".";
```

Alternatively, consider using template literals as follows. It simplifies integrating of variables, calculations, and line switches in a string.

```js
let x = 10;
let y = 20;
let msg = `The values of x and y are ${x} and ${y}, respectively. 
The sum is ${x + y}.`;
```

Notice that to use template literals, use \` to quote the string instead of the regular quotation marks. There are developers using \` for any string any way, regardless of whether template literals are used.

## Type Conversion and Coercion

Values of different types might be converted from one type to another. For example, a string `'1991'` can be converted to number `1991`. The developer may manually convert the data using functions, in which case it is called a "conversion", or the JavaScript interpreter may do that conversion automatically behind the screen in some operations, in which case it is called a "coercion".

An example of conversion and coercion is given below.

```js
let x = "1991";
let y = x + 1992; // y is a string says '19911992'
let z = Number(x) + 1992; // z is a number of 3983;
```

where in calculating `y`, JavaScript converts number `1992` into a string `'1992'` by coercion, then concatenate it with string `x` to get `19911992`. In calculating `z`, string `x` is first converted into number `1991`, then added with another number `1992` to get `3983`.

Use `Number()` to convert a string to a number. In the case where the string does not make sense, `NaN` is returned. Use `String()` to convert a number to a string.

Notice that though data coercion is convenient, it is sometimes not very intuitive. Examples are given below.

```js
let x;
x = "1991" + "1992"; // string, '19911992'
x = "1991" + 1992; // string, '19911992'
x = "1991" - "1992"; // number, -1
x = "1991" - 1992; // number, -1
```

Apparently, JavaScript is taking `+` as string concatenate operator over arithmetic operator, and numbers are converted into strings. When comes to `-`, since there is no corresponding string operator, it is treated as an arithmetic operator, and strings are converted into numbers.

Variables of other types can be converted to boolean type using `Boolean()`. Boolean coercion also happens frequently wherever an IF statement is used.

Only the following values are converted to `false`, and everything else would become `true`. They are: `0`, `''` (empty string), `undefined`, `null`, and `NaN`. Notice that empty object `{}` is converted to true. More about object is introduced in later part of the notebook.

## IF Statement

The control structure syntax of using an IF statement is shown below.

```js
if (<expression>) {
  <statement>;
  <statement>;
} else if {
  <statement>;
  <statement>;
} else {
  <statement>;
  <statement>;
}
```

In case where there is only one line of command in the code block in the IF statement, the curly bracket is not required.

In the above, `<expression>` a series of comparison operation formed by `==` (loose equality), `!=`(loose inequality), `===` (strong equality), `!==` (strong inequality), `>`, `<`, `>=`, `<=`. It is also possible to use a variable as the condition, in which case JavaScript will convert `<expression>` to a boolean variable using coercion. It is worth mentioning the difference between strong (in)equality and loose (in)equality. The loose (in)equality does data coercion before comparison. An example is given below.

```js
1991 === 1991; // true
"1991" === "1991"; // true
"1991" === 1991; // false, as they are of different data types
"1991" == 1991; // true, they are identical after coercion
```

In practice, use strong (in)equality wherever possible over loose (in)equality.

Notice that any variable declared inside a code block, in this case, `{}`, cannot be interacted from outside. The variable needs to be defined outside. An example is given below.

```js
let a = prompt("Input a number: ");
a = Number(a);
if (a) {
  let b = a;
} else {
  let b = "a joke";
}
alert(`You input ${b}. A good choice!`); // this would not work; b is not defined outsize the code block
```

Instead, use

```js
let a = prompt("Input a number: ");
a = Number(a);
let b;
if (a) {
  // if a is a non-zero numeric number
  b = a;
} else {
  b = "a joke";
}
alert(`You input ${b}. A good choice!`); // this works
```

Notice that `prompt()` prompts a window from where the user can input something. The input from the user is converted into a string.

Use `&&` (AND), `||` (OR), `!` (NOT) to connect statements if necessary. An example is given below.

```js
const age = 18;
const eyeSight = true;
if (age >= 18 && eyeSight) {
  alert(`You can drive.`);
} else {
  alert(`You cannot drive.`);
}
```

## SWITCH Statement

SWITCH statement can be regarded as a special case of IF statement. The control structure syntax is given below. SWITCH uses strong equality "`===`" to check values.

```js
switch (<variable>) {
  case <value-1>:
    <statement>; // execute if <variable> === <value-1>
    <statement>;
    break; // break is important
  case <value-2>:
  case <value-3>:
    <statement>; // if either <value-2> or <value-3> values match
    <statement>;
    break; // break is important
  default:
    <statement>;
    <statement>;
}
```

Notice that `break` is important after each (group) of case statement. Without `break`, the program would keep executing all the remaining commands, regardless of the remaining case checks results. In other words, if one of the case checks passes, it will bypass all remaining case checks and execute all the remaining commands until its end or when there is a `break`.

SWITCH statement is getting less used than before, as there are more and more ways to walk around.

## Conditional Operator

Conditional operator works like a lite version of the IF statement. The syntax is given below.

```js
<expression> ? <statement-or-expression-1> : <statement-or-expression-2>
```

The above line of code either execute a statement, or return an expression. An example is given below.

```js
let income = prompt("Enter the income:");
income = Number(income);
let tax =
  income <= 5000
    ? 0
    : income <= 10000
    ? 0.05 * (income - 5000)
    : income <= 20000
    ? 0.05 * 5000 + 0.1 * (income - 10000)
    : 0.05 * 5000 + 0.1 * 10000 + 0.2 * (income - 20000);
alert(
  `The income including tax is ${income}. The tax is ${tax}. The income excluding tax is ${
    income - tax
  }.`
);
```
