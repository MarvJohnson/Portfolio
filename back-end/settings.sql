DROP DATABASE portfolio;
CREATE DATABASE portfolio;
CREATE USER portfoliouser WITH CREATEDB PASSWORD 'portfolio';
GRANT ALL PRIVILEGES ON DATABASE portfolio TO portfoliouser;
