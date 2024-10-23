CREATE OR REPLACE PROCEDURE add_book(
    p_name VARCHAR,
    p_author VARCHAR,
    p_year_published INT,
    p_borrow_time INT,
    p_filename VARCHAR,
    p_status VARCHAR DEFAULT 'available'
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insert into the books table
    INSERT INTO base_book (name, author, year_published, borrow_time, filename, status)
    VALUES (p_name, p_author, p_year_published, p_borrow_time, p_filename, p_status);
END;
$$;

CREATE OR REPLACE PROCEDURE add_customer(
    p_username VARCHAR,
    p_password VARCHAR,
    P_name VARCHAR,
    p_city VARCHAR,
    p_age INT,
)
LANGUAGE plpgsql
AS $$
BEGIN

END
AS $$


