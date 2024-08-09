#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Use the filter method to count the occurrences of searchElement in the list
  const occurrences = list.filter(element => element === searchElement);

  // Return the count of occurrences
  return occurrences.length;
};
