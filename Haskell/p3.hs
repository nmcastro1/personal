--P3 - Largest prime factor

isPrime n (x:xs) = (x*x > n) || (mod n x /= 0) && (isPrime n xs)

primes = 2 : filter (\x -> isPrime x primes) [3..]

p3 n = last $ filter (divisor n) $ takeWhile (\p -> p * p <= n) primes
       where divisor num prime = num `mod` prime == 0