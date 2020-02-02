# Blind XXE Payload Generator
The purpose of this project is to help ethical hackers easily detect Blind XXE by generating payloads that use a freshly generated postbin.  
If the server is vulnerable to Blind XXE, the postbin will log a request from the server's IP address.  

## Setup
Use `git clone https://github.com/discodamone/XXE-Generator.git`  
*optional: make blindxxe.py executable with `chmod +x blindxxe.py`*  

## Usage
`python3 blindxxe.py -h` for help  

## Example
`python3 blindxxe.py -c -t -f png jpg svg pdf gif docx`  
This will clear all of the files from the payload folder, print the payload in text, and create a file for each filetype listed after.  
