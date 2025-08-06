CREATE TABLE IF NOT EXISTS questions_sql (
    id SERIAL,
    question_text TEXT NOT NULL,
    date_addition TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_used_date TIMESTAMP WITH TIME ZONE,
    CONSTRAINT ck_last_used_date CHECK (last_used_date IS NULL OR last_used_date >= date_addition),
    CONSTRAINT question_sql_id PRIMARY KEY (id)
);
