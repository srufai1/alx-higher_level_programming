#!/usr/bin/node

// Searches for the second biggest integer in the list of arguments

if (process.argv.length <= 2) {
  console.log(0);
} else {
  // Convert all arguments to integers and filter out NaN values
  const numbers = process.argv.slice(2).map(Number).filter(num => !isNaN(num));

  if (numbers.length <= 1) {
    console.log(0);
  } else {
    // Sort numbers in descending order
    const sortedNumbers = numbers.sort((a, b) => b - a);
    console.log(sortedNumbers[1]);
  }
}

