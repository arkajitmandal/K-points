# --- Written By Arkajit Mandal -------------
# --- Debugged By Liwei Wang ----------------


# ----------- Define Your vector as v1 v2 --------------------------------
# 1. THESE ARE YOUR RESIPROCAL VECTORS --------------------------
# 2. YEAHMOP.out contains the K points that are needed to be copied to YAEHMOP


v1 = [0.8789689, 0 ] 
v2 = [-0.4428547,-0.759297318]

#v1  = [-1.5070377058155324,0 ]   
#v2  = [-0.7592973180881675, -1.3018545676985878 ]
#C  =  v1[0] 
#v1 = [1,0]
#v2 = [v2[0]/C,v2[1]/C]

#v1 = [1.0 , 0.0]
#v2 = [0.0 , 2.0 ]
#v1 = [ -7.2026168970 ,  4.1584331861]
#v2 = [0 , 8.5268927904 ]
#================= DONT TOUCH ANYTHING BELOW THIS =========================



def proj(P,A,B):
	P2 = (P[1]*A[0] - P[0]*A[1])/(B[1]*A[0] - B[0]*A[1]) 
	P1 = (P[0] - P2*B[0])/A[0]
	return [P1,P2]

v1p = []
v2p = []
for i in range(-2,3):
	sp = [i*v1[0],i*v1[1]]
	v1p.append([i*v1[0],i*v1[1]])
	for j in range(-2,3):
		if (j!= 0):
			v1p.append([j*v2[0]+sp[0],j*v2[1]+sp[1]])



fob = open("kspace.out", "w+") 

for i in v1p:
	fob.writelines(str(i[0])+"\t"+str(i[1])+"\n")
fob.close()

maxx = 0
maxy = 0
minx = 0 
miny = 0 
for i in v1p:
	if i[0]>maxx:
		maxx = i[0]
	if i[0]<minx:
		minx = i[0]
	if i[1]>maxy:
		maxy = i[1]
	if i[1]<miny:
		miny = i[1]	


maxx = max(maxx,maxy)
maxy = maxx
minx = min(minx,miny)
miny = minx


def dist(a,b):
	return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5


fob = open("kpoint.out", "w+") 
N = 300
start = [minx,miny]
kpoints = [[0,0]] 
for i in range(N) :
	for j in range(N):
		kp = [ minx + (maxx - minx)*float(i)/float(N) , miny + (maxy - miny)*float(j)/float(N)  ] 	
		fob.writelines(str(kp[0]) +"\t"+  str(kp[1]) + "\n" )
		kpoints.append(kp)
fob.close()
		
                           		
K = []		
for i in kpoints:
        #print i
	r0 = dist(i,[0,0])
	accept = True 
	for j in v1p:
	 
		rij  = dist(i,j)
		if rij < r0 :
			accept = False
			break
		
	if accept:
 		K.append(i)







def cow(a):
        l = len(a) + 2

        g = "w" #["v",  "w","ww","vw","/"][random.randint(0,4)]


        print "\n %s \n< %s  >\n %s \n        \   ^__^\n         \  (oo)\_______\n            (__)\       )\/\ \n                ||----%s |\n                ||     ||"%(l*"_",a,l*"-",g)




fob = open("Brilloin.out", "w+")
fob2 = open("YAEHMOP.out", "w+")
fob3 = open("Reconstruct.out", "w+")
import os
#os.system("echo %s K-points | python ../cow.py"%(len(K)) )

cow("K- points : %s"%(len(K)))

fob2.writelines("%s\n\n"%(len(K))) 

for i in K:
	 
	P = proj(i,v1,v2)
	fob2.writelines(str(P[0])+"\t"+str(P[1])+ "\t0.0\t 1.0\n")
	R1 = P[0]*v1[0] + P[1]*v2[0]  
	R2 = P[0]*v1[1] + P[1]*v2[1] 
	fob3.writelines(str(R1)+"\t"+str(R2)+ "\t0.0\t 1.0\n")
	fob.writelines(str(i[0])+"\t"+str(i[1])+ "\t0.0\t 1.0\n")
fob.close()
fob2.close()
#fob3.close()

