#!/bin/sh

curl -O https://golang.org/dl/go1.14.4.linux-armv6l.tar.gz
tar -xvf go1.14.4.linux-armv6l.tar.gz


sudo chown -R root:root ./go
sudo mv go /usr/local

export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin

