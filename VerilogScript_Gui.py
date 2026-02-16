
import tkinter as tk
from tkinter import simpledialog

# Function to get get_input with a dialog box
def get_input(prompt):
    return simpledialog.askstring("get_input", prompt)

# Function to display messages
def show_message(message):
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, message + "\n")
    text_output.config(state=tk.DISABLED)



# Create main window
root = tk.Tk()
root.title("Verilog Code Generator")


# Create Text widget for displaying output
text_output = tk.Text(root, height=60, width=100, state=tk.DISABLED)
text_output.pack()


root.withdraw()






 
## Don't Get Shocked It is Just the Reserced KeyWords :)
 
ReservedWords = {'always': 0, 'end': 0, 'ifnone': 0, 'or': 0, 'rpmos': 0, 'tranif1': 0,
          'and': 0, 'endcase': 0, 'initial': 0, 'output': 0, 'rtran': 0, 'tri': 0, 'assign': 0, 'endmodule': 0,
          'inout': 0, 'parameter': 0, 'rtranif0': 0, 'tri0': 0, 'begin': 0, 'endfunction': 0, 'input': 0,
          'pmos': 0, 'rtranif1': 0, 'tri1': 0, 'buf': 0, 'endprimitive': 0, 'integer': 0, 'posedge': 0,
          'scalared': 0, 'triand': 0, 'bufif0': 0, 'endspecify': 0, 'join': 0, 'primitive': 0, 'small': 0,
          'trior': 0, 'bufif1': 0, 'endtable': 0, 'large': 0, 'pull0': 0, 'specify': 0, 'trireg': 0,
          'case': 0, 'endtask': 0, 'macromodule': 0, 'pull1': 0, 'specparam': 0, 'vectored': 0, 'casex': 0,
          'event': 0, 'medium': 0, 'pullup': 0, 'strong0': 0, 'wait': 0, 'casez': 0, 'for': 0, 'module': 0,
          'pulldown': 0, 'strong1': 0, 'wand': 0, 'cmos': 0, 'force': 0, 'nand': 0, 'rcmos': 0, 'supply0': 0,
          'weak0': 0, 'deassign': 0, 'forever': 0, 'negedge': 0, 'real': 0, 'supply1': 0, 'weak1': 0,
          'default': 0, 'for': 0, 'nmos': 0, 'realtime': 0, 'table': 0, 'while': 0, 'defparam': 0,
          'function': 0, 'nor': 0, 'reg': 0, 'task': 0, 'wire': 0, 'disable': 0, 'highz0': 0, 'not': 0,
          'release': 0, 'time': 0, 'wor': 0, 'edge': 0, 'highz1': 0, 'notif0': 0, 'repeat': 0, 'tran': 0,
          'xnor': 0, 'else': 0, 'if': 0, 'notif1': 0, 'rnmos': 0, 'tranif0': 0, 'xor': 0}




## Lists and Dictionaries to collect Design Information 
Inputs = {}

Outputs={}

Choose_Between_Inputs_Or_Outputs={1:Inputs,2:Outputs}

Type={1:'input',2:'output'}

SignalType={'w':'','r':'reg'}

OutputType ={}

CombNum = 0 

AlwaysComb = ''

AlwaysSeq = ''



### Colors--------------------------------------------------

CYAN = '\033[1;36m'
GREEN = '\033[1;32m'
RED = '\033[1;31m'
BLUE = '\033[1;34m'
RESET = '\033[0m'
YELLOW = '\033[1;33m'
Font= '\033[3m'
UNDERLINE = "\033[4m"

BOLD = "\033[1m"

DARK_BLUE = "\033[0;34m"
LIGHT_PURPLE = "\033[1;35m"

## -----------------------------------------------------------                  



## Collecting Data



while True:
    
    ModuleName= get_input("\nEnter Module Name"+' : ')
    if not(ModuleName in ReservedWords.keys()):
        
        if (ModuleName[0].isalpha() or ModuleName[0] == '_' ):
            for char in ModuleName[1:len(ModuleName)]:
            
                if not (char.isdigit() or char.isalpha() or char =='$' or char =='_'):
                    show_message("/nEnter Valid Name !")
                    break  
                      
                else:
                    continue 
                
            else:
                break
                
        else:
            show_message("\nEnter Valid Name !")
            continue
        
        
    else:
        show_message("\nReserved KeyWord !! Enter Another Name")
        continue
            
    
    
