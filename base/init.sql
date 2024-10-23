CREATE OR REPLACE PROCEDURE add_book(
    p_name TEXT,
    p_author TEXT,
    p_year_published INTEGER,
    p_borrow_time INTEGER,
    p_filename TEXT,
    p_status TEXT DEFAULT 'available'
)
-- RETURNS VOID AS $$
LANGUAGE plpgsql
AS $$
BEGIN
    -- Insert into the books table
    INSERT INTO base_book (name, author, year_published, borrow_time, filename, status)
    VALUES (p_name, p_author, p_year_published, p_borrow_time, p_filename, p_status);
END;
$$;

-- CREATE OR REPLACE PROCEDURE add_customer(
--     p_username TEXT,
--     p_password TEXT,
--     P_name TEXT,
--     p_city TEXT,
--     p_age INTEGER,
-- )


-- CREATE OR REPLACE PROCEDURE get_all_customers()
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     SELECT * FROM base_customer;
-- END;
-- $$;
-- -----------------------------------------------------------------------
CREATE OR REPLACE FUNCTION get_all_customers()
RETURNS TABLE(id INT, name TEXT, city TEXT, age INTEGER)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT id, name, city, age
    FROM base_customer;
END;
$$;






