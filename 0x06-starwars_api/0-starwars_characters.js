#!/usr/bin/node

const request = require('request');

// Function to get and display characters of a given movie
function getCharacters (movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Fetch film data
  request(filmUrl, (error, response, body) => {
    if (error || response.statusCode !== 200) {
      console.error('Error fetching movie details:', error || response.statusCode);
      return;
    }

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    // Fetch each character's name
    characterUrls.forEach((url) => {
      request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        }
      });
    });
  });
}

// Check if movie ID is provided as a command line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a Movie ID as the first argument');
  process.exit(1);
}

getCharacters(movieId);
