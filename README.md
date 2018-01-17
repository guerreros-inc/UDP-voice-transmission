# UDP-voice-transmission
Two simple server-client scripts for transmitting voice via UDP (unidirectional)

This allows you to transmit voice messages from a client to a server in realtime at high quality. Just start your server (receiver) script on one machine and a client (transmitter) on another machine in the same network. The microphone stream from the transmitter is then being sent to the receiver (speaker or line-out). As we are using UDP here is no need for a handshake. As soon as server and client are both running, the transmission is active.
