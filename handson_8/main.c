#include <stdio.h>

int main(void) {
  char name[0x100];
  puts("What's your team name?");
  fgets(name, 0x160, stdin);
  
  printf("Hi, %s. Welcome to OkuPay CTF 2020!\n", name);
  return 0;
}
