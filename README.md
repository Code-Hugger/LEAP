# LEAP
Learning Environment for Advanced Python. The simple and extendable framework for creating CTF style programming puzzles.

play.py shows an example of how to interact with the game server, as well as solutions for all the challenges in the "basics" module.

server.py and remote.py show an example of how you can store the business logic (and score mechanism) on a remote server.

When the game engine object is created it will look for any .py or .pyc files in the game folder that don't start with a _ and import them, it will then rip out all objects created by those scripts that don't start with a _. Be careful with global objects as the game server may interpret them as being game modules to load.

To create a new challenge to solve use the format provided at the top of "basics.py". 'data' and 'answer' are hard coded variables but **kwargs exists for future releases to not break existing challenges. Currently the only thing implemented in kwargs is 'playerName' when used for remote scoring.

When a challenge is submitted to the game engine it will request 100 sets of data from the challenge and run your function against all those sets. The solution will only be marked as correct if all 100 attemps return True from the challenge. This means net code will make 200 connections per challenge submission. 100 for data requests, 100 for answer submissions.
