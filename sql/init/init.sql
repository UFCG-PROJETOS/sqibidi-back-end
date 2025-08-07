CREATE TABLE IF NOT EXISTS questions_sql (
    id SERIAL,
    question_text TEXT NOT NULL,
    question_type TEXT NOT NULL,
    date_addition TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_used_date TIMESTAMP WITH TIME ZONE,
    CONSTRAINT id_question_sql PRIMARY KEY (id),
    CONSTRAINT ck_last_used_date CHECK (last_used_date IS NULL OR last_used_date >= date_addition),
    CONSTRAINT ck_question_type CHECK (question_type IN ('SELECT', 'UPDATE', 'DELETE', 'CREATE'))
);