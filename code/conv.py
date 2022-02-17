def convlayer(X, W, Y):
	for u in range(len(Y)):  # boucle sur les f.maps de Y
		for v in range(len(X)):
			conv(X[v], W[u,v], Y[u])
