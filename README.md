# JanLinders-Webscraper
Web scraper that collects information about products at Jan linders.

# How to use:
All information is uploaded to a MySQL database. 
You can either run a database server locally using a program like xampp,
or get a company to host one for you.

Change your credentials and database name in the db.py file to your own login details.

In your MySQL database create this table:
```sql
CREATE TABLE `products` (
  `name` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `brand` varchar(45) NOT NULL,
  `weight` varchar(45) NOT NULL,
  `group` varchar(45) NOT NULL,
  PRIMARY KEY (`name`,`price`,`brand`,`weight`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```
