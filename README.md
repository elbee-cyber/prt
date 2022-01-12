# Hackerone Passive Recon Tool
**A passive-recon tool that parses through found assets and interacts with the Hackerone API.**

![Demo](https://s10.gifyu.com/images/ezgif.com-gif-maker478b5d3b2a6a6a97.gif)

### Setup
Simply run `setup.sh` to automatically install the required python libraries.

### Usuage
```
  -q, --quiet           Do not display banner.
  -u USER, --user USER  Hackerone username.
  -t TOKEN, --token TOKEN
                        Hackerone API token.
  -p PROGRAM, --program PROGRAM
                        Program handle, not program name.
  -i, --info            Display program information.
  -o OUTPUT, --output OUTPUT
                        Output results to a file.
  -w WAIT, --wait WAIT  Pause between Google dorks.
  -n, --noprint         Don't print found assets at the end of execution.
 ```


### The Process
- First, the program scope information is retrieved using the provided token and the H1 API.
- The base scope is sent to **crt.sh** where certificate transparency is checked.
- The base scope is sent to Sublist3r.
- The base scope's pages are parsed for additional assets.
- Results are printed and grepped.
Throughout the process, assets that are out of scope are dropped.

This tool should not be relied on soley to retrieve accurate and culminating results. Use your arsenal and judgement. I am not responsible for the misuse of this tool.

https://buymeacoffee.com/elbee1

https://twitter.com/elbee_ez
