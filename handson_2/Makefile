CC = /usr/bin/gcc
LINK = /usr/bin/gcc

CFLAGS = -m32  -Wall -ggdb3 -O0 -no-pie

BIN = chall
BIN_2 = chall_2
SRC := $(wildcard *.c)

all: $(BIN)  $(BIN_2) 

$(BIN):
	$(CC) $(CFLAGS) -z execstack -o $(BIN) $(SRC)

$(BIN_2):
	$(CC) $(CFLAGS) -o $(BIN_2) $(SRC)

clean:
	rm $(BIN)*