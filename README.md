# Hackerone Passive Recon Tool
**LA passive-recon tool that parses through found assets and interacts with the Hackerone API.**

![Demo](https://s10.gifyu.com/images/ezgif.com-gif-maker478b5d3b2a6a6a97.gif)

### Setup
Simply run `setup.sh` to automatically install the required python libraries.

### Usuage


### The Process
- First, the program scope information is retrieved using the provided token and the H1 API.
- The base scope is sent to **crt.sh** where certificate transparency is checked.
- The base scope is sent to Sublist3r.
- The base scope's pages are parsed for additional assets.
- Results are printed and grepped.
Throughout the process, assets that are out of scope are dropped.

This tool should not be relied on soley to retrieve accurate and culminating results. Use your arsenal and judgement. I am not responsible for the misuse of this tool.
