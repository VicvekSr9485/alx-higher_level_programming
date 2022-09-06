#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const nbo of list) {
    if (nbo === searchElement) count++;
  }
  return count;
};
