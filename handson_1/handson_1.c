/* handson_1 */
#include <stdio.h>

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

__attribute__((constructor))
void setup(){
    setvbuf(stdin,  NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}