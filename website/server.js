const express = require('express');
const bodyParser = require("body-parser");
const app = express();
const path = require('path')
const http = require("http");
const session = require('express-session');
const port = 8082;
const fs = require("fs");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
const { check, validationResult } = require('express-validator/check');
var LocalStrategy   = require('passport-local').Strategy;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(session({
	secret: 'secret',
	resave: true,
	saveUninitialized: true
}));

app.use(express.static());


pass2 = "2";
function callback(responseText){
    var save = responseText;
    pass2 = save;
}

function readTextFile(file, act_on_response)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                callback(rawFile.responseText);
            }
        }
    }
    rawFile.send();
}

readTextFile("file://C:/Users/adiso/Downloads/password.txt")

// init db
var mysql = require('mysql');
var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: pass2,
  database: "testdb"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));


var server = app.listen(8082, "127.0.0.1", function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Example app listening at http://%s:%s", host, port)

});

function userIsAllowed(callback, status) {
  // this function would contain your logic, presumably asynchronous,
  // about whether or not the user is allowed to see files in the
  // protected directory
  console.log(status);
  callback(status);
};

// This function returns a middleware function
var protectPath = function(regex) {
  return function(req, res, next) {
    if (!regex.test(req.url)) { return next(); }

    userIsAllowed(function(allowed) {
      if (allowed) {
        next(); // send the request to the next handler, which is express.static
      } else {
        res.end('You are not allowed!');
      }
    });
  };
};

app.use(protectPath(/^\/protected\/.*$/));

 app.post('/auth', [
   check('username').trim().escape(),
   check('password').trim().escape()
 ], function(request, response) {
 	var username = request.body.username;
   console.log(username);
	 var password = request.body.password;
   console.log(password);
 	if (username && password) {
 		con.query('SELECT * FROM accounts WHERE username = ? AND password = ?', [username, password], function(error, results, fields) {
 			if (results.length > 0) {
 				request.session.loggedin = true;
 				request.session.username = username;
 				response.redirect('/admin');
 			} else {
 				response.send('Incorrect Username and/or Password!');
 			}
 			response.end();
 		});
 	} else {
 		response.send('Please enter Username and Password!');
 		response.end();
 	}
 });

 app.get('/admin', function(request, response) {
 	if (request.session.loggedin) {
 		return response.sendFile(__dirname + '/classroom/web-dev/protected/web-development.html');
 	} else {
 		return response.send('Please login to view this page!');
 	}
 	response.end();
 });
