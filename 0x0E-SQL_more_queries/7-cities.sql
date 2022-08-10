-- This script creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE TABLE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY(id),
    FOREIGN KEY(state_id),
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    state_id INT NOT NULL REFERENCES hbtn_0d_usa.state.id,
    name VARCHAR(256) NOT NULL
);

