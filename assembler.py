import os, sys

comp = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
    }


dest = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
    }


jump = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
    }

table = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    "R0" : 0,
    "R1" : 1,
    "R2" : 2,
    "R3" : 3,
    "R4" : 4,
    "R5" : 5,
    "R6" : 6,
    "R7" : 7,
    "R8" : 8,
    "R9" : 9,
    "R10" : 10,
    "R11" : 11,
    "R12" : 12,
    "R13" : 13,
    "R14" : 14,
    "R15" : 15,
    }
variableaddress = 16

def removewhite(line):
  c = line[0]
  if (c == "\n" or c == "/"):
    return ""
  elif (c == " "):
    return removewhite(line[1:])
  else:
    return (c + removewhite(line[1:]))

def addvariable(label):
  global variableaddress
  global table
  table[label] = variableaddress
  variableaddress += 1
  return table[label]

def normalize(line):
  line = line[:-1]
  if not "=" in line:
    line = "null=" + line
  if not ";" in line:
    line = line + ";null"
  return line 

def translateToa(line):
  if (line[1].isalpha()):
    label = line[1:-1]
    avalue= table.get(label,-1)
    if(avalue == -1):
      avalue = addavariable(label)
  else:
    avalue = line[1:]
  bvalue = bin(int(avalue))[2:].zfill(16)
  return bvalue

def translateToc(line):
  line = normalize(line)
  temp = line.split("=")
  destCode = dest.get(temp[0], "destFAIL")
  temp = temp[1].split(";")
  compCode = comp.get(temp[0], "compFAIL")
  jumpCode = jump.get(temp[1], "jumpFAIL")
  return compCode, destCode, jumpCode

def translate(line):
  if(line[0] == "@"):
    return translateToa(line)
  else:
    code = translateToc(line)
    return "111" + code[0] + code[1] + code[2]

def firstpass():
  global ip
  global infile 
  infile = open(ip,'r')
  global outfile 
  outfile = open("fil" , 'a')
  linenum = 0
  for line in infile:
    wline = removewhite(line)
    if (wline != ""):
      if(wline[0] != "("):
        label = wline[1:-1]
        table[label] = linenum
        wline = ""
      else:
        linenum += 1
        outfile.write(wline + "\n")
  infile.close()
  outfile.close()

def assemble():
  global ip
  global infile
  infile = open(ip ,'r')
  global outfile
  outfile = open("fil" , 'a')
  for line in infile:
    tline = translate(line)
    outfile.write(tline + "\n")

  infile.close()
  outfile.close()
  os.remove(ip )
ip = sys.argv[-1]
f = open(ip)
firstpass()
assemble()