## Collecting Inputs & Outputs Signals names ---------------------



show_message("\n>>>>>>>>>>>> Enter the Inputs >>>>>>>>>>>>")
Choice = 1
OutType = 'w'    
while True:
    
    
    
    SignalsNumber=get_input("\nEnter the Signals number"+' : ')
    
    if SignalsNumber.isdigit() and int(SignalsNumber) >0:
        
        for i in range(int(SignalsNumber)):
            
            while True:
            
                    SignalName=get_input("\nEnter the Signal Number "+str(i+1)+" Name : ")
                     
                    
                    if not(SignalName in ReservedWords.keys()):
                        
                        if SignalName in Inputs.keys() or SignalName in Outputs.keys():
                            
                            show_message("\nSignal Already exist !")
                            
                            continue
                    
                    
                    
                        else:
                        
                            
                        
                            if (SignalName[0].isalpha() or SignalName[0] == '_'):
                            
                                for char in SignalName[1:len(SignalName)]:
                                
                    
                                    if not (char.isdigit() or char.isalpha() or char =='$' or char =='_'):
                                    
                                        show_message("\nEnter Valid Name !")
                                        break  
                                
                                    
                                    
    
    
 ## Collecting Output Signals Types ----------------------------------                               
                    
 
    
                                else:
                                
                                    if Choice ==2:
                                        while True: 
                                                    
                                            OutType=str.lower(get_input("\n-----Enter Signal Type-----\n>>"+' W '+"for wire >>"+' R '+"for Reg"+" : "))
                                        
                                            if not (OutType =='w' or OutType =='r'):
                                            
                                                show_message("\nEnter valid Choice !")
                                                continue
                                        
                                            else:
                                            
                                                OutputType.update({SignalName:SignalType[OutType]})
                                                break
                                            break
                                            
                                    break              
                                continue              
                
                            else:
                            
                                show_message("\nEnter Valid Name !")
                                continue
                            
                    else:
                        show_message("\nReserved KeyWord !! Enter Another Name")
                        continue
                               
                              
                    break
                
## Collecting Signals Sizes -----------------------------------------  
   


               
            while True:
                
                Signal_Size=get_input('\nEnter '+SignalName+' Width'+': ')
                
                if not (Signal_Size.isdigit() and int(Signal_Size) > 0):
                    
                    show_message("\nEnter Valid number !")
                    continue
                
                else:
                    
                    Signal_Size=int(Signal_Size)-1
                    show_message('\n>>Signal '+SignalName+' Added')
                    break
                
            Choose_Between_Inputs_Or_Outputs[Choice].update({SignalName:Signal_Size})
            
        else:
            
            if int(Choice) ==2:
                break
            
        Choice =2
        show_message('\n>>>>>>>>>>>>> Enter Outputs >>>>>>>>>>>>> ')
        continue
            
    else:
        
        show_message("\nEnter Valid Number !") 
        continue






## Collecting Always Blocks Information ---------------------------
    



               
while True:
                   
    AlwaysComb=str.lower(get_input("\nDo you want Combinational blocks ?"+"(Y/N)"+" : "))
                   
    if not(AlwaysComb == 'y' or AlwaysComb == 'n'):
                       
        show_message("\nEnter a Valid Answer !")
        continue
                   
   
            
            
    if AlwaysComb =='y':
                   
        while True:
                           
            CombNum=get_input("\nEnter Number of Combinationa blocks"+": ")
                       
                       
            if not(CombNum.isdigit() and int(CombNum) > 0):
               show_message("\nEnter Valid number !")
               continue
                       
            else:
                break
    
       
    while True:
           
        AlwaysSeq=str.lower(get_input("\nDo you want a Sequntial block ?"+"(Y/N)"+":"))
        if not(AlwaysSeq == 'y' or AlwaysSeq =='n'):
                          
            show_message("\nEnter a Valid Answer !")
            continue
                      
        else:
            break
               
               
    if AlwaysSeq =='y':
                      
       while True:
                          
           SyncOrAsynch=str.lower(get_input("\nAsynchronous or Synchronous?\n\n"+">>>Enter "+'A'+" for Asynchronous >>  "+'S'+" for Synchronous"+": "))    
               
           if not(SyncOrAsynch == 'a' or SyncOrAsynch == 's'):
               show_message("\nEnter Valid Choice !")
               continue
               
           else:
               Inputs.update({'clk' :0 ,'rst':0}) 
               break
                   
                       
    break           
      



