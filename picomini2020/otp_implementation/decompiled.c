#include <stdio.h>
#include <stdint.h>
#include <string.h>


uint8_t valid_char(char param_1)

{
  uint8_t uVar1;
  if ((param_1 < '0') || ('9' < param_1)) {
    if ((param_1 < 'a') || ('f' < param_1)) {
      uVar1 = 0;
    }
    else {
      uVar1 = 1;
    }
  }
  else {
    uVar1 = 1;
  }
  return uVar1;
}

uint32_t jumble(char param_1)
{
  int8_t bVar1;
  int8_t local_c;
  /* '`' == 0x60 == 90 */
  local_c = param_1;
  if ('`' < param_1) {
    /* '\t' == 0x9 */
    local_c = param_1 + '\t';
  }
  /* always 0 */
  bVar1 = (int8_t)((char)local_c >> 7) >> 4;
  /* local_c = (local_c * 2) */
  local_c = ((local_c + bVar1 & 0xf) - bVar1) * '\x02';
  if ('\x0f' < (char)local_c) {
    local_c = local_c + 1;
  }
  return (uint32_t)local_c;
}

char hex [] = {'0', '1', '2', '3', '4', '5', '6' ,'7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
char ans [] = "jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan";

int main (int param_1, char** param_2) {
  int8_t bVar1;
  int iVar2;
  uint8_t uVar3;
  uint32_t uVar4;
  long in_FS_OFFSET;
  int local_f0;
  int local_ec;
  char local_e8 [100];
  int local_84;
  char local_78 [104];
  long local_10;


  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  if (param_1 < 2) {
    printf("USAGE: %s [KEY]\n",*param_2);
    uVar3 = 1;
  }
  else {
    strncpy(local_e8,(char *)param_2[1],100);
    local_84 = 0;
    local_f0 = 0;
    int i = 0;
    while( 1 ) {

      /*
      local_e8 [local_f0] = hex [i];
      i = (i + 1) % 16;
      uint32_t tmp1 = uVar3;
      uint32_t tmp2 = uVar4;
      uint32_t tmp3 = bVar1;
      uint32_t tmp4 = local_78 [local_f0];
      uint32_t tmp5 = iVar2;
      */

      uVar3 = valid_char(local_e8[local_f0]);
      if ((int)uVar3 == 0) break;
      if (local_f0 == 0) {
        uVar4 = jumble(local_e8[0]);
        bVar1 = (int8_t)((char)uVar4 >> 7) >> 4;
        local_78[0] = (((char)uVar4 + bVar1 & 0xf) - bVar1);
      }
      else {
        uVar4 = jumble(local_e8[local_f0]);
        iVar2 = (int)(char)uVar4 + (int)local_78[local_f0 + -1];
        bVar1 = (int8_t)(iVar2 >> 0x37);
        local_78[local_f0] = ((char)iVar2 + (bVar1 >> 4) & 0xf) - (bVar1 >> 4);
      }

      //if brute doesnt work
      /*
      if (local_78 [local_f0] + 'a' != ans [local_f0]) {
        uVar3 = tmp1;
        uVar4 = tmp2;
        bVar1 = tmp3;
        local_78 [local_f0] = tmp4;
        iVar2 = tmp5;
        continue;
      }
      */
      local_f0 = local_f0 + 1;
    }

    local_ec = 0;
    while (local_ec < local_f0) {
      local_78[local_ec] = local_78[local_ec] + 'a';
      local_ec = local_ec + 1;
    }
    printf ("%s\n", local_78);
    if (local_f0 == 100) {
      iVar2 = strncmp(local_78,
                      "jbgkfmgkknbiblpmibgkcneiedgokibmekffokamknbkhgnlhnajeefpekiefmjgeogjbflijnekebeokpgngjnfbimlkdjdjhan"
                      ,100);
      if (iVar2 == 0) {
        puts("You got the key, congrats! Now xor it with the flag!");
        uVar3 = 0;
        return 0;
      }
    }
    //puts("Invalid key!");
    uVar3 = 1;
  }
  return 0;
}
