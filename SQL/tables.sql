-- create table people(id int not null, name text, email text, password varchar(25),primary key(id))
-- select * from people


-- ALTER TABLE people
-- ADD city text

-- create table city(id int not null,name varchar(25),country varchar(15),primary key(id))

-- SELECT * FROM rohan_ece.city;

 select * from people left join citys on people.city = citys.id
