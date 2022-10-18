#!/usr/bin/node

const fs = require('fs');
filePath = process.argv[2];
fs.readFile(filePath, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
