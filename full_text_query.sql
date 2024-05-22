-- Common Regular Expression Patterns
-- . (dot): Matches any single character except newline.
-- ^: Anchors the match at the start of the string.
-- $: Anchors the match at the end of the string.
-- [...]: Matches any single character listed within the brackets.
-- [^...]: Matches any single character not listed within the brackets.
-- a|b: Matches either a or b.
-- *: Matches 0 or more occurrences of the preceding element.
-- +: Matches 1 or more occurrences of the preceding element.
-- ?: Matches 0 or 1 occurrence of the preceding element.
-- {n}: Matches exactly n occurrences of the preceding element.
-- {n,}: Matches n or more occurrences of the preceding element.
-- {n,m}: Matches between n and m occurrences of the preceding element.
-- %: Represents zero or more characters. It can be used to match any sequence of characters, including an empty sequence.

-- Using the LIKE opereator to simply search for keywords partilal words as well
SELECT * FROM item_table
WHERE item_number_value LIKE '%16mm%';

SELECT * FROM publication
WHERE Aircraft_Model LIKE '%0';

        
DROP INDEX description_index ON publication;
DROP INDEX hyperlink_index ON documents;


CREATE FULLTEXT INDEX hyperlink_index ON documents(see_it);
CREATE FULLTEXT INDEX description_index ON publication(Description, Aircraft_Model);

-- This is using Full-Text Search to search for entire phrases wihtout errors.
SELECT * FROM documents
WHERE MATCH(see_it) AGAINST('Sikorsky' IN NATURAL LANGUAGE MODE);


-- Example of using Boolean mode for FTS to search for Partial matches within the database 
SELECT * FROM publication
WHERE MATCH(Description,Aircraft_Model) AGAINST('300' IN BOOLEAN MODE);

-- Example Using Binary-Tree index
CREATE INDEX pic_index ON picture(Item_number);
SELECT Item_number,see_it  FROM picture WHERE Item_number = 'Nega0061';

