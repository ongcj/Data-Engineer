CREATE TABLE IF NOT EXISTS team (
    team_id             BIGSERIAL           PRIMARY KEY,
    name                VARCHAR(20)         NOT NULL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id         BIGSERIAL           PRIMARY KEY,
    name                VARCHAR(20)         NOT NULL,
    phone               VARCHAR(20)         NOT NULL
);

CREATE TABLE IF NOT EXISTS cars (
    car_id              BIGSERIAL           PRIMARY KEY,
    manufacturer        VARCHAR(20)         NOT NULL,
    model               VARCHAR(20)         NOT NULL,
    serial_number       VARCHAR(20)         NOT NULL,
    price               DOUBLE PRECISION    CHECK (NOT NULL AND price > 0),
    weight              DOUBLE PRECISION    NOT NULL

);

CREATE TABLE IF NOT EXISTS sales_persons (
    sale_person_id      BIGSERIAL           PRIMARY KEY,
    name                VARCHAR(20)         NOT NULL,
    phone               VARCHAR(20)         NOT NULL,
    team_id             BIGSERIAL           REFERENCES team (team_id)
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id      BIGSERIAL           PRIMARY KEY,
    car_id              BIGSERIAL           REFERENCES cars (car_id),
    sales_person_id     BIGSERIAL           REFERENCES sales_persons (sale_person_id),
    customer_id         BIGSERIAL           REFERENCES customers(customer_id),
    purchase_price      DOUBLE PRECISION    NOT NULL,
    transaction_date    DATE                NOT NULL,
    transaction_time    TIME                NOT NULL
);
