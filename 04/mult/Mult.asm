// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.
@0
D=M        //ram[0] is my first number and ram[1] is my second number ram[2] conatins the product
@3
M=D     //loading ram[0] to memory location 3 which is my iterator
(loop)
    @3
    M=M-1    //ram[3]--
    @1
    D=M
    @2
    M=M+D     //ram[2] = ram[2] + ram[1]
    @3
    D=M
    @over
    D;JLE         //exit the loop if ram[3] == 0
    @loop
    D;JGE        //else jump to loop
(over)

