#!/usr/bin/python3

import requests, argparse, sys, os, time, sublist3r, string, random
from googlesearch import search
from bs4 import BeautifulSoup
from tld import get_tld

def banner(hide):
	if hide:
		return
	print("\n\n ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███   ▒█████   ███▄    █ ▓█████       ")
	print("▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀       ")
	print("▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒▒███         ")
	print("░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄       ")
	print("░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░░▒████▒      ")
	print(" ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░      ")
	print(" ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░      ")
	print(" ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ ░ ░ ░ ▒     ░   ░ ░    ░         ")
	print(" ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░         ░ ░           ░    ░  ░      ")
	print("                  ░                                                                ")
	print(" ██▓███   ▄▄▄        ██████   ██████  ██▓ ██▒   █▓▓█████                           ")
	print("▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒ ▓██▒▓██░   █▒▓█   ▀                           ")
	print("▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒██▒ ▓██  █▒░▒███                             ")
	print("▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░██░  ▒██ █░░▒▓█  ▄                           ")
	print("▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░██░   ▒▀█░  ░▒████▒                          ")
	print("▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░░▓     ░ ▐░  ░░ ▒░ ░                          ")
	print("░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░ ▒ ░   ░ ░░   ░ ░  ░                          ")
	print("░░         ░   ▒   ░  ░  ░  ░  ░  ░   ▒ ░     ░░     ░                             ")
	print("               ░  ░      ░        ░   ░        ░     ░  ░                          ")
	print("                                              ░                                    ")
	print(" ██▀███  ▓█████  ▄████▄   ▒█████   ███▄    █    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    ")
	print("▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ")
	print("▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ")
	print("▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ")
	print("░██▓ ▒██▒░▒████▒▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒")
	print("░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░")
	print("  ░▒ ░ ▒░ ░ ░  ░  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░")
	print("  ░░   ░    ░   ░        ░ ░ ░ ▒     ░   ░ ░      ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ")
	print("   ░        ░  ░░ ░          ░ ░           ░                 ░ ░      ░ ░      ░  ░")
	print("\n\nhttps://github.com/elbee-cyber")
	print("https://buymeacoffee.com/elbee1")
	print("https://twitter.com/elbee_ez\n\n")

	time.sleep(2)

def info(obj):
	print("\n"+"="*30+" "+obj["attributes"]["name"]+" "+"="*30)
	fiat=obj["attributes"]["currency"].upper()
	open=obj["attributes"]["submission_state"]=="open"
	if open:
		status="accepting"
	else:
		status="not accepting"
	if obj["attributes"]["state"] == "public_mode":
		state = "public"
	else:
		state = "private"
	bounties=obj["attributes"]["offers_bounties"]
	print("The program is "+state+" and "+status+" submissions.")
	if bounties:
		print("The program is paying in: "+fiat+".")
		print("Does the program allow bounty splitting: "+str(obj["attributes"]["allows_bounty_splitting"]).lower()+".")
	else:
		print("This program does not offer bounties.")
	print("="*(62+len(obj["attributes"]["name"]))+"\n")

def scope(obj):
	out_of_scope = []
	in_scope = []
	for dict in obj:
		for attr,val in dict.items():
			if attr=="attributes":
				if val["asset_type"] == "URL":
					if val["eligible_for_bounty"] == False and val["eligible_for_submission"] == False:
						if val["asset_identifier"][-1] == '/':
							uri = val["asset_identifier"][:-1]
						else:
							uri = val["asset_identifier"]
						out_of_scope.append(uri.replace("https://","").replace("http://","").replace("*.","."))
					else:
						if val["asset_identifier"][-1] == '/':
							uri = val["asset_identifier"][:-1]
						else:
							uri = val["asset_identifier"]
						in_scope.append(uri.replace("https://","").replace("http://","").replace("*.","."))
	print("Scope built!\n")
	print("The following is in scope:\n")
	for i in in_scope:
		print(i)
	print("\n")
	print("The following is out of scope:\n")
	for i in out_of_scope:
		print(i)
	print("\n")
	return out_of_scope,in_scope

def confirm(msg):
	confirmation = input(msg)
	if str(confirmation).upper() != 'Y' and str(confirmation).upper() != 'N':
		print("\nInvalid option!")
		confirm(msg)
	return confirmation.upper()

