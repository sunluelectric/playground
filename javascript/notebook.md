# **JavaScript**

Author: Sun Lu

This is a notebook on JavaScript programming. The notebook is based on following materials:
- Jonas Schmedtmann, *The Complete JavaScript Course 2023: From Zero to Expert!*, Udemy

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
alert("Hello World!")
```
then press `Enter`. An alert message that says "Hello World!" shall pop up.

Another example where an `if` statement is used is given below.
```js
let js = 'show'
if (js === 'show')
    alert('Hello World Again!')
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
      let js = 'flag';
      if (js === 'flag')
        alert("Welcome to JavaScript!");
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
    let js = 'flag';
    if (js === 'flag')
    alert("Welcome to JavaScript!");
</script>
```
is a piece of JavaScript code integrated into the html file. This should pop up an alert message that says "Welcome to JavaScript!" each time the page is refreshed.

When the JavaScript code becomes complicated, it is often more convenient to save the script in a separate file than using the inline script, and call that script in the html file. As an example, create a file `script.js` under the same folder with the html file as follows.
```js
let js = 'amazing';
if (js === 'amazing')
  alert("Welcome to JavaScript!");
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

| Data Type | Explanation | Example |
| :-------- | :---------- | :------ |
| Number | Floating point numerical numbers, both integers and decimals. | `let var = 1;` |
| String | Sequence of characters. | `let var = "apple";` |
| Boolean | Logic true or false. | `let var = true;` |
| Undefined | Empty value. | `let var;` |
| Null | Empty value, used in different circumstances from undefined value. | |
| Symbol | Unique and static value. | |
| BigInt | Big integer value. | |

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
```

Notice that in a program block, `let` is used only in the first instance when the variable is declared. It is not allowed to use `let` to declare multiple variables with the same name, or to update variables.
