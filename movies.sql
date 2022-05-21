CREATE DATABASE Movies;
USE Movies;

CREATE USER dbadmin IDENTIFIED BY 'helloworld';
GRANT ALL ON Movies .* TO 'dbadmin'@'%';
FLUSH PRIVILEGES;

CREATE TABLE MovDetails(
id int auto_increment UNIQUE KEY,
MovieName varchar(50) NOT NULL,
MaleLead varchar(30),
FemaleLead varchar(30),
YearOfRelease char(4) NOT NULL,
Director varchar(30) NOT NULL,
Ratings numeric(1),
primary key(MovieName,YearOfRelease)
);

INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'A Silent Voice','Shoya Ishida','Shoko Nishimiya','2016','Naoko Yamada',5);
INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'Spirited Away','Haku','Chihiro Ogino','2001','Hayao Miyazaki',5);
INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'Ulidavaru Kandanthe','Rakshit Shetty','Thara','2014','Rakshit Shetty',5);
INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'K.G.F: Chapter 1','Yash','Srinidhi Shetty','2018','Prashanth Neel',5);
INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'Lucia','Sathish Neenasam','Sruthi Hariharan','2013','Pawan Kumar',5);
INSERT INTO MovDetails (MovieName, MaleLead, FemaleLead, YearOfRelease, Director, Ratings) values( 'Luca','Jacob Tremblay','Emma Berman','2021','Enrico Casarosa',4);

select * from MovDetails;
