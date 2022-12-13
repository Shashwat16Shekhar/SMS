from flask import Flask, jsonify, request, render_template
import json
import time
import cx_Oracle
import os

app = Flask(__name__)

try:
    print("Try")
    uname="sxr3348"
    pwd="Raikaroscar12"
    dom="acaddbprod.uta.edu:1523/pcse1p.data.uta.edu"
    cx_Oracle.init_oracle_client(lib_dir="/Users/Srishti/Downloads/instantclient_21_7")
    print("Connected")

    conn=cx_Oracle.connect(user=uname,password=pwd,dsn=dom)
    cur = conn.cursor()
    # project_root = os.path.dirname(__file__)
    # template_path = os.path.join(project_root)
    # app = Flask(__name__, template_folder=template_path)

except Exception as ex:
    print("Initiation",ex)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')
    
    
@app.route('/viewDBPage', methods=['GET','POST'])
def viewDBPage():
    print("1", request.method)    
    if request.method == 'POST':
        viewData = request.form["viewData"]
        print(viewData)
        if(viewData == "storeRegion"):
            heading="Store Region"
            results=[]
            cols=["REGION_ID","NAME","STREET","CITY","STATE","ZIPCODE"]
            cur.execute('select REGION_ID, NAME, STREET, CITY, STATE, ZIPCODE from Fall22_S004_11_STORE_REGION')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "store"):
            heading="Store"
            results=[]
            cols=["STORE_ID","NAME","REGION_ID"]
            cur.execute('select STORE_ID, NAME, REGION_ID from Fall22_S004_11_STORE')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "expType"):
            heading="Expenditure Type"
            results=[]
            cols=["EXPTYPE_ID","DESCRIPTION"]
            cur.execute('select EXPTYPE_ID, DESCRIPTION from Fall22_S004_11_EXPENDITURE_TYPE')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "exp"):
            heading="Expenditure"
            results=[]
            cols=["EXP_ID","STORE_ID","EXP_DATE","AMOUNT","EXPTYPE_ID"]
            cur.execute('select EXP_ID, STORE_ID, EXP_DATE, Amount, EXPTYPE_ID from Fall22_S004_11_EXPENDITURE')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "cus"):
            heading="Customer"
            results=[]
            cols=["CUST_ID","FIRST_NAME","MIDDLE_NAME","LAST_NAME","DOB","CUST_TYPE","CITY"]
            cur.execute('select CUST_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOB, CUST_TYPE, CITY from Fall22_S004_11_CUSTOMER')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "cusPh"):
            heading="Customer Phone"
            results=[]
            cols=["CUST_ID","PHONE"]
            cur.execute('select CUST_ID, PHONE from Fall22_S004_11_CUSTOMER_PHONE')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "prodCat"):
            heading="Product Category"
            results=[]
            cols=["PRODCAT_ID","DESCRIPTION"]
            cur.execute('select PRODCAT_ID, DESCRIPTION from Fall22_S004_11_PRODUCT_CATEGORY')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "product"):
            heading="Product"
            results=[]
            cols=["PROD_ID","DESCRIPTION","AISLE","PRODCAT_ID"]
            cur.execute('select PROD_ID, DESCRIPTION, AISLE, PRODCAT_ID from Fall22_S004_11_PRODUCT')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "trans"):
            heading="Transaction"
            results=[]
            cols=["TRANS_ID","STORE_ID","CUST_ID","AMOUNT","DISCOUNT","TRANS_DATE","TRANS_TIME","TRANS_TYPE"]
            cur.execute('select TRANS_ID, STORE_ID, CUST_ID, AMOUNT, DISCOUNT, TRANS_DATE, TRANS_TIME, TRANS_TYPE from Fall22_S004_11_TRANSACTION')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "transP"):
            heading="Transaction on Product"
            results=[]
            cols=["TRANS_ID","PROD_ID","QUANTITY","AMOUNT"]
            cur.execute('select TRANS_ID, PROD_ID, QUANTITY, AMOUNT from Fall22_S004_11_TRANSACTION_MADE_ON_PRODUCT')
            for row in cur.fetchall():
                results.append(row)
    return render_template('/viewDBTable.html', results=results, cols=cols, heading=heading)
    
@app.route('/viewDB')
def viewDB():
    print("2")
    return render_template('/viewDB.html')
 
    
