#!/usr/bin/node

// Check the number of command line arguments and print appropriate message
let words;
if (!process.argv[2]) {
  words = 'No argument';
} else if (process.argv.length === 3) {
  words = 'Argument found';
} else {
  words = 'Arguments found';
}
console.log(words);
