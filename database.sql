drop database railway;
create database railway;
use railway;

create table list_of_train(train_no int ,train_name varchar(100),start_time time,start_st_id bigint ,end_time time,end_st_id bigint,journey_time time);
create table route(train_no int,st_id bigint,ar_time time);
 create table stations(st_id varchar(100),st_mgr varchar(100),st_name varchar(100));
create table passenger(pnr_no int,train_no int,boarding_st_id varchar(100),dest_st_id varchar(100),p_id int );
create table users(p_id int ,p_name varchar(100),dob date,age int ,gender varchar(100),mobile_no int);
create table payments(pnr int ,p_id int,amount int ,pay_id int);
create table  coach (c_type varchar(100),c_price int);
insert into list_of_train values(12222,'rajdhani','05:55:00',999,'08:55:00',1100,'03:00:00');
insert into list_of_train values(12290,'shatbdi exp','05:55:00',999,'10:55:00',1230,'05:00:00');
insert into list_of_train values(12899,'chennai exp','09:55:00',999,'10:55:00',1100,'25:00:00');
insert into list_of_train values(100023,'roorkee exp','08:55:00',999,'08:55:00',1600,'24:00:00');
insert into list_of_train values(14000,'ju_haridwar','19:55:00',999,'03:55:00',1200,'11:00:00');
 insert into list_of_train values(18966,'ju_ranchi','17:55:00',1955,'23:55:00',1200,'07:00:00');
insert into list_of_train values(18888,'ju_jaipur','18:55:00',1899,'06:55:00',1200,'14:00:00');
insert into list_of_train values(17888,'ju_ujjain','10:55:00',1989,'01:55:00',1400,'03:00:00');
insert into list_of_train values(14813,'ju_bpl','16:55:00',999,'11:55:00',1000,'17:00:00');
 insert into list_of_train values(14815,'ju_indore','16:55:00',999,'01:55:00',1200,'09:00:00');
insert into coach values('1st ac',2000);
insert into coach values('2nd ac',1500);
 insert into coach values('3rd ac',1000);
insert into coach values('sleeper',500);
insert into coach values('general',200);
 insert into users values(1,'sagar','2000-02-15',22,'male','99999999');
insert into users values(2,'smriti','1995-06-22',27,'female',88888888);
insert into users values(3,'rakhi','1980-06-12',42,'female',77777777);
insert into users values(4,'sakshi','1996-09-30',26,'female',66666666);
 insert into users values(5,'rahul','2000-02-13',22,'male',55555555);
insert into users values(6,'vikas','2006-06-22',31,'male',33333333);
insert into users values(7,'vaibhav','1999-08-22',23,'male',99933333);
insert into users values(8,'vaishali','2009-05-22',13,'female',88866666);
insert into users values(9,'sara','2001-07-12',21,'female',888888999);
insert into users values(10,'vibha','1989-06-22',33,'female',88889963);
insert into payments value(123456,1,1500,22222222);
insert into payments value(456789,2,200,33333333);
insert into payments value(789456,3,1500,22225555);
insert into payments value(77778888,4,500,33222222);
 insert into payments value(126789,5,1500,99222222);
insert into payments value(129996,6,1500,88222222);
 insert into payments value(123886,7,1500,85222222);
insert into payments value(4888888,8,200,99966666);
 insert into payments value(4888998,9,500,99889966);
insert into payments value(4888998,10,200,99886666);
 insert into stations values(999,'nitin kumar','bhopal jn');
insert into stations values(1000,'naman kumar','jodhpur jn');
insert into stations values(1200,'sourabh singh','indore jn');
insert into stations values(5000,'ankit kumar','haridwar jn');
 insert into stations values(1500,'archit verma','ranchi jn');
insert into stations values(7000,'rakhi ','jaipur jn');
insert into stations values(1400,'shamita','ujjain jn');
 insert into stations values(1100,'amit ','mumbai central');
insert into stations values(1230,'amar','delhi jn');
insert into stations values(8889,'prithvi teja','chennai jn');
insert into stations values(1600,'amrit singh','roorkee jn');
insert into stations values(999,'nitin kumar','bhopal jn');