@app.route('/updateDBPage', methods=['GET','POST'])
def updateDBPage():
    print("1", request.method)    
    if request.method == 'POST':
        updateData = request.form["updateData"]
        print(updateData)
        if(updateData == "storeRegion"):
            heading="Store Region"
            results=[]
            cols=["REGION_ID","NAME","STREET","CITY","STATE","ZIPCODE"]
            cur.execute('select REGION_ID, NAME, STREET, CITY, STATE, ZIPCODE from Fall22_S004_11_STORE_REGION')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "store"):
            heading="Store"
            results=[]
            cols=["STORE_ID","NAME","REGION_ID"]
            cur.execute('select STORE_ID, NAME, REGION_ID from Fall22_S004_11_STORE')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "expType"):
            heading="Expenditure Type"
            results=[]
            cols=["EXPTYPE_ID","DESCRIPTION"]
            cur.execute('select EXPTYPE_ID, DESCRIPTION from Fall22_S004_11_EXPENDITURE_TYPE')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "exp"):
            heading="Expenditure"
            results=[]
            cols=["EXP_ID","STORE_ID","EXP_DATE","AMOUNT","EXPTYPE_ID"]
            cur.execute('select EXP_ID, STORE_ID, EXP_DATE, Amount, EXPTYPE_ID from Fall22_S004_11_EXPENDITURE')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "cus"):
            heading="Customer"
            results=[]
            cols=["CUST_ID","FIRST_NAME","MIDDLE_NAME","LAST_NAME","DOB","CUST_TYPE","CITY"]
            cur.execute('select CUST_ID, FIRST_NAME, MIDDLE_NAME, LAST_NAME, DOB, CUST_TYPE, CITY from Fall22_S004_11_CUSTOMER')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "cusPh"):
            heading="Customer Phone"
            results=[]
            cols=["CUST_ID","PHONE"]
            cur.execute('select CUST_ID, PHONE from Fall22_S004_11_CUSTOMER_PHONE')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "prodCat"):
            heading="Product Category"
            results=[]
            cols=["PRODCAT_ID","DESCRIPTION"]
            cur.execute('select PRODCAT_ID, DESCRIPTION from Fall22_S004_11_PRODUCT_CATEGORY')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "product"):
            heading="Product"
            results=[]
            cols=["PROD_ID","DESCRIPTION","AISLE","PRODCAT_ID"]
            cur.execute('select PROD_ID, DESCRIPTION, AISLE, PRODCAT_ID from Fall22_S004_11_PRODUCT')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "trans"):
            heading="Transaction"
            results=[]
            cols=["TRANS_ID","STORE_ID","CUST_ID","AMOUNT","DISCOUNT","TRANS_DATE","TRANS_TIME","TRANS_TYPE"]
            cur.execute('select TRANS_ID, STORE_ID, CUST_ID, AMOUNT, DISCOUNT, TRANS_DATE, TRANS_TIME, TRANS_TYPE from Fall22_S004_11_TRANSACTION')
            for row in cur.fetchall():
                results.append(row)
        elif(updateData == "transP"):
            heading="Transaction on Product"
            results=[]
            cols=["TRANS_ID","PROD_ID","QUANTITY","AMOUNT"]
            cur.execute('select TRANS_ID, PROD_ID, QUANTITY, AMOUNT from Fall22_S004_11_TRANSACTION_MADE_ON_PRODUCT')
            for row in cur.fetchall():
                results.append(row)
    return render_template('/updateDBTable.html', results=results, cols=cols, heading=heading)
    
@app.route('/updateDB')
def updateDB():
    print("2")
    return render_template('/updateDB.html')
     
    
    
@app.route('/getResultPage', methods=['GET','POST'])
def getResultPage():
    print("1", request.method)    
    if request.method == 'POST':
        viewData = request.form["BG"]
        print(viewData)
        if(viewData == "BG1"):
            heading="Make a report showing the total expenditures of the store region and the individual stores having expendiature of more than 400000"
            results=[]
            cols=["REGION","STORE NAME","SALES"]
            cur.execute('select sr.NAME as Region,s.NAME as StoreName,  SUM(e.Amount) as Sales from Fall22_S004_11_STORE s inner join Fall22_S004_11_STORE_REGION sr on sr.REGION_ID = s.REGION_ID inner join Fall22_S004_11_EXPENDITURE e on e.STORE_ID = s.STORE_ID group by Rollup(sr.NAME,s.NAME) having SUM(e.Amount) > 400000 order by sr.NAME,s.NAME')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "BG2"):
            heading="Check which date of the month is the store's peak sales day for top 5 performing store based on sales"
            results=[]
            cols=["NAME","MONTH","PEAK DATE","TOTAL SALES"]
            cur.execute('select NAME, EXTRACT(MONTH FROM TRANS_DATE) as Month, EXTRACT(DAY FROM TRANS_DATE) as PeakDate ,SUM(AMOUNT) as TotalSales from Fall22_S004_11_TRANSACTION t inner join Fall22_S004_11_STORE s on s.STORE_ID = t.STORE_ID group by NAME, EXTRACT(MONTH FROM TRANS_DATE), EXTRACT(DAY FROM TRANS_DATE) having SUM(AMOUNT) >= ALL(select SUM(AMOUNT) from Fall22_S004_11_TRANSACTION tt inner join Fall22_S004_11_STORE ss on ss.STORE_ID = tt.STORE_ID where ss.name=s.name group by NAME, EXTRACT(MONTH FROM TRANS_DATE), EXTRACT(DAY FROM TRANS_DATE)) order by TotalSales desc FETCH FIRST 5 ROWS ONLY')
            for row in cur.fetchall():
                results.append(row)
        elif(viewData == "BG3"):
            heading="Analyze the store's sales by customer type and overall sales based on customer type and display first six"
            results=[]
            cols=["NAME","CUST TYPE","TOTAL_SALES"]
            cur.execute('(select pc.DESCRIPTION, sum(QUANTITY) as TOTALQUANTITY from Fall22_S004_11_PRODUCT p inner join Fall22_S004_11_TRANSACTION_MADE_ON_PRODUCT tr on p.PROD_ID = tr.PROD_ID inner join Fall22_S004_11_PRODUCT_CATEGORY pc on pc.PRODCAT_ID = p.PRODCAT_ID group by pc.DESCRIPTION order by sum(QUANTITY) desc FETCH FIRST 1 ROWS ONLY )UNION(select pc.DESCRIPTION, sum(QUANTITY) as TOTALQUANTITY from Fall22_S004_11_PRODUCT p inner join Fall22_S004_11_TRANSACTION_MADE_ON_PRODUCT tr on p.PROD_ID = tr.PROD_ID inner join Fall22_S004_11_PRODUCT_CATEGORY pc on pc.PRODCAT_ID = p.PRODCAT_ID group by pc.DESCRIPTION order by sum(QUANTITY)  FETCH FIRST 1 ROWS ONLY)')
            for row in cur.fetchall():
                results.append(row)
    return render_template('/getResultTable.html', results=results, cols=cols, heading=heading)

@app.route('/getResult')
def getResult():
    print("2")
    return render_template('getResult.html')
    
    
if __name__ == "__main__":
    app.run(debug=True)