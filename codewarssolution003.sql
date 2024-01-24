-- # write your SQL statement here: you are given a table 'disemvowel' with column 'str', return a table with column 'str' and your result in a column named 'res'.
SELECT str, TRANSLATE(str, 'AEIOUaeiou', '') AS res
FROM disemvowel;