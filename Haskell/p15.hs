--P15 - Lattice poths from 0,0 to 20,20

lattice :: (Int, Int) -> Int
lattice (0,_) = 1
lattice (_,0) = 1
lattice (a,b) = lattice (a-1,b) + lattice (a, b-1)

latticeList 0 n = 0: (replicate n 1)
latticeList k n = latListGen 0 $ latticeList (k-1) n

latListGen 0 (p:ps) = 1 : latListGen 1 ps
latListGen c [] = []
latListGen c (p:ps) = (c+p) : latListGen (c+p) ps

p15 = last $ latticeList 20 20