import pandas as pd
import customer_file 
# new customers in same time interval (I think this is the one we need)
class Supermarkt:
    def __init__ (self,number_customer:int,start_date='2022-02-01 07:00:00',time_delta='1T'):
        self.number_customer=number_customer
        self.start_date =start_date 
        self.time_delta=time_delta

    # Calls Customer class and generates new customer
    def new_customer_df(self):
        # new customer
        customer_df = pd.DataFrame(columns=['location'])
        customer_df['location']=customer_file.CustomerClass().next_state()
        # Giving the new_customer df timestamp
        date_range = pd.date_range(self.start_date, periods=len(customer_df), freq = self.time_delta)
        customer_df['timestamp'] =date_range
        column_names = ['timestamp', 'customer_no', 'location']
        customer_df= customer_df.reindex(columns=column_names) 
        return customer_df

    # generates multiple customers, and gives them customer no
    def simulate_customers(self):       
        all_customers=pd.DataFrame([])
        for i in range (self.number_customer):
            df=self.new_customer_df()
            customer_no = [i+1] * len(df)
            df['customer_no']=customer_no                       #generate customer_no
            all_customers =all_customers.append(df, ignore_index=True)                 
        return  all_customers 
  
test=Supermarkt(5).simulate_customers()
test.to_csv('simulation_data.csv')
print(test)
