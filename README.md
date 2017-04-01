# JanLinders-Webscraper
Web scraper that collects information about products at Jan linders.

# How to use:
All information is uploaded to a MySQL database. 
You can either run one locally using a program like xampp or get free hosting at a company.

Change your credentials and database name in the db.py file to your own.

In your sql server create this table:
```sql
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `price` double NOT NULL,
  `brand` varchar(45) NOT NULL,
  `weight` varchar(45) NOT NULL,
  `group` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=latin1;
```
