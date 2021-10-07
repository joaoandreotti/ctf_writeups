#include <bits/stdc++.h>

int main () {
  int x [8];
  x[0] = 1096770097;
  x[1] = 1952395366;
  x[2] = 1600270708;
  x[3] = 1601398833;
  x[4] = 1716808014;
  x[5] = 1734304867;
  x[6] = 942695730;
  x[7] = 942748212;

  int tmp = (1 << 8) - 1;
  int y[] = {tmp, tmp << 8, tmp << 16, tmp << 24};

  printf ("picoCTF{");
  for (char i = 0; i < 8; i++)
    for (char j = 3; j >= 0; j--)
      printf ("%c", (x [i] & y [j]) >> (j * 8));
  puts ("}");
  return 0;
}