## Organizaing Data ---------------------------------------------

FinalSignals = []


for char in Inputs:
    FinalSignals.append(char)
    


for char in Outputs:
    FinalSignals.append(char)
         







## Printing Signals Declaration  -------------------------------------



F=open(ModuleName+'.v','w') 

F.write('Module  '+ModuleName+'(') 

F.write(",".join(FinalSignals)+');\n')  





for i in Inputs:
    
    if Inputs[i] == 0: 
        
        F.write('input '+i+' ;\n')
        
    else:
        
        F.write('input '+'['+str(Inputs[i])+':0]'+' '+i+' ;\n')
    
    
    
    
    
for i in Outputs:
    
    if Outputs[i] == 0:
        
        F.write('output '+' '+OutputType[i]+' '+i+' ;\n')
        
    else:
        F.write('output '+OutputType[i]+' '+'['+str(Outputs[i])+':0]'+' '+i+' ;\n')
        
        
        
 
## Printing Always Blocks ------------------------------------------        
 
        
if  AlwaysSeq == 'y':
    
    if SyncOrAsynch == 'a':
        
        F.write("\nalways @(posedge clk or negedge rst) begin\n if (!rst) begin \n \nend\nend")
    else:
        F.write("\nalways @(posedge clk) begin \n if (!rst) begin \n\nend\nend ")
        
        
if AlwaysComb == 'y':
    
    for i in range(int(CombNum)):
        
        F.write("\nalways @(*) begin \n \n end\n")
        
        
        
F.write("\n\nendmodule")
        
F.close()  




## creating TestBench -----------------------------------------------


F1=open(ModuleName+'TestBench'+'.v','w') 
F1.write('`timescale 1ns/1ps\nModule  '+ModuleName+'_TB'+'();\n') 


## Signals Declaration--------------------------------------


for i in Inputs:
    
    if Inputs[i] == 0: 
        
        F1.write('reg '+i+'_tb'+' ;\n')
        
    else:
        
        F1.write('reg '+'['+str(Inputs[i])+':0]'+' '+i+'_tb'+' ;\n')


for i in Outputs:
    
    if Outputs[i] == 0:
        
        F1.write('wire '+' '+i+'_tb'+' ;\n')
        
    else:
        F1.write('wire '+' '+'['+str(Outputs[i])+':0]'+' '+i+'_tb'+' ;\n')
        
        
        
## Instantiating Design Module -------------------------------
        

F1.write('\n\n'+ModuleName+'    Dut'+'(\n\t\t')

for i in range(len(FinalSignals)):
    FinalSignals[i] =FinalSignals[i]+"_tb"

F1.write(",\n\t\t".join(FinalSignals)+');') 

if  AlwaysSeq == 'y': 
    
    F1.write("\n\n Always #5 clk_tb = ~clk_tb;")
    F1.write("\n\ninitial begin\nclk_tb=0;\nrst_tb=0;\n#5\nrst_tb=1;\n\n") 
    
else:
    
    F1.write("\n\ninitial begin\n\n") 




## First TestCase ---------------------------


for i in Inputs:
    if i != 'clk' and i != 'rst':
        F1.write("\n"+i+"_tb"+"=$random;")
        
F1.write("\n#20;")


## Second TestCase ---------------------------

for i in Inputs:
     if i != 'clk' and i != 'rst':
         F1.write("\n"+i+"_tb"+"=$random;")    
         
         
F1.write("\n#20;\n\n$finish;\n\nend")       


## Monitoring Inputs & Outputs --------------


F1.write("\ninitial begin\n\n$monitor(\" Time : %t ,")



for i in Inputs:
    if i != 'clk' and i != 'rst':
        F1.write(i+"_tb"+" : %d ,")
        

for i in Outputs:
    F1.write(i+"_tb"+" : %d ,")        
        

F1.write("\",$time")




for i in Inputs:
    if i != 'clk' and i != 'rst':
        F1.write(","+i+"_tb")
        

for i in Outputs:
    F1.write(","+i+"_tb")        
        

F1.write(");\n\nend\n\nendmodule")


F1.close()


