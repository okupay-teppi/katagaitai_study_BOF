#include <stdio.h>

void vuln()
{
  char buf[100] = {};
  printf("buf = %p\n", buf);
  gets(buf);
  puts(buf);
}

int main(int argc, char *argv[])
{
  vuln();
  return 0;
}

__attribute__((constructor))
void setup(){
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}