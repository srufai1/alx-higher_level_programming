#!/usr/bin/node

// Check if a command-line argument is a number and print accordingly
let a = 'Not a number';
const n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  a = 'My number: ' + n;
}
console.log(a);

