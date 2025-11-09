print('''
________________________________________
 MongoDB Commands 
________________________________________
1. Listing Databases
show dbs
Description: Lists all databases present in MongoDB.
________________________________________
2. Create a Database
use Employee_25MDT1033
Description: Creates (or switches to) the database named Employee_25MDT1033.
________________________________________
3. Create Collection and Insert Documents
Create a collection named empdetails and insert documents.
(a) Insert One
db.empdetails.insertOne({
    name: "Jake",
    age: 29,
    ID: "E011",
    Deptname: "HR",
    city: "Miami",
    salary: 70000,
    address: "234 st"
})

(b) Insert Many
db.empdetails.insertMany([
    {
        name: "Lisa",
        age: 25,
        ID: "E012",
        Deptname: "Finance",
        city: "Austin",
        salary: 78000,
        address: "891 st"
    },
    {
        name: "Tom",
        age: 26,
        ID: "E013",
        Deptname: "Finance",
        city: "Seattle",
        salary: 20000,
        address: "701 st"
    }
])

________________________________________
 Find (Query) Operations
4. Display All Documents
db.empdetails.find().pretty()

5. Display Output in JSON Format
db.empdetails.find().forEach(doc => printjson(doc))

6. Find Employees in “Sales” Department
db.empdetails.find({ Deptname: "Sales" }).pretty()

7. Find Employee by ID
db.empdetails.find({ ID: "E001" }).pretty()

8. Employees Not from “Salem”
db.empdetails.find({ city: { $ne: "Salem" } }).pretty()

9. Employees with Salary Either 30000 or 60000
db.empdetails.find({ salary: { $in: [30000, 60000] } }).pretty()

10. Display Only Name and ID
db.empdetails.find({}, { name: 1, ID: 1, _id: 0 }).pretty()

11. Employees Younger than 30
db.empdetails.find({ age: { $lt: 30 } }).pretty()
________________________________________
 Update and Sort Operations
12. Add ₹500 Bonus to All Employees
db.empdetails.updateMany({}, { $inc: { salary: 500 } })
db.empdetails.find().pretty()

13. Sort by Age (Ascending)
db.empdetails.find().sort({ age: 1 }).pretty()

14. Sort by Age (Descending)
db.empdetails.find().sort({ age: -1 }).pretty()

15. Update City of Employee with ID “E001”
db.empdetails.updateOne(
    { ID: "E001" },
    { $set: { city: "New City Name" } }
)
db.empdetails.find({ ID: "E001" }).pretty()

16. Count Number of Documents
db.empdetails.countDocuments()

17. Display Distinct Department Names
db.empdetails.distinct("Deptname")

18. Find Maximum Salary
db.empdetails.aggregate([
    { $group: { _id: null, maxSalary: { $max: "$salary" } } }
])

19. Show Average Salary by Department
db.empdetails.aggregate([
    {
        $group: {
            _id: "$Deptname",
            average_salary: { $avg: "$salary" },
            employees: { $push: "$$ROOT" }
        }
    }
])
________________________________________
INDEXING IN MONGODB
________________________________________
1. Create Database
use productsale_24MDT1092

2. Create Collection and Insert Documents
db.orderdetails.insertMany([
    {
        custname: "Ajay",
        aadhaar: "123456789",
        age: 30,
        orderID: 1001,
        productname: "Laptop",
        city: "Delhi",
        price: 50000
    },
    {
        custname: "Tej",
        aadhaar: "567891011",
        age: 25,
        orderID: 1002,
        productname: "Smartphone",
        city: "Chennai",
        price: 10000
    }
])

3. Display Collection
db.orderdetails.find().pretty()
________________________________________
⚙️ Index Operations
4. Create Unique Index on orderID
db.orderdetails.createIndex(
    { orderID: 1 },
    { name: "orderno", unique: true }
)
db.orderdetails.getIndexes()

5. Create Index on aadhaar
db.orderdetails.createIndex({ aadhaar: 1 })
db.orderdetails.getIndexes()

6. Display All Indexes
db.orderdetails.getIndexes()

7. Drop Specific Index
db.orderdetails.dropIndex("orderno")


8. Create Compound Index on custname and orderID
db.orderdetails.createIndex({ custname: 1, orderID: 1 })

9. Drop All Indexes
db.orderdetails.dropIndexes()
db.orderdetails.find().pretty()

10. Sort by OrderID (Descending)
db.orderdetails.find().sort({ orderID: -1 }).pretty()

11. Get Indexes and Display Collection
db.orderdetails.getIndexes()
db.orderdetails.find().pretty()


''')