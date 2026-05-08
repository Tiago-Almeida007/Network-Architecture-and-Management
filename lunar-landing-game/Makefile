DEFINES=
#DEFINES= -DDEBUG
OPTIONS= -g 
#OPTIONS += -Wall -ansi -pedantic 
#OPTIONS= -O
CC=gcc

all : lunar-landing-game
	rm -f *.o

lunar-landing-game : lunar-landing-game.o
	$(CC) $(OPTIONS) -o lunar-landing-game lunar-landing-game.o -lm

clean :
	rm -f lunar-landing-game core *.o

zip : lunar-landing-game.zip
	rm -f lunar-landing-game.zip
	zip -9 lunar-landing-game *.c *.py *.txt Makefile

