#!/usr/bin/node

const request = require('request');
const FILM_ID = process.argv[2];
const BASE_URL = 'https://swapi-api.alx-tools.com/api';

if (!FILM_ID) {
  console.error('Please provide a film ID');
  process.exit(1);
}

// Promisify request to handle async operations better
function makeRequest(url) {
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

// Get character name from URL
async function getCharacterName(url) {
  try {
    const character = await makeRequest(url);
    return character.name;
  } catch (error) {
    console.error(`Error fetching character: ${error}`);
    return null;
  }
}

// Main function to get and print characters
async function printMovieCharacters(filmId) {
  try {
    // Get film data
    const film = await makeRequest(`${BASE_URL}/films/${filmId}/`);

    // Get all character names in order
    const characterPromises = film.characters.map(url => getCharacterName(url));
    const characterNames = await Promise.all(characterPromises);

    // Print character names
    characterNames.forEach(name => {
      if (name) console.log(name);
    });
  } catch (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
}

printMovieCharacters(FILM_ID);
