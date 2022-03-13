# Pokefinder-Infrastructure-Stack

This is the Repository, to create an Infrastructure Stack for Pokefinder Discord Bot.

This Stack includes:

MariaDB: SQL Database for storing all relevant information 
PHPMyAdmin: User Interface to check the Database
Mosquito: MQTT Broker to recieve Commands
Webhook: Webhook Reciever

Installation:

first this is not a secure installation. All Ports are open to the Internet. If your just run this on your local computer this is not a big deal, there are inly reachable in your home network. But if you prefer to run this on a server, please change the ports and activate the Authentification for mosquitto.

1. Clone the repository:
`git clone https://github.com/SpielerNogard/Pokefinder-Infrastructure-Stack.git`
2. Change the MariaDB Root Password inside the `docker-compose.yaml`
3. change the ports to something you prefer or better just delete them and only open them to localhost.
4. run: `docker-compose up -d` to start the stack.