#!/usr/bin/node

// Print the first command-line argument if present, otherwise print "No argument"
let words;
if (!process.argv[2]) {
  words = 'No argument';
} else {
  words = process.argv[2];
}
console.log(words);

