import math
#open two files: POSCAR.begin and POSCAR.end
print("Did you put the convert.py with the POSCAR.begin and POSCAR.amend in the same file?")
print('Did you change the CONTCAR names into POSCAR.begin and POSCAR.amend?')
#determine substraction 
#determine the beginning number of line 
data1=data2=[]
f1=open('POSCAR.begin','r')
N1=N1D=1
for line1 in f1:
	data1=line1.split()
	if data1==["Direct"]:
		N1D=N1
		break
	N1=N1+1
f1.close()

#set the same volume with POSCAR.begin
f1=open('POSCAR.begin','r')
N1=N2=N3=1
f3=open('POSCAR','w')
for line1 in f1:
	if N1<=N1D:
		f3.write(line1)
	else:
		break
	N1=N1+1
f1.close()	

X2a=Y2a=Z2a=0
N1=1
f1=open('POSCAR.begin','r')
for line1 in f1:
	data1=line1.split()
	if N1>N1D and data1!=[]:
		x1=data1[0]
		y1=data1[1]
		z1=data1[2]
		
		L=len(x1)-2
		X1=float(x1)
		Y1=float(y1)
		Z1=float(z1)
		f2=open('POSCAR.amend','r')
		N2=1
		for line2 in f2:
			data2=line2.split()
			if N2>N1D and data2!=[]:
				x2=data2[0]
				y2=data2[1]
				z2=data2[2]
				X2=float(x2)
				Y2=float(y2)
				Z2=float(z2)		
				if N2==N1:
					Sx=float(round(X1-X2))
					Sy=float(round(Y1-Y2))
					Sz=float(round(Z1-Z2))
					if abs(Sx)==1.0 or abs(Sy)==1.0 or abs(Sz)==1.0:
						if abs(Sx)==1:
							if X2<0.5:
								X2=math.floor((X2+1)*10**L)/(10**L)
							else:
								X2=math.floor((X2-1)*10**L)/(10**L)						
						elif abs(Sy)==1:
							if Y2<0.5:
								Y2=math.floor((Y2+1)*10**L)/(10**L)
							else:
								Y2=math.floor((Y2-1)*10**L)/(10**L)
						elif abs(Sz)==1:
							if Z2<0.5:
								Z2=math.floor((Z2+1)*10**L)/(10**L)
							else:
								Z2=math.floor((Z2-1)*10**L)/(10**L)	
						sX2=str(X2)
						sY2=str(Y2)
						sZ2=str(Z2)
						print(sX2,sY2,sZ2)
						line2=line2.replace(line2,'  '+sX2+'  '+sY2+'  '+sZ2+'\n')
						#print(line2)
						f3.write(line2)
					else:
						f3.write(line2)	
			N2=N2+1
		f2.close()
	N1=N1+1
f1.close()
f3.close()

