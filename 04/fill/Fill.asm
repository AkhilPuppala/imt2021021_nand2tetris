// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(begin)
@SCREEN
D=A
@startlocation
M=D

(input)
@KBD
D=M
@black
D;JGT
@white
D;JEQ
@input
0;JMP

(black)
@temp
M=-1
@change
0;JMP

(white)
@temp
M=0
@change
0;JMP

(change)
@temp
D=M

@startlocation
A=M
M=D

@startlocation
D=M+1
@KBD
D=A-D

@startlocation
M=M+1
A=M

@change
D;JGT

@begin
0;JMP