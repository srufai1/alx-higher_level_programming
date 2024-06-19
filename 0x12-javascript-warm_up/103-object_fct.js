#!/usr/bin/node
// new function incr that increments the integer value.

const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject); // Output: { type: 'object', value: 12 }

myObject.incr = function () {
  myObject.value++; // Increment the 'value' property of myObject
};

myObject.incr(); // Increment 'value' by 1
console.log(myObject); // Output: { type: 'object', value: 13 }

myObject.incr(); // Increment 'value' by 1
console.log(myObject); // Output: { type: 'object', value: 14 }

myObject.incr(); // Increment 'value' by 1
console.log(myObject);
