-- Create a function with two arguments that will return an array of the first n multiples of x.

-- Assume both the given number and the number of times to count will be positive numbers greater than 0.

-- Return the results as an array or list ( depending on language ).

-- Examples
-- countBy(1,10)  should return  {1,2,3,4,5,6,7,8,9,10}
-- countBy(2,5)  should return {2,4,6,8,10}
-- # write your SQL statement here: 
-- you are given a table 'counter' with columns 'x' (int) and 'n' (int)
-- return a query with columns 'x', 'n' and your result in a column named 'res' (array)
-- sort results by column 'x' ascending, then by 'n' ascending
-- note that each pair of 'x' and 'n' in 'counter' is unique 
CREATE OR REPLACE FUNCTION count_by_x(x INT, n INT) 
  RETURNS INT[] 
  LANGUAGE PLPGSQL
AS
$$
DECLARE
  nums INT[];
BEGIN
  FOR i IN 1..n LOOP
    nums := nums || i * x;
  END LOOP;
  RETURN nums;
END;
$$;

SELECT x, n, count_by_x(x, n) AS res
FROM counter;
