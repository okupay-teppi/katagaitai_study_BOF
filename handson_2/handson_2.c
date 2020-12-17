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
