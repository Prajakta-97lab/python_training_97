use prajakta_db;

create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);

select * from employees;


insert into employees(name, designation , technology, phone_num, commission, salary, years_of_exp) values('Aadya','Secretary','IT',9765412387, 32, 75000,5);

insert into employees(name, designation , technology, phone_num, commission, salary, years_of_exp) values('Arushi','HR','IT',9876532148, 32, 70000,10);

insert into employees(name, designation , technology, phone_num, commission, salary, years_of_exp) values('Preesha','Design_manager','IT',98765312487, 35, 50000,5);

insert into employees(name, designation , technology, phone_num, commission, salary, years_of_exp) values('Prajakta','COO','IT',9875623478, 32, 1,00,000,7);
