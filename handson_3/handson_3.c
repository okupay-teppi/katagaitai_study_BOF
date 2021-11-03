/*handson_3.c */
#include <stdio.h>
#include <stdlib.h>

void cheat()
{
  system("/bin/sh");
  exit(0);
}


void vul_1()
{
  char buf1[30] = {};  /* set all bytes to zero */
  printf("buf1 = %p\n", buf1);
  puts("hello");
  
  gets(buf1);
  puts(buf1);
}

int main(int argc, char *argv[])
{
  vul_1();	
  return 0;
}

__attribute__((constructor))
void setup(){
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}