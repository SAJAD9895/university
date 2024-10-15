const functions = require('firebase-functions');
const express = require('express');
const app = express();

// Example function
app.get('/hello', (req, res) => {
  res.send('Hello from Firebase Functions!');
});

exports.app = functions.https.onRequest(app);
