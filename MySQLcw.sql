create table IF NOT EXISTS persons(id int primary key auto_increment, name varchar(50) not null, gender varchar(2), location varchar(50), age int check(age>0));

select*from persons;

insert into persons(name, gender, location, age) values('Yuvraj','m','Rajasthan',39);

insert into persons(name,gender,age) values('prajakta','f',19);

select * from persons where locaton = null;

select * from persons where locaton = 'null';

select * from persons where locaton is null;

select avg(age) as average_age from persons;