def main():
	parser = argparse.ArgumentParser(description='Automate a passive recon scan on a given target.')
	parser.add_argument('-q','--quiet',action='store_true',help='Do not display banner.')
	parser.add_argument('-u','--user',type=str,required=True,help='Hackerone username.')
	parser.add_argument('-t','--token',type=str,required=True,help='Hackerone API token.')
	parser.add_argument('-p','--program',type=str,required=True,help='Program handle, not program name.')
	parser.add_argument('-i','--info',action='store_true',help='Display program information.')
	parser.add_argument('-o','--output',type=str,help="Output results to a file.")
	parser.add_argument('-w','--wait',type=int,default=5,help="Pause between Google dorks.")
	parser.add_argument('-n','--noprint',action='store_true',help='Don\'t print found assets at the end of execution.')
	args = parser.parse_args()

	h1user=args.user
	token=args.token
	handle=args.program
	banner(args.quiet)

	domains = []

	session = requests.Session()
	session.auth = (h1user,token)
	session.headers.update({'Accept': 'application/json'})
	try:
		r = session.get("https://api.hackerone.com/v1/hackers/programs/"+handle)
	except:
		print("Error connecting to Hackerone API..")
		print("Quiting.. ")
		sys.exit()
	obj = r.json()
	if args.info:
		info(obj)
	print("\nBuilding scope...")
	out_of_scope,in_scope=scope(obj["relationships"]["structured_scopes"]["data"])
	continue2recon = confirm("Continue to passive recon? (Y/N) ")
	if continue2recon == 'N':
		print("Quiting..")
		sys.exit()

	# Add base in-scope domains
	for i in in_scope:
		if i[0] == '.':
			domains.append(i[1:])
			in_scope[in_scope.index(i)] = i[1:]
		else:
			domains.append(i)
	domains = list(set(domains))

	for i in out_of_scope:
		if i[0] == '.':
			out_of_scope[out_of_scope.index(i)] = i[1:]
	
	# Certificate Transparency
	base = domains.copy()
	skipCertCheck = confirm("It is recommended to check for certificate transparency, would you like to do this? (Y/N) ")
	if skipCertCheck != 'N':
		foo = 1
		tempList = []
		for i in base:
			print(str(foo)+"/"+str(len(base))+" assets checked..", end='\r')
			foo += 1
			tld = get_tld("http://"+i)
			try:
				r = requests.get("https://crt.sh/?q="+i)
			except:
				print("Error connecting to crt.sh.. ")
				print("Quiting.. ")
				sys.exit()
			soup = BeautifulSoup(r.text, 'html.parser')
			for j in soup.find_all('tr'):
				for x in j.find_all('td'):
					bar = x.getText()
					if " " not in bar and tld in bar:
						foobar = bar.split(tld)
						for v in foobar:
							if v != "":
								tmp = str(v+tld).replace("*","")
								if any(x in tmp for x in in_scope) and any(y in tmp for y in out_of_scope) == False:
									if tmp[0] == ".":
										domains.append(tmp[1:])
									else:
										domains.append(tmp)
		domains = list(set(domains))
		print("Assets found: "+str(len(domains)-len(base))+"                                             ")

	# Sublister
	skipDork = confirm("\nSublister recon utilizes OSINT and can take a bit, would you like to do this? (Y/N) ")
	if skipDork != 'N':
		foo = 1
		file = "/tmp/."+''.join(random.choice(string.ascii_lowercase) for i in range(30))
		os.system("/usr/bin/touch "+file)
		print("Using Sublist3r...")
		for i in base:
			print(str(foo)+"/"+str(len(base))+" assets sublisted..",end='\r')
			foo += 1
			tempList = []
			if i[0] == ".":
				bar = i[1:]
			else:
				bar = i
			# Choose a random filename to store temp data
			sublist3r.main(bar,40,savefile=file,ports=None,silent=True,verbose=False,enable_bruteforce=False,engines=None)
			print("Wrote data to temp file!")
			f = open(file,"r")
			tempList = f.read().splitlines()
			f.close()
			for d in tempList:
				if any(x in d for x in in_scope) and any(y in d for y in out_of_scope) == False:
					if d[0] == ".":
						domains.append(d[1:])
					else:
						domains.append(d)
		domains = list(set(domains))
		print("Assets found: "+str(len(domains)-len(base))+"                                             ")
		os.system("/usr/bin/rm "+file)
		print("Temp file removed!")

	skipParse = confirm("\nWould you like to parse the base domains for links and paths? (Note this will produce URIs, not domains) (Y/N) ")
	if skipParse != 'N':
		for i in base:
			try:
				r = requests.get("https://"+i,allow_redirects=True)
			except Exception:
				try:
					r = requests.get("http://"+i,allow_redirects=True)
				except Exception:
					continue
			page = BeautifulSoup(r.text, 'html.parser')
			sl = page.find_all("a")
			for s in sl:
				if s.has_attr("href"):
					foo = s.attrs['href']
					if "/" not in foo[7:]:
						foo = foo.replace("http://","").replace("https://","")
					if any(x in foo for x in in_scope) and any(y in foo for y in out_of_scope) == False:
						domains.append(foo)
		domains = list(set(domains))
		print("Assets found: "+str(len(domains)-len(base))+"                                         ")


	domains = list(set(domains))

	if args.output:
		print("Writing to "+args.output+"...")
		w = open(args.output,'w')
		for i in domains:
			w.write(i+"\n")
		w.close()
		print("Saved to "+args.output+"!")

	if args.noprint:
		print("Execution finished!")
		sys.exit()

	print("\nListing found assets:")
	print("="*50)
	time.sleep(6)
	for i in domains:
		print(i)
	print("="*50)

	grep = ["storage","admin", "it-", "-it", ".it.", "service", "us-east", "prod", "backend", "terraform", "legacy", "vpn", "server", "login", "staging", "portal", "router", "log", "jira", "graphql", "dev", "gateway", "config", "server", "api", "gw", "test", "v1", "mail", "live.", "tools.", "ftp", "vault", "kibana", "staff", "employee", "private", "secret", "euw1", "rtcp", "monitor", "tracking", "us-", "west", "east", "central", "sandbox", "engineering.", "staging", "environment", "beta", "alpha", "camera", "helpdesk", "data", "storage", "lab", "live", "dns", "dc", "jenkins", "sql", "mongo", "base", "wp-login", "eu-", "encrypt", "netbox", "oauth"]
	print("\nPotential good finds:")
	print("="*50)
	time.sleep(6)
	for i in domains:
		if any(x in i for x in grep):
			print(i)
	print("="*50)




if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Quiting.. ")
