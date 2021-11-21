import numpy as np
data=np.load('spotify.npy',allow_pickle=True,)
#np.savetxt('prueba',data,delimiter=',')
print("ohlasdad",np.shape(data))
print("ohlasdad",len(data.shape))
np.load('spotify.npy',allow_pickle=True)
print(data)

