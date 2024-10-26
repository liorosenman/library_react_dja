CREATE OR REPLACE PROCEDURE add_book(
    p_name TEXT,
    p_author TEXT,
    p_year_published INTEGER,
    p_borrow_time INTEGER,
    p_filename TEXT,
    p_status TEXT DEFAULT 'available'
)

LANGUAGE plpgsql
AS $$
BEGIN
    -- Insert into the books table
    INSERT INTO base_book (name, author, year_published, borrow_time, filename, status)
    VALUES (p_name, p_author, p_year_published, p_borrow_time, p_filename, p_status);
END;
$$;

-----------------------------------------------------------------------------------

CREATE OR REPLACE PROCEDURE get_all_customers()
RETURNS TABLE(id INT, name VARCHAR, city VARCHAR, age INT) AS $$
BEGIN
    RETURN QUERY SELECT id, name, city, age FROM base_customer;
END;
$$ LANGUAGE plpgsql;


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

-- CREATE OR REPLACE FUNCTION get_all_customers()
-- RETURNS TABLE (
--     id INT,
--     username VARCHAR,
--     password VARCHAR,
--     name VARCHAR,
--     city VARCHAR,
--     age INT
-- ) AS $$
-- BEGIN
--     RETURN QUERY
--     SELECT 
--         u.id,
--         u.username,
--         u.password,
--         c.name,
--         c.city,
--         c.age
--     FROM 
--         base_customer c
--     JOIN 
--         auth_user u ON c.user_id = u.id;
-- END;
-- $$ LANGUAGE plpgsql;

-- CREATE OR REPLACE PROCEDURE get_all_customers(INOUT ref refcursor)
-- $$ LANGUAGE plpgsql;
-- AS $$
-- BEGIN
--     OPEN ref FOR
--     SELECT 
--         u.id,
--         u.username,
--         u.password,
--         c.name,
--         c.city,
--         c.age
--     FROM 
--         base_customer c
--     JOIN 
--         auth_user u ON c.user_id = u.id;
-- END;


-- CREATE OR REPLACE PROCEDURE get_all_customers(OUT id INT, OUT name TEXT, OUT city TEXT, OUT age INT)
-- LANGUAGE plpgsql
-- AS $$
-- BEGIN
--     FOR id, name, city, age IN SELECT id, name, city, age FROM Customer LOOP
--         RETURN NEXT;
--     END LOOP;
-- END;
-- $$;

CREATE OR REPLACE FUNCTION get_all_customers()
RETURNS SETOF RECORD AS $$
BEGIN
    RETURN QUERY
    SELECT 
        u.id,
        u.username,
        u.password,
        c.name,
        c.city,
        c.age
    FROM 
        base_customer c
    JOIN 
        auth_user u ON c.user_id = u.id;
END;
$$ LANGUAGE plpgsql;











