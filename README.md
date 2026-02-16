# Verilog Template & Testbench Generator  
A Python-based GUI tool for automatically generating Verilog module templates and corresponding testbench files.

## 📌 Project Overview
This project provides an automated way to generate:
- A Verilog **design module** template  
- A matching **testbench module**  
- Automatic instantiation and signal wiring  
- Basic test cases for simulation  

The tool uses a simple Tkinter interface to collect user inputs and then generates two separate `.v` files:
1. `<ModuleName>.v` – Design module  
2. `<ModuleName>TestBench.v` – Testbench module  

This helps students and engineers quickly scaffold Verilog projects without writing repetitive boilerplate code.

---

## 🚀 Features
### **✔ Automatic Module Generation**
- Validates module names (avoids reserved keywords)
- Supports multiple inputs and outputs
- Allows custom signal widths
- Supports wire/reg output types

### **✔ Always Block Templates**
- Optional combinational blocks (`always @(*)`)
- Optional sequential block  
  - Synchronous (`posedge clk`)  
  - Asynchronous (`posedge clk or negedge rst`)  

### **✔ Testbench Generation**
- Automatic signal declaration (`reg` for inputs, `wire` for outputs)
- Automatic DUT instantiation
- Clock generation (if sequential logic is selected)
- Two randomized test cases using `$random`
- `$monitor` block for observing signal activity

---

## 🧠 How It Works
The program:
1. Prompts the user for module name  
2. Collects input/output signal names and widths  
3. Asks whether combinational or sequential blocks are needed  
4. Generates the design module file  
5. Generates the testbench file with:
   - Signal declarations  
   - DUT instantiation  
   - Clock/reset logic  
   - Test cases  
   - Monitoring  

---

## 📂 Output Files
The tool generates two files:

| File | Description |
|------|-------------|
| **`<ModuleName>.v`** | Verilog design module |
| **`<ModuleName>TestBench.v`** | Testbench module with DUT instantiation |

---

## 🛠 Technologies Used
- **Python 3**
- **Tkinter** (GUI)
- **Verilog HDL**

---

## 📥 How to Run
1. Install Python 3  
2. Ensure Tkinter is installed (included by default in most Python installations)  
3. Run the script:

```bash
python verilog_generator.py

---

👤 **Author**

Omar Elbasiouny  
📧 **Email:** omarelbasiony24@gmail.com

This project was developed as a final project to facilitate the Verilog development workflow.

