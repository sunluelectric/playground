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
