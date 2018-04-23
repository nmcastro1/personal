--P4 - Largest palindrome product of two 3-digit numbers

p4 = maximum products

products = [x * y | x <- [100..999], y <- [100..999] , palindrome (x * y)]

palindrome n = let ds = digitList n []
			   in ds == reverse ds

digitList :: Int -> [Int] -> [Int]
digitList n ds
	| n < 10 	= (n:ds)
	| otherwise	= digitList (n `div` 10) ((n `mod` 10):ds)