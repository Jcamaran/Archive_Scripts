DROP TABLE item_table;
DROP TABLE aircraft_model_table;
DROP TABLE doc_type_table;
DROP TABLE documents;
DROP TABLE hardware;
DROP TABLE document_picture;
DROP TABLE picture;
DROP TABLE publication;
DROP TABLE video;



-- SYNTAX
-- SELECT - extracts data from a database
-- UPDATE - updates data in a database
-- DELETE - deletes data from a database
-- INSERT INTO - inserts new data into a database
-- CREATE DATABASE - creates a new database
-- ALTER DATABASE - modifies a database
-- CREATE TABLE - creates a new table
-- ALTER TABLE - modifies a table
-- DROP TABLE - deletes a table
-- CREATE INDEX - creates an index (search key)
-- DROP INDEX - deletes an index




-- Example of syntax that joing queries together
SELECT * FROM documents WHERE Aircraft_Model = 'S-76'
UNION
SELECT * FROM hardware WHERE Aircraft_Model = 'S-76';




-- INSTERTING INTO DATABASE EXMAPLES -----------------------------------------
-- Insert statements for aircraft_model_table
INSERT INTO aircraft_model_table (model_name) VALUES ('S-7070');
INSERT INTO aircraft_model_table (model_name) VALUES ('CH-53E Super Stallion');

-- Insert statements for doc_type_table
INSERT INTO doc_type_table (doc_type) VALUES ('Manga');
INSERT INTO doc_type_table (doc_type) VALUES ('Luffy');

-- Insert statements for item_table
INSERT INTO item_table (item_number_value) VALUES ('Item001');
INSERT INTO item_table (item_number_value) VALUES ('Item002');

INSERT INTO documents (doc_type, Item_number, index_1, index_2, type, reference, see_it, Aircraft_Model, Description, names, date, comment)
VALUES ('Manga', 'Item001', 'IndexA1', 'IndexB1', 'Type1', 'Reference1', 'SeeItPath1', 'S-76', 'Sample description for document 1', 'Name1', '2023-05-17', 'Sample comment for document 1');

INSERT INTO documents (doc_type, Item_number, index_1, index_2, type, reference, see_it, Aircraft_Model, Description, names, date, comment)
VALUES ('Luffy', 'Item002', 'IndexA2', 'IndexB2', 'Type2', 'Reference2', 'SeeItPath2', 'CH-53E Super Stallion', 'Sample description for document 2', 'Name2', '2024-05-17', 'Sample comment for document 2');

-- Insert statements for document_picture
INSERT INTO document_picture (doc_type, Item_number, index_1, index_2, type, reference, see_it, Aircraft_Model, Description, names, date, comment)
VALUES ('Manga', 'Item001', 'IndexP1', 'IndexQ1', 'Type1', 'Reference1', 'SeeItPath1', 'S-76', 'Sample description for document picture 1', 'Name1', '2023-05-17', 'Sample comment for document picture 1');

INSERT INTO document_picture (doc_type, Item_number, index_1, index_2, type, reference, see_it, Aircraft_Model, Description, names, date, comment)
VALUES ('Luffy', 'Item002', 'IndexP2', 'IndexQ2', 'Type2', 'Reference2', 'SeeItPath2', 'CH-53E Super Stallion', 'Sample description for document picture 2', 'Name2', '2024-05-17', 'Sample comment for document picture 2');


INSERT INTO hardware (doc_type, Item_number, index_1, index_2, type, reference, see_it, Aircraft_Model, Description, names, date, comment)
VALUES ('Manga', 'Item001', 'IndexP1', 'IndexQ1', 'Type1', 'Reference1', 'SeeItPath1', 'S-76', 'Sample description for document picture 1', 'Name1', '2023-05-17', 'Sample comment for document picture 1');
