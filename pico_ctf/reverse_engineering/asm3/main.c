#include <stdio.h>

extern int asm3 (int, int, int);

int main () {
  printf ("james: %x\n", asm3(0xd73346ed,0xd48672ae,0xd3c8b139));
  return 0;
}
