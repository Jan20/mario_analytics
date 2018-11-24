import importlib
import matplotlib.pyplot as plt  
import urllib3

importlib.import_module('mpl_toolkits.mplot3d').__path__

http = urllib3.PoolManager()
r = http.request('GET', 'http://maps-012.appspot.com')


hello = 'Hi ' + r.data.decode("utf-8") 

print(hello)





fig = plt.figure()

x =[1,2,3,4,5,6,7,8,9,10]
y =[5,6,2,3,13,4,1,2,4,8]
z =[2,3,3,3,5,7,9,11,9,10]

ax = fig.add_subplot(111, projection='3d')


ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

print(ax)
plt.show()
