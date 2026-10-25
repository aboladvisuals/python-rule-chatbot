# Rule-Based Chatbot

A command-line bot that answers only the messages stored in a dictionary. Unknown text gets one fallback. `quit` stops it.

## How to run

```powershell
python chatbot.py

Try hello, help, python, data, and quit.How it works
A while loop keeps asking until you quit.
Input is cleaned with .strip().lower() before it is checked.
Replies live in a dictionary. There is one if for a match and one else for everything else.
The bot does not learn and does not call a language model.
Files
















FileWhat it ischatbot.pyThe programREADME.mdThis page