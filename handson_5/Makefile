CC = /usr/bin/gcc
LINK = /usr/bin/gcc

CFLAGS = -m32  -Wall -ggdb3 -O0 -fno-stack-protector -no-pie

BIN = chall
SRC := $(wildcard *.c)

all: $(BIN)

$(BIN):
	$(CC) $(CFLAGS) -o $(BIN) $(SRC)

clean:
	rm $(BIN)