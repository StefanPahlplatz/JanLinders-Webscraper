# JanLinders-Webscraper
> Web scraper that collects information about products at Jan linders.

Gets its data from [jan linders](http://www.janlinders.nl/ons-assortiment.html).


# How to use
All information is uploaded to a MySQL database. 
You can either run a database server locally using a program like xampp,
or get a company to host one for you.

Change your credentials and database name in the db.py file to your own login details.

The table that is automatically created in your database will look like this:
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

# Todo
- [x] Improve UI.
- [x] Show elapsed time when done.
- [ ] Scrape offers page and store them in a seperate table.
- [ ] Option to choose which groups to scrape.
- [ ] Build test to see if the site structure is still the same.
