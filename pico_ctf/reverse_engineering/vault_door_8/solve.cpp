#include <bits/stdc++.h>

int switchBits(int c, int p1, int p2) {
  /* Move the bit in position p1 to position p2, and move the bit
     that was in position p2 to position p1. Precondition: p1 < p2 */
  int mask1 = (int)(1 << p1);
  int mask2 = (int)(1 << p2);
  /* int mask3 = (int)(1<<p1<<p2); mask1++; mask1--; */
  int bit1 = (int)(c & mask1);
  int bit2 = (int)(c & mask2);
  /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
     System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
  int rest = (int)(c & ~ (mask1 | mask2));
  int shift = (int)(p2 - p1);
  int result = (int)((bit1 << shift) | (bit2 >> shift) | rest);
  return result;
}

int main () {
  int expected[] = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xE0, 0x95, 0xF1, 0xE1, 0xE0, 0xA4, 0xC0, 0x94, 0xA4};
  printf ("picoCTF{");
    for (int i = 0; i < 32; i++) {
      int c = expected [i];
      c = switchBits(c, 6, 7);
      c = switchBits(c, 2, 5);
      c = switchBits(c, 3, 4);
      c = switchBits(c, 0, 1);
      c = switchBits(c, 4, 7);
      c = switchBits(c, 5, 6);
      c = switchBits(c, 0, 3);
      c = switchBits(c, 1, 2);
      printf ("%c", c);
    }
  puts ("}");
  return 0;
}