insert into route values(14813,'999','16:55:00');
insert into route values(14813,'990','18:55:00');
insert into route values(14813,'998','10:55:00');
insert into route values(14813,'1000','11:55:00');
insert into route values(19203,'999','16:55:00');
insert into route values(19203,'1005','10:55:00');
insert into route values(19203,'1009','12:00:00');
insert into route values(19203,'1200','01:55:00');
insert into route values(14000,'999','19:55:00');
insert into route values(14000,'1209','23:55:00');
insert into route values(14000,'1250','02:55:00');
insert into route values(14000,'5000','03:55:00');
insert into route values(18966,'999','17:55:00');
insert into route values(18966,'5660','20:55:00');
insert into route values(18966,'1500','23:55:00');
insert into route values(18888,'999','18:55:00');
insert into route values(18888,'5631','20:55:00');

insert into route values(18888,'5963','23:55:00');
insert into route values(18888,'7000','06:55:00');
insert into route values(17888,'999','10:55:00');
insert into route values(17888,'1022','12:55:00');
insert into route values(17888,'1400','01:55:00');



insert into route values(12222,'999','05:55:00');
insert into route values(12222,'7899','06:55:00');
insert into route values(12222,'7722','07:55:00');
insert into route values(12222,'1100','08:55:00');
insert into route values(12290,'999','05:55:00');
insert into route values(12290,'9090','09:55:00');
insert into route values(12290,'1230','10:55:00');
insert into route values(12899,'999','09:55:00');
insert into route values(12899,'10000','19:55:00');
insert into route values(12899,'1111','05:55:00');
insert into route values(12899,'8889','10:55:00');
insert into route values(100023,'999','08:55:00');
insert into route values(100023,'12222','11:55:00');
insert into route values(100023,'2566','23:55:00');
insert into route values(100023,'1600','08:55:00');
insert into passenger values(123456,14813,'999','1000',1);
insert into passenger values(456789,19203,'999','1200',2);
insert into passenger values(789456,14000,'999','5000',3);
insert into passenger values(77778888,18966,'999','1500',4);
insert into passenger values(126789,18888,'999','7000',5);
insert into passenger values(129996,17888,'999','1400',6);
insert into passenger values(123886,12222,'999','1100',7);
insert into passenger values(4888888,12290,'999','1230',8);
insert into passenger values(4888998,12899,'999','8889',9);
insert into passenger values(4888998,100023,'999','1600',10);
insert into stations values('990','samar','kota jn');
insert into stations values('998','sakshi','bundi  jn');
insert into stations values('1005','zishan khan','muradabad jn');
 insert into stations values('1009','zayn','mandi jn');
insert into stations values('1209','anil','raj garh jn');
insert into stations values('1250','amar','bhangarh jn');
 insert into stations values('5660','arma','udaipur jn');
insert into stations values('5631','amaren','kanpur jn');
insert into stations values('5963','vinita','up  jn');
insert into stations values('1022','samar agr','bandra jn');

insert into stations values('7899','farzi','hardoi  jn');
insert into stations values('7722','samar singh','banswada jn');
insert into stations values('9090','abhishek','guna jn');
insert into stations values('10000','akash','sawar jn');
insert into stations values('1111','abhijeet','mandsor jn');
insert into stations values('12222','angad','jhalawar jn');
insert into stations values('2566','amreen','madras jn');
alter table route rename column st_id to ar_time;
alter table route modify column ar_time time;


select * from list_of_train;
select * from route;
select * from stations;
select * from passenger;
select * from users;
select * from payments ;





select L.train_no , L.train_name
from list_of_train as L,route as R1,route as R2
where L.train_no = R1.train_no and R1.train_no = R2.train_no and R1.st_id = 999 and R2.st_id = 2566  ;


select st_id , ar_time
                    from route
                    where train_no = 12222 and ar_time < cast('13:00:00' as time)
                    ORDER BY ar_time DESC
                    LIMIT 1  ;






