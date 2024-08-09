#!/usr/bin/node
const Rectangle = require('./4-rectangle');
/*a class Square that defines a square and inherits from Rectangle of 4-rectangle.js*/

class Square extends Rectangle{
    constructor(size){
        super(size, size);
    }
    charPrint(c){
        if(c === undefined){
            c = 'X';
        }
        for( let i = 0; i < this.height; i++){
                console.log(c.repeat(this.width))
            }

    }
}
module.exports = Square;
