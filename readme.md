Welcome to Consumer Update project

***Used Python and pip Version***

python 3.8

pip version 19.3.1

***Input FIle***
Along with db.sql, i have made a migration script (migration.sql) to alter the table t_shops and add a column there 
'processed'.

This column is significant for the application as, it will remove the redundant notification sending to the shops

If the shops is offline or notification is already sent, then the column 'processed' will set
to 1. The next time when application will run and get this shops record, it will 
not send new notifications in the same month

Also, I have added some more records for the november month in table t_budgets to test the scenarios.

***Run the Application***

Run the application using the following statement

to load the table and migration script

```
python application.py migration
```

To run the application

```
python application.py process
```

This will run the application and send the notification for the shops