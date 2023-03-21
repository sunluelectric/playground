# **JavaScript**

Author: Sun Lu

This is a notebook on JavaScript programming. The notebook is based on following materials:
- Jonas Schmedtmann, *The Complete JavaScript Course 2023: From Zero to Expert!*, Udemy

The program is tested on a PC with RHEL 9.1.

---

# What Is JavaScript

JavaScript is a high-level object-oriented computer programming language. It is widely used in building web applications. 

For example, consider a web page. HTML records the content of the web page, while CSS determines the presentation of the content. JavaScript is the actual logics integrated into the web page which makes it not only a static poster but a interactive application with data transmission. For example, JavaScript can respond to the button clicks on the web page, retrieve data from a remote server, and subsequently display the data on the in a dynamic manner.

# JavaScript Runtime Setup

## Browser-Based JavaScript Runtime

Many web browsers, including Microsoft Edge and Google Chrome, have so called "developer tools" that allows the user to check and test JavaScript codes using the browser. The outcome of the code can be immediately displayed on the browser.

Take Microsoft Edge as an example. To setup a browser-based JavaScript runtime on Edge, open a blank page with URL `about:blank`. Then press `F12` to open the developer tools. Select "Console" in the developer tools. The user can then test JavaScript codes using the console.

For quick demonstration, type the following in the console
```
alert("Hello World!")
```
then press `Enter`. An alert message that says "Hello World!" shall pop up.

Another example where an `if` statement is used is given below.
```
let js = 'show'
if (js === 'show')
    alert('Hello World Again!')
```
A message box that says "Hello World Again!" shall pop up.

## VSCode-Based JavaScript Runtime

Microsoft Visual Studio Code (VSCode) is a very powerful and flexible text and program editor. Download and install Microsoft Visual Studio Code from [here](https://code.visualstudio.com/).





