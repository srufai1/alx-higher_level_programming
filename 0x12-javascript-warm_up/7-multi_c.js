#!/usr/bin/node

// Print the string 'C is fun' a number of times specified by the command-line argument
const words = 'C is fun';
const j = process.argv[2];
let i = 0;
while (i < j) {
  console.log(words);
  i++;
}
