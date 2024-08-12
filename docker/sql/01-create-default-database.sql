SELECT 'CREATE DATABASE jet_db' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'jet_db');
\connect jet_db;