#!/usr/bin/node

const request = require('request');

request(process.argv[2], "utf-8", function(err, response, body) {
    if (err == null) {
        const json = JSON.stringify(body);
        console.log(json);
    }
});
