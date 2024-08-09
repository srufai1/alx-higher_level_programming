#!/usr/bin/node
/* Defining a rectangle using Javascript class and a constructor eith parameters
*/

class Rectangle {
    constructor(w, h){
        if(w > 0 && h > 0){
        this.width = w;
        this.height = h;
        }
    }
    
}

module.exports = Rectangle;

