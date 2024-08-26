create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null, gender varchar(2), location varchar(50), age int check(age>0));

select*from persons;

insert into persons(name,gender,location,age) values('prajakta','f','Hubli',19);

insert into persons(name, gender, location, age) values('Yuvraj','m','Rajasthan',39);

insert into persons(name, gender, location, age) values('Rudra','m','Rajasthan',23);

insert into persons(name, gender, location, age) values('Tristain','m','Shadowport',28);

insert into persons(name, gender, location, age) values('Dante','m','Tenebrae',32);

insert into persons(name,location,age) values('Aadya','Hubli',20);

select * from persons;

select name, location from persons;

select loaction from persons;

select distinct location from persons;

select * from persons where age>8;

select * from persons where  location = 'Hubli';

select *  from persons where name like 'a%a';

select *  from persons where name like 'a___a';

insert into persons(name,location,age) values('shikha','Hubli',50);

select * from persons where location in ('Hubli','Rajasthan');

select * from persons where age between 20 and 50;