#include "contiki.h"
#include <stdio.h>
#include <random.h> /* For random_rand() */


PROCESS(hello_world_process, "Hello world process");
AUTOSTART_PROCESSES(&hello_world_process);

PROCESS_THREAD(hello_world_process, ev, data)
{
  PROCESS_BEGIN();
  printf("Hello, world\n");

  printf("Generating 10 random numbers between 0 and 1\n\n");
  int count= 10;
  int i;
  float sum = 0;
  for (i = 0; i < count; i++) {
       double randomNumber = (double)random_rand() / (double)RANDOM_RAND_MAX ;
       printf("%.8f\n", randomNumber);
       sum = randomNumber+sum;
  }
  printf("The sum of all the generated random numbers is %.8f\n", sum);
  PROCESS_END();
}
