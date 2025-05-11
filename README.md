# CryptoChat

Chat for private conversations.

> "Truth is protected by cipher, as the soul is protected by silence." _

Description CryptoChat is a minimalistic console application that allows you to conduct secure correspondence between users.

## Features (planned):
- Asymmetric key generation 
- Message encryption 
- Peer-to-peer connection 
- TUI interface 
## Stack 
- Python 3 
- PyNaCl or cryptography 
-Sockets 
- curses (future)

## connect to server
There are two types of connection in the program: 
1. Local. 2. Public.
To connect publicly, use Radmin VPN or Hamachi.
Once you've set up a VPN, start the server, and connect to it through the IP address that you wrote either when you started the server or in the VPN itself.

## launch
`bash
python main.py - generate secret.key

python server.py - start server

python client.py - start client

-----------------------------------------
how to setup?

chmod +x setup.sh

./setup.sh
