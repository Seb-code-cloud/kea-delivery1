use delivery1;
create view empolyee_sale as
Select employee.employee_id, firstname , lastname, sum(orders.unitprice*orders.quantity) as sold, orders.orderdate
from employee
left join orders
on employee.employee_id = orders.employee_id
group by employee.employee_id, firstname , lastname, orders.orderdate
order by sold desc; 

create view customer_sale as
select customers.customer_id, first_name , last_name, sum(orders.unitprice*orders.quantity) as sold
from customers
left join orders
on customers.customer_id = orders.customer_id
group by customers.customer_id, first_name , last_name
order by sold desc;

create view product_sale as
select productname, sum(orders.unitprice*orders.quantity) as sold
from products
left join orders
on products.product_id = orders.product_id
group by productname
order by sold desc;


create view product_type as
select productname, sum(orders.unitprice*orders.quantity) as sold, products.type1
from products
left join orders
on products.product_id = orders.product_id
group by productname, products.type1
order by sold desc;

