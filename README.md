WillametteShippingCalculator
============================
* Items (Cost, Weight, Title, fs)
* Standard Shipping Cost Calculation
  * .1-1 pounds $5
  * 1 - 5 pounds $7
  * > 5 pounds $10
  * low weight is inclusive. high weight is exclusive
  * over $100 cost, free shipping (no matter the weight)
  * Some items are on special and have free shipping!
    * don't count in weight

Command Line Options
====================
To run the program:
```
python3 main.py --file dataFiles/normalSales.csv [--shipping (normal|sale)]

--file takes a file name of items (CSV format).

--shipping is optional and takes one option, either normal or sale to determine how to price shipping

```



Student Tasks
=============
* Hook up your group repository to Travis-CI
  * run test_SaleItemUnitTest.py
* Write unittests for each existing class
  * run these unittests via Travis-CI
* Fix any bugs found!


