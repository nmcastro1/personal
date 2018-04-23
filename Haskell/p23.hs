--P23 - Abundant sum

import Data.List

divisors :: Int -> [Int]
divisors n = 1:[x | x <- [2..(n `div` 2)], (n `mod` x) == 0]

abundant' n = n < (sum $ divisors n)

abundants' = [ a | a <- [1..10000], abundant' a]

abSum' = let abby = abundants' in nub [x + y | x <- abby, y <- abby]

p23' = length $ filter (<28123) abSum

--2nd try
isPrime n (x:xs) = (x*x > n) || (mod n x /= 0) && (isPrime n xs)
primes :: [Int]
primes = 2 : filter (\x -> isPrime x primes) [3,5..]

fact n = multSet $ factorize n primes

factorize :: Int -> [Int] -> [Int]
factorize 1 _ = []
factorize n (p:ps)
  | n `mod` p == 0  = p: factorize (n `div` p) (p:ps)
  | otherwise       = factorize n ps

multSet =  foldl insertMS []

insertMS :: [(Int, Int)] -> Int -> [(Int, Int)]
insertMS [] e = [(e,1)]
insertMS ((x,f):ms) e
  | x == e    = (x, (f + 1)) : ms
  | otherwise = (x,f) : insertMS ms e

divSum :: Int -> Int
divSum n = foldl step 1 $ fact n
  where step acc (p,i) = acc * ((p^(i + 1) - 1) `div` (p - 1))

abundant n = n < (divSum n - n)

abundants = [ a | a <- [1..10000], abundant a]

abSum = let abby = abundants in [x + y | x <- abby, y <- abby]