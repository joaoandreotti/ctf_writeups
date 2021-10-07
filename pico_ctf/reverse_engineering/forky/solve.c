#include <stdio.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  int *x;
  *x = 1000000000;
  for (int i = 0; i < 16; i++)
    *x = *x + 0x499602d2;
  printf ("ans: %d\n", *x);
  return 0;
}
