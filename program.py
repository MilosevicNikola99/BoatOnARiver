import numpy as np 
import matplotlib.pyplot as plt 

plt.rcParams['figure.figsize'] = (14,9)

#sirina reke
D = 100
#brzina reke
u = np.array([0.0,-2.0])
#vremenski korak
dt = 0.1


#Driving with constant velocity


#Plotujemo zavisnost trajanja puta od ugla vektora brzine
thetas = np.linspace(np.deg2rad(-60), np.deg2rad(60), 100)
vbps = 5 * np.array([np.cos(thetas), np.sin(thetas)]).T
vbs = u + vbps
ts = []

plt.xlabel('x')
plt.ylabel('y')
for vb in vbs:
    t = 0
    r = np.array([0.0,0.0])
    while(r[0] < D):
        r += vb * dt
        t += dt
    ts.append(t)

plt.plot(np.rad2deg(thetas), ts)
plt.xlabel('angle')
plt.ylabel('time(s)')
plt.title('Duration of the voyage')
plt.show()


#Driving with varying velocity
t, x, y = np.loadtxt('boatvelocity.d', usecols=[0,1,2], unpack=True)
n = len(t)
dt = t[1] - t[0]
v = np.zeros((n,2), np.float64)
v[:,0] = x
v[:,1] = y
r = np.zeros((n,2), np.float64)

r[0] = np.array([0.0,0.0])
for i in range(1,n):
    r[i] = r[i-1] + (v[i-1]+u)*dt

plt.plot(r[:,0],r[:,1])
plt.xlabel('x [m]'), plt.ylabel('y [m]')
plt.axis('equal')
plt.title('Trajectory of a boat with varying velocity')
plt.show()

#Najbolji nacin da iz (0,0) dodjemo do (D,0) tako sto prvo predjemo reku po nekom pravcu,
#pa se duz obale dovezemo do (D,0)



#Plotujemo putanje broda za brzine razlicitih
#pravcaca, ali istog intenziteta
thetas = np.linspace(np.deg2rad(-60), np.deg2rad(60), 100)
vbps = 5 * np.array([np.cos(thetas), np.sin(thetas)]).T
vbs = u + vbps
ts = []

for vb in vbs:
    t = 0
    r = np.array([0.0,0.0])
    #Brod prvo pelazi reku po pravcu
    while r[0] < D:
        r += vb * dt
        t += dt

    #Pa obalom dolazi do tacke (D,0)
    if(r[1] > 0):
        vb = np.array([0, -5]) + u
        smer = -1
    else:
        vb = np.array([0,5]) + u
        smer = +1
    while smer*r[1] < 0:
        r += vb * dt
        t += dt

    ts.append(t)

#Plotujemo zavisnost trajanja puta od ugla

plt.plot(np.rad2deg(thetas), ts)
plt.xlabel('angle')
plt.ylabel('time(s)')
plt.title('Duration of the voyage from (0,0) to (D,0) for a boat with constant velocity')
plt.show()

