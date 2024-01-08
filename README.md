# Social Bots

Social Bots is a collection of containerized bots (e.g. Discord, Telegram, etc) where each bot is hosted in an isolated container. 
Each bot container also hosts an API to allow it to recieve messages that are to be sent to their respective social apps.
An extra container is hosted alongside, that acts as the centralized storage for the API keys of every bot.

The goal is to create a simple and easily accessible API framework that is able to provide notification and messaging capabilites to other projects.