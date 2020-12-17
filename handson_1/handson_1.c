/* handson_1 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void vuln(){
  char buf[16];
  int secret = 0;
  gets(buf);

  if (secret == 0xdeadbeef){
    puts("Congratulations!!");
  }
  else{
    printf("The secret is %x\n", secret);
  }
}

int main(){
  vuln();
  return 0;
}
