#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
  double altitude=2350;
  double speed=-470;
  int fuel=600;
  int burn=0;
  int time_interval=1;
  double g=-5;

  do {
    printf("Altitude=%f\tSpeed=%f\tFuel=%d\n", altitude, speed, fuel);
    printf("Fuel to burn: ");
    scanf("%d", &burn);
    if (burn > 75) burn=75;
    if (burn < 0) burn=0;
    if (burn > fuel) burn=fuel;
    fuel-= burn;
    altitude= altitude+speed*time_interval+(burn+g)*time_interval*time_interval/2;
    if (altitude < 0) {
      printf("You crashed at speed %f\n", speed);
      break;
    }
    speed=speed+(burn+g)*time_interval;

  } while (altitude > 0 && fuel > 0);

  if (altitude==0 && speed==0)
    printf("Congratulations: you landed safely with %d fuel left\n", fuel);
  else {
    if (fuel <= 0) {
      printf("No fuel\n");
      speed=-sqrt(speed*speed-2*g*altitude);
      printf("You crashed at speed %f\n", speed);
    }
  }
  return 0;
}
