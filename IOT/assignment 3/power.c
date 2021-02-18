#include "contiki.h"
#include "net/rime.h"
#include "random.h"

#include "powertrace.h"

#include "dev/button-sensor.h"

#include "dev/leds.h"
#include "dev/sht11-sensor.h"

#include <stdio.h>
/*---------------------------------------------------------------------------*/
PROCESS(process1, "powertrace example");
AUTOSTART_PROCESSES(&process1);
/*---------------------------------------------------------------------------*/
PROCESS_THREAD(process1, ev, data)
{
  static struct etimer et;


  PROCESS_BEGIN();


  /* Start powertracing, once every second. */
  powertrace_start(CLOCK_SECOND * 1);
  
  int number1 =10, number2 =20;
  int sum;

  int multiplication;
  while(1) {
    /* Delay 2-4 seconds */
    etimer_set(&et, CLOCK_SECOND * 4 + random_rand() % (CLOCK_SECOND * 4));

    PROCESS_WAIT_EVENT_UNTIL(etimer_expired(&et));
    sum = number1+number2;
    multiplication = number1 * number2;
    printf("Sum : %d", sum);
    printf("multiplication : %d", multiplication);
  }

  PROCESS_END();
}
/*---------------------------------------------------------------------------*/

