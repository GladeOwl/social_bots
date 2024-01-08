# Social Bots

Social Bots is a collection of containerized appication where each social bot (e.g. Discord, Telegram, etc) are hosted in an isolated container. Each bot container also hosts an API to allow it to recieve messages that are to be sent to their respective social apps.
An extra container is hosted alongside, that acts as the centralized storage for the API keys of each Bot.

The goal is to create a simple and easily accessible API framework that is able to provide notification and messaging capabilites to other projects.