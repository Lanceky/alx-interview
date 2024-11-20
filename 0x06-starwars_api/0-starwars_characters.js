#!/usr/bin/node

const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
}

async function getCharacterName (url) {
  try {
    const character = await makeRequest(url);
    return character.name;
  } catch (error) {
    return null;
  }
}

async function printMovieCharacters (filmId) {
  try {
    // Get film data
    const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;
    const film = await makeRequest(filmUrl);

    // Process characters sequentially to maintain order
    for (const characterUrl of film.characters) {
      const name = await getCharacterName(characterUrl);
      if (name) {
        console.log(name);
      }
    }
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
}

// Get movie ID from command line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

printMovieCharacters(movieId);
