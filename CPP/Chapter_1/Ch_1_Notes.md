# Chapter 1 Notes

## Summary

- A basic introduction to programming with an emphasis on C++
- 'Anatomy of a computer'
  - CPU, memory, I/O devices,
- Primary v Secondary memory (RAM v HDD) 
  - RAMrequires electricity to operate
  - SSD/HHD memory persists when here is no power
- Standards organizations (ISO, ANSI)
  - ensure interoperability across different platforms.
- Flow of a program:
- Editor -> Source Filer ->Compiler -> Machine Code/Library Files -> Linker -> Executable
- Most C++compilers require files to end in an extension of .cpp, .cxx, .cc, or .c,
- Backup files often with multiple directories for the backups

### Code Break Down

#include <iostream> - this is similar to the 'import' statement in python

using namespace std; - Namespaces are used to avoid name collisions. Not covered in this chapter

int main() - This is the entry point of the program and every program must have a main function
{
    cout << "Hello World!" << endl; - cout = c out or console output. Similar to print in python. << before whatever you send to cout. << endl starts a new line
    return 0;
}
