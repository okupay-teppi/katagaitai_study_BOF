#include <stdio.h>

int main(void) {
  char name[0x100];
  puts("What's your team name?");
  fgets(name, 0x160, stdin);
  
  printf("Hi, %s. Welcome to OkuPay CTF 2020!\n", name);
  return 0;
}

__attribute__((constructor))
void setup(){
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}