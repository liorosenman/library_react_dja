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
-- CREATE OR REPLACE FUNCTION get_all_customers()
-- RETURNS TABLE(id INTEGER, name TEXT, city TEXT, age INTEGER)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     RETURN QUERY
--     SELECT c.id, c.name, c.city, c.age
--     FROM base_customer c;
-- END;
-- $$;

CREATE OR REPLACE FUNCTION get_all_customers()
RETURNS TABLE(user_id INTEGER, username TEXT, name TEXT, city TEXT, age INTEGER) AS $$
BEGIN
    RETURN QUERY
    SELECT u.id AS user_id, u.username, c.name, c.city, c.age
    FROM auth_user u  
    JOIN base_customer c ON c.user_id = u.id;  
END; $$ LANGUAGE plpgsql;







