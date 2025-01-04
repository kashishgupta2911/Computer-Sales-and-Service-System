# Computer-Sales-and-Service-System
*Description*
This project is a simple Computer Sales and Service Management System implemented using Python and SQLite. It provides functionality to manage computer part details, purchase records, service requests, customer feedback, and problem reports. The database is stored in a file named comps.db, and interactions are managed through Python scripts.

*Features*
Computer Part Management:
View available computer parts
Add details about computer parts including quantity and price.

Customer Purchase Records:
Record customer purchases.
Capture details like name, phone number, email, address, and the purchased computer part.

Service Requests:
Allow customers to request computer services.
Record service details for future reference.

Feedback System:
Collect customer feedback, including ratings and comments.

Problem Reporting:
Maintain logs of sales-related and service-related problems.

*Requirements*
Python 3.x
SQLite3

#How to use
1. Setup the Database:
Run the database setup script to create and populate the necessary tables in comps.db.

```python database_setup.py```

2. View Computer Parts:
Use the view_parts() function to display the available parts and their details.

3. Record a Purchase:
Use the buy_part() function to capture customer purchase details.

4. Request a Service:
Use the request_service() function to record a service request.

5. Provide Feedback:
Use the feedback() function to collect ratings and comments from customers

#Future Developments
- add a GUI (probably using tkinter)
