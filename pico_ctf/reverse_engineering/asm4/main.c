#include <stdio.h>

extern int asm4(char*);

int main () {
  printf ("james: %x\n", asm4 ("picoCTF_a3112"));
  return 0;
}
