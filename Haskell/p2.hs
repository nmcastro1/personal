--P2 - Sum of even fibonacci below 4mill

p2 = sum $ takeWhile (<4000000) $ filter (even) (fibonacci 30 [2,1])

fibonacci 0 xs = xs
fibonacci n coso@(x:y:xs) = fibonacci (n-1) ((x + y) : coso)