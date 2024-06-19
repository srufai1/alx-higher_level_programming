#!/usr/bin/node
'use strict';

// Print statements based on command-line arguments
let words;
if (!process.argv[2]) {
  words = 'undefined is undefined';
} else if (!process.argv[3]) {
  words = process.argv[2] + ' is undefined';
} else {
  words = process.argv[2] + ' is ' + process.argv[3];
}
console.log(words);

