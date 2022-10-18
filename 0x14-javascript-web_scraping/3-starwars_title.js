#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + movieId + '/', function (error, response, body) {
  if (error == null) {
    const movies = JSON.parse(body);
    console.log(movies.title);
  }
});
