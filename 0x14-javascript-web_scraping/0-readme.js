#!/usr/bin/node

const fs = require('fs');
const request = require('request');
path = process.argv[2];
fs.readFile(path, 'utf8', function(err, data) {
    if (err) {
        console.log(err);
    }
    else {
        console.log(data);
    }
});
