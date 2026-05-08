#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# lunar-landing-game.py
# Python program to play Lunar Landing Game
#
import sys, os, math

play_again= 1

while (play_again):
  altitude=2350.0
  velocity=-470.0
  fuel=600
  burn=0
  time_interval=1;
  g=-5.0;

  print("\nLunar Landing Game")
  print("You are in a spacecraft approaching the moon. The onboard computer malfunctioned.")
  print("You have to manually choose the amount of fuel to burn to land with zero velocity.")
  print("Using more fuel, you reduce the velocity more, and vice-versa.\n")

  while (altitude > 0 and fuel > 0):
    print("Altitude=%f\tVelocity=%f\tFuel=%d" % (altitude, velocity, fuel))
    burn= int(input("Amount of fuel to burn [0-75]: "))
    if (burn > 75):
        burn=75
        print("Using the maximum of 75 fuel.")
    if (burn < 0):
        burn=0
        print("Using the minimum of 0 fuel.")
    if (burn > fuel):
        burn=fuel
        print("\nNo more fuel! You can only use %f." % burn)
    fuel-= burn;
    altitude= altitude+velocity*time_interval+(burn+g)*time_interval*time_interval/2.0
    if (altitude < 0):
      print("\nYou crashed at a speed of %f" % velocity)
      break
    velocity=velocity+(burn+g)*time_interval

  if (altitude==0 and velocity==0):
    print("Congratulations: you landed safely, with %d fuel left.\n" % fuel)
  else:
    if (fuel <= 0):
      print("You run out of fuel! You are falling from an altitude of %f.\n" % altitude)
      velocity= -math.sqrt(velocity*velocity-2*g*altitude)
      print("You crashed at a speed of %f.\n" % velocity)

  play_again= (input("Want to play again? [y/n] ")!="n")
