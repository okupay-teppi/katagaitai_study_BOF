/* handson_5.c */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void vul_1()
{
  char buf1[30] = {};
  puts("hello");
  gets(buf1);
  puts(buf1);
}

int main(void)
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