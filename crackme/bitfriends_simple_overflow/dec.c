#include <stdio.h>
#include <stdlib.h>

void login(void)
{
  char *__s;
  unsigned int *puVar1;
  printf("enter password: ");
  __s = (char *)malloc(0x10);
  puVar1 = (unsigned int *)malloc(8);
  *puVar1 = 1;
  fgets(__s,0xa0,stdin);
  printf("uid: %x\n",(unsigned long)*puVar1);
  if (*puVar1 == 0) {
    puts("you are logged in as admin");
  }
  else {
    puts("you are logged in as user");
  }
  return;
}

int main () {
  login ();
  return 0;
}
