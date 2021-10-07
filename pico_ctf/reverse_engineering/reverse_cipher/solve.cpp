#include <bits/stdc++.h>

// ciphered flag: picoCTF{w1{1wq84fb<1>49}

int main () {
  std::string str = "w1{1wq84fb<1>49";
  for (int i = 0; i < str.size (); i++)
    if (i & 1)
      str [i] += 2;
    else
      str [i] -= 5;
  printf ("picoCTF{%s}\n", str.c_str ());
  return 0;
}
