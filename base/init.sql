-- Create the stored procedure for inserting a book
CREATE OR REPLACE PROCEDURE add_book(
    p_name VARCHAR,
    p_author VARCHAR,
    p_year_published INT,
    p_borrow_time INT,
    p_filename VARCHAR,
    p_status VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insert into the books table
    INSERT INTO app_book (name, author, year_published, borrow_time, filename, status)
    VALUES (p_name, p_author, p_year_published, p_borrow_time, p_filename, p_status);
END;
$$;


CALL add_book(
    'Hammlet',
    'Shakespear',
    1750,
    1,  
    'pic1.jpg',
    'available' 
);
