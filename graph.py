a=[[0,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,1,0],[0,0,1,0,0,1],[1,1,1,0,0,1],[0,0,0,1,1,0]]
c=["a","b","c"]
l=[]
for m in range(len(a)):
	n=m%len(c)				
	l.append({"p":m,"c":c[n]})
for m in range(len(a)):
	n=m%len(c)
	for i in range(len(a[m])):
		if a[m][i]==1:
			k=m;
			while(l[i]["c"]==c[n]):
				k=k+1
				n=k%len(c)
	l[m]["c"]=c[n]
print l